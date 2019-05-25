import re
import argparse

precedence_map = {'(':1, '|':2, '.':3, '?':4, '*':4, '+':4}

def getPrecedence(char):
    try:
        precedence = precedence_map[char]
        return precedence
    except KeyError:
        return 6

def concatenate(regex):
    new_regex = ''
    operators_c = ['(','|']
    operators_next_c = [')','*','?','+', '|']
    for i,c in enumerate(regex):
        new_regex += c
        if(i == len(regex)-1):
            break
        next_c = regex[i+1]

        if c not in operators_c and next_c not in operators_next_c:
            new_regex += '.'

    return new_regex

def infix_to_postfix(r):
    regex = concatenate(r)

    postfix = ''
    stack = []

    for c in regex:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while len(stack) > 0:
                peeked_char = stack[-1]

                curr_char_precedence = getPrecedence(c)
                peeked_char_precedence = getPrecedence(peeked_char)

                if peeked_char_precedence >= curr_char_precedence:
                    postfix += stack.pop()
                else:
                    break

            stack.append(c)

    while len(stack) > 0:
        postfix += stack.pop()

    return postfix

def symbol_nfa(symbol):
    global count
    nfa = []

    state = ["q"+str(count), "q"+str(count+1)]
    alphabets = [symbol]
    start = "q"+str(count)
    count+=1
    end = ["q"+str(count)]
    count+=1
    transition = [(start,symbol,end)]

    nfa.append(state)
    nfa.append(alphabets)
    nfa.append(start)
    nfa.append(end)
    nfa.append(transition)

    return nfa

def concat_nfa(nfa_1, nfa_2):
    new_nfa = []

    new_states = nfa_1[0] + nfa_2[0]
    new_states.remove(nfa_2[2])
    new_alphabets = list(set().union(nfa_1[1], nfa_2[1]))
    new_start = nfa_1[2]
    new_ends = nfa_2[3]

    for i in range(len(nfa_2[4])):
        if nfa_2[4][i][0] == nfa_2[2]:
            lst = list(nfa_2[4][i])
            lst[0] = nfa_1[3][0]
            nfa_2[4][i] = tuple(lst)

    new_transitions = nfa_1[4] + nfa_2[4]

    new_nfa.append(new_states)
    new_nfa.append(new_alphabets)
    new_nfa.append(new_start)
    new_nfa.append(new_ends)
    new_nfa.append(new_transitions)

    return new_nfa

def union_nfa(nfa_1, nfa_2):
    global count
    new_nfa = []

    new_states = nfa_1[0] + nfa_2[0]
    new_alphabets = list(set().union(nfa_1[1], nfa_2[1],' '))
    new_start = "q"+str(count)
    count += 1
    new_end = ["q"+str(count)]
    count += 1
    new_transitions = nfa_1[4] + nfa_2[4]
    new_transitions.append((new_start,' ', [nfa_1[2]]))
    new_transitions.append((new_start,' ', [nfa_2[2]]))
    for l in nfa_1[3]:
        new_transitions.append((l,' ', [new_end[0]]))
    for l in nfa_2[3]:
        new_transitions.append((l,' ', [new_end[0]]))

    new_states.append(new_start)
    new_states += new_end

    new_nfa.append(new_states)
    new_nfa.append(new_alphabets)
    new_nfa.append(new_start)
    new_nfa.append(new_end)
    new_nfa.append(new_transitions)

    return new_nfa

def kleene_star_nfa(nfa):
    global count
    new_nfa = []

    new_states = nfa[0]
    new_alphabets = list(set().union(nfa[1],' '))
    new_start = "q"+str(count)
    count += 1
    new_end = ["q"+str(count)]
    count += 1
    new_transitions = nfa[4]

    new_transitions.append((new_start,' ', [new_end[0]]))
    new_transitions.append((new_start,' ', [nfa[2]]))
    for l in nfa[3]:
        new_transitions.append((l,' ', [new_end[0]]))
        new_transitions.append((l,' ', [nfa[2]]))

    new_states.append(new_start)
    new_states += new_end

    new_nfa.append(new_states)
    new_nfa.append(new_alphabets)
    new_nfa.append(new_start)
    new_nfa.append(new_end)
    new_nfa.append(new_transitions)

    return new_nfa

def one_or_more_nfa(nfa):
    global count
    new_nfa = []

    new_states = nfa[0]
    new_alphabets = list(set().union(nfa[1],' '))
    new_start = "q"+str(count)
    count += 1
    new_end = ["q"+str(count)]
    count += 1
    new_transitions = nfa[4]

    new_transitions.append((new_start,' ', [nfa[2]]))
    for l in nfa[3]:
        new_transitions.append((l,' ', [new_end[0]]))
        new_transitions.append((l,' ', [nfa[2]]))

    new_states.append(new_start)
    new_states += new_end

    new_nfa.append(new_states)
    new_nfa.append(new_alphabets)
    new_nfa.append(new_start)
    new_nfa.append(new_end)
    new_nfa.append(new_transitions)

    return new_nfa

def zero_or_one_nfa(nfa):
    global count
    new_nfa = []

    new_states = nfa[0]
    new_alphabets = list(set().union(nfa[1],' '))
    new_start = nfa[2]
    new_end = ["q"+str(count)]
    count += 1
    new_transitions = nfa[4]

    new_transitions.append((new_start,' ', [new_end[0]]))
    for l in nfa[3]:
        new_transitions.append((l,' ', [new_end[0]]))

#     new_states.append(new_start)
    new_states += new_end

    new_nfa.append(new_states)
    new_nfa.append(new_alphabets)
    new_nfa.append(new_start)
    new_nfa.append(new_end)
    new_nfa.append(new_transitions)

    return new_nfa

def print_nfa(nfa):
    states = ", ".join(nfa[0])
    alphabets = ", ".join(nfa[1])
    start = nfa[2]
    ends = ", ".join(nfa[3])
    # transitions = ", ".join(map(str, nfa[4]))

    s = ""

    s += states + "\n"
    s += alphabets + "\n"
    s += start + "\n"
    s += ends + "\n"
    # s += transitions + "\n"
    for t in nfa[4]:
        s += '('
        # s += (", ".join([str(s1) for s1 in list(t)]))
        s += (", ".join([str(s1) if type(s1).__name__ == 'str' else ''.join(s1) for s1 in list(t)]))
        s += '), '

    return s[:len(s)-2]


def regex_to_nfa(regex):
    global count
    new_regex = infix_to_postfix(regex)
    operators = ['.','*','+','|','?']
    stack = []
    count = 0

    for c in new_regex:
        if c not in operators:
            nfa = symbol_nfa(c)
            stack.append(nfa)

        elif c == '.':
            nfa1 = stack.pop()
            nfa2 = stack.pop()
            nfa = concat_nfa(nfa2, nfa1)
            stack.append(nfa)

        elif c == '*':
            nfa = kleene_star_nfa(stack.pop())
            stack.append(nfa)

        elif c == '+':
            nfa = one_or_more_nfa(stack.pop())
            stack.append(nfa)

        elif c == '|':
            nfa1 = stack.pop()
            nfa2 = stack.pop()
            nfa = union_nfa(nfa2, nfa1)
            stack.append(nfa)

        elif c == '?':
            nfa = zero_or_one_nfa(stack.pop())
            stack.append(nfa)

    return stack.pop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


t  = open(args.file, "r")
regex_s = t.read()


count = 0

nfa = regex_to_nfa(regex_s)
s = print_nfa(nfa)

result = open("task_2_result.txt", "w")
result.write(s)
result.close()
























#

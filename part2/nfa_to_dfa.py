import re
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


t  = open(args.file, "r")

text = t.read()

#PARSING THE INPUT
nfa = text.split('\n')
states = nfa[0].split(',')
alphabets = [a.strip() for a in nfa[1].split(',')]
alphabets = [' ' if len(a) == 0 else a for a in alphabets]
start_state = nfa[2]
final_states = nfa[3].split(',')
a = re.findall('\([^)]*\)',nfa[4])
b = [el.strip('()') for el in a]
c = [el.split(',') for el in b]
transitions = [tuple(el2.strip() for el2 in el) for el in c]
for i in range(len(transitions)):
    t = transitions[i]
    if t[1] == '':
        x = list(t)
        x[1] = ' '
        transitions[i] = tuple(x)

def find_epsilon_transitions(state, transitions):
    states = state
    for s in states:
        for tpl in transitions:
            if tpl[0] == s and tpl[1] == ' ' and tpl[2] not in states:
                states.append(tpl[2])

    states = list(set(states))
    return states

def new_state(alphabet, states):
    to_states = []
    for tpl in transitions:
            if tpl[0] in states and tpl[1] == alphabet:
                to_states.append(tpl[2])

    new_to_states = find_epsilon_transitions(to_states, transitions)

    return new_to_states

def is_final_state(states):
    return common_member(states, final_states)

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False

def print_output():
    out = ''
    out = ', '.join(map(str, DFA_states)) + '\n'
    out += ','.join(map(str, DFA_alphabets)) + '\n'
    out += DFA_start_state + '\n'
    out += ', '.join(map(str, DFA_finals)) + '\n'

    for t in DFA_transitions:
        out += '('
        out += (", ".join([str(s) for s in list(t)]))
        out += '), '

    return out if len(DFA_transitions) == 0 else out[:len(out)-2]



DFA_alphabets = alphabets
if ' ' in DFA_alphabets:
    DFA_alphabets.remove(' ')
count_char = '0'
DFA_start_state = '0'
DFA_states = []
DFA_finals = []
DFA_transitions = []

DFA_states.append(count_char)
nfa_start = find_epsilon_transitions([start_state], transitions)
if is_final_state(nfa_start):
    DFA_finals.append(count_char)

nfa_to_dfa = [[count_char, nfa_start]]

for state in nfa_to_dfa:
    for alphabet in DFA_alphabets:
        current_states = new_state(alphabet, state[1])
        if not current_states:
            DFA_states = list(set().union(DFA_states, ['DEAD']))
            DFA_transitions.append((state[0], alphabet, 'DEAD'))
            continue

        #check if current_states already has a state in dfa
        flag = False
        current_dfa_state = ''
        for l in nfa_to_dfa:
            if set(l[1]) == set(current_states):
                flag = True
                current_dfa_state = l[0]
                break
        if not flag:
            count_char = chr(ord(count_char) + 1)
            current_dfa_state = count_char
            DFA_states.append(count_char)
            nfa_to_dfa.append([count_char, current_states])

        DFA_transitions.append((state[0], alphabet, current_dfa_state))

        if is_final_state(current_states): #check if it contains a final state
            DFA_finals.append(current_dfa_state)

if 'DEAD' in DFA_states:
    for alphabet in DFA_alphabets:
        DFA_transitions.append(('DEAD', alphabet, 'DEAD'))

DFA_finals = sorted(list(set(DFA_finals)))

output = print_output()
result = open("task_2_2_result.txt", "w")
result.write(output)
result.close()































#

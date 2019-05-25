import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


t  = open(args.file, "r")

text = t.read().strip()

rules = []
non_terminals = []
first = dict()

#SPLIT INPUT
spl = text.split('\n')
for r in spl:
    rule = r.split(':')
    rhs = rule[1].split('|')
    rhs = [s.strip() for s in rhs]
    r = rule[0].strip()
    rules.append([r, rhs])
    first[r] = set([])
    non_terminals.append(r)

def allTerminals(rule):
    terminals = []
    splt = rule.split(' ')
    for s in splt:
#         if not s.isupper():
        if s not in non_terminals:
            terminals.append(s)

    return terminals


for rule in rules:
    lhs = rule[0]
    rhs = rule[1]
    for s in rhs:
        terminals = allTerminals(s)

        for terminal in terminals:
            if terminal not in first:
                if terminal != 'epsilon':
                    first[terminal] = set([terminal])

        if len(s.split(' ')) == 1 and len(terminals) == 1:
            if lhs not in first:
                first[lhs] = set([terminals[0]])
            else:
                first[lhs].add(terminals[0])

#FIRST
def all_epsilon(nonterminals):
    for rule in nonterminals:
#         print(rule)
        if rule != 'epsilon' and 'epsilon' not in first[rule]:
            return False

    return True

def find_firsts(nonterminals):
    s = set([])

    for rule in nonterminals:
        s.update(first[rule])

    return s - {'epsilon'}


change = True
x = 0
while change:
    change = False
    for R in rules:
        lhs = R[0]
        for rhs in R[1]:
            splt = rhs.split(' ')
            if splt[0] == 'epsilon':
                continue
            if all_epsilon(splt):
                first[lhs].update(find_firsts(splt))
                if 'epsilon' not in first[lhs]:
                    first[lhs].add('epsilon')
                    change = True
            else:
                for i in range(len(splt)):
                    if (i == 0) or (all_epsilon(splt[0:i])):
                        if not (first[splt[i]] - {'epsilon'}).issubset(first[lhs]):
                            first[lhs].update(first[splt[i]] - {'epsilon'})
                            change = True

#END FIRST

#FOLLOW

follow = dict()
for key in first:
    follow[key] = set([])

def find_follow(A,B,beta):
    # A -> alpha B
    flag = False
    if len(beta) == 0:
        if not follow[A].issubset(follow[B]):
            follow[B].update(follow[A])
            return True

    # A -> alpha B beta
    for i in range(len(beta)):
        bb = beta[i]
#         print(follow[B])
#         print(first[bb] - {'epsilon'})
        if not (first[bb] - {'epsilon'}).issubset(follow[B]):
            follow[B].update(first[bb] - {'epsilon'})
            flag = True

        if i == len(beta)-1:
            if 'epsilon' in first[bb]:
                if not follow[A].issubset(follow[B]):
                    follow[B].update(follow[A])
                    flag = True

        if not 'epsilon' in first[bb]:
            break

    return flag

follow[non_terminals[0]].add('$')
change = True

while change:
    change = False

    for rule in rules:
        lhs = rule[0]
    #     rhs = rule[1]

        for rule1 in rules:
            A = rule1[0]
            for t in rule1[1]:
                splt = t.split(' ')
                if lhs in splt:
                    for i in range(len(splt)):
                        if splt[i] != lhs:
                            continue

                        change |= find_follow(A,lhs,splt[i+1:])
#END FOLLOW

#PRINT OUTPUT
output = ''
for non_terminal in non_terminals:
    output += non_terminal + ' : '

    first_values = first[non_terminal]
    follow_values = follow[non_terminal]

    for frst in first_values:
        output += frst + ' '

    output += ': '
    for fllw in follow_values:
        output += fllw + ' '

    output = output[:len(output)-1] + '\n'

output = output[:len(output)-1]

result = open("task_5_1_result.txt", "w")
result.write(output)
result.close()










































#

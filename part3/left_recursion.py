import argparse

def is_left_rec(rule):
    alphas = []
    betas = []
    for word in rule[1]:
        first = word.split(' ')[0]
        if first == rule[0]:
            return True
    return False

def elim_left_rec(rule):
#     print(rule)
    alphas = []
    betas = []
    for word in rule[1]:
        word_split = word.split(' ')
        if(word_split[0] == rule[0]):
            s = ""
            for i in range(1,len(word_split)):
                s += word_split[i] + ' '
            s.strip()
            alphas.append(s)
        else:
            betas.append(word.strip())

    lhs_1 = rule[0].strip()
    lhs_2 = rule[0].strip() + '\''
    if len(betas) == 0:
        rhs_1 = [lhs_2]
    else:
        rhs_1 = [beta.strip() + ' ' + lhs_2 for beta in betas]
    rhs_2 = [alpha.strip() + ' ' + lhs_2 for alpha in alphas]
    rhs_2.append('epsilon')
    rules = []
    rules.append([lhs_1, rhs_1])
    rules.append([lhs_2, rhs_2])
#     print(rules)
    return rules

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


t  = open(args.file, "r")

text = t.read()

rules = []
#[['S', [A a,b]], ['A', [S c, b d]]]

#SPLIT INPUT
spl = text.split('\n')
for r in spl:
    #split by :
    rule = r.split(':')
    # print(rule[1])
    rhs = rule[1].split('|')
    rhs = [s.strip() for s in rhs]
    rules.append([rule[0].strip(), rhs])


for i in range(len(rules)):
    for j in range(i):
        rhs_i = rules[i][1]
        flag = False
        to_append = []
        for r in rules[i][1]:
            word_split = r.split(' ', 1)
            if word_split[0] == rules[j][0]:
                flag = True
                if len(word_split) >= 2:
                    to_append.append(word_split[1])
                else:
                    to_append.append('')

        if flag == True:
            tmp = []
            for r in to_append:
                tmp1 = [s + ' ' + r for s in rules[j][1]]
                tmp = tmp + tmp1

            tmp2 = []
            for r in rules[i][1]:
                word_split = r.split(' ', 1)
                if word_split[0] != rules[j][0]:
                    tmp2.append(r.strip())
            rules[i][1] = tmp2 + tmp
    if is_left_rec(rules[i]):
        elim = elim_left_rec(rules[i])
        rules[i][1] = elim[0][1]
        rules.append(elim[1])

out = ''
for r in rules:
    out += r[0] + ' : '
    for sub_r in r[1]:
        out += sub_r + ' | '

    out = out[:len(out)-2]
    out += '\n'

output = out[:len(out)-1]
result = open("task_4_1_result.txt", "w")
result.write(output)
result.close()






































#

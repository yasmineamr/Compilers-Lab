from itertools import zip_longest
import argparse

def get_prefixes(rules):
    pref = []
    for r in rules:
        pref.append(r.split(' ')[0])

    return list(set(pref))

def find_left_factors(rule):
    result_prefixes = get_prefixes(rule)
    prefix_suffix = dict()
    pre_suf = []
    for r in rule:
        tmp = []
        for prefix in sorted(result_prefixes, key=lambda x: len(x), reverse=True):
            if r.startswith(prefix):
                if prefix in prefix_suffix:
                    prefix_suffix[prefix].append(r.replace(prefix, '', 1).strip())
#                     prefix_suffix[prefix] = list(dict.fromkeys(prefix_suffix[prefix]))
                else:
                    prefix_suffix[prefix] = list([r.replace(prefix, '', 1).strip()])
    l = list(prefix_suffix.items())
    return [t for t in l if len(t[1]) > 1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


t  = open(args.file, "r")

text = t.read().strip()

rules = []
#[['S', [A a,b]], ['A', [S c, b d]]]

#SPLIT INPUT
spl = text.split('\n')
for r in spl:
    #split by :
    rule = r.split(':')
    rhs = rule[1].split('|')
    rhs = [s.strip() for s in rhs]
    rules.append([rule[0].strip(), rhs])
# rules

#GENERAL ALGORITHM
i = 0
while i < len(rules):
    lhs_rule = rules[i][0]
    while(True):
        rules[i][1] = list(dict.fromkeys(rules[i][1]))
        rhs_rule = rules[i][1]
        to_factor = find_left_factors(rhs_rule)
        if(len(to_factor) == 0):
            break
        prev = lhs_rule + '\''
        for t in to_factor:
            pref = t[0]
            suff = t[1]

            for j, s in enumerate(suff):
                if len(s) > 0:
                    rhs_rule.remove(pref + ' ' + s)
                else:
                    rhs_rule.remove(pref)
                    suff[j] = 'epsilon'
            rhs_rule.append(pref + ' ' + prev)
            new_rule = [prev, suff]
            rules[i][1] = rhs_rule
            rules.append(new_rule)
            prev = prev + '\''
    i+=1

#PRINT OUTPUT
out = ''
for r in rules:
    out += r[0] + ' : '
    for sub_r in r[1]:
        out += sub_r + ' | '

    out = out[:len(out)-2]
    out += '\n'

output = out[:len(out)-1]
result = open("task_4_2_result.txt", "w")
result.write(output)
result.close()


# REFERENCES:
# prefix_suffix: https://stackoverflow.com/questions/21217410/left-factoring-using-python























    #

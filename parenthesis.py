def solve(string):
    new = []
    for char in string:
        new.append(char)
    for pindex in range(1, len(new)):
        if new[pindex] == '(':
            if new[pindex-1] == '-':
                for k in range(pindex+1, len(new)):
                    temp = ''.join(new)
                    if new[k].isalpha():
                        new[pindex - 1] = ''
                        if new[k-1] == '-':
                            new[k-1] = '+'
                        else:
                            new.insert(k, '-')
                            new[pindex-1] = ''
                            new[k-2] = ''
                            #new[k] = '-' + new[k]
            elif new[pindex-1] == '+':
                new[pindex-1] = ''
            new[pindex] = ''
    nude = list(''.join(list(filter(lambda c: c != '(' and c != ')', new))))
    for c in nude:
        if c == '+':
            nude[nude.index(c)] = ''
        else:
            break

    return ''.join(nude)
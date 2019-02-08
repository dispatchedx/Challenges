import itertools

def permutations(string):
    print(list(''.join(p) for p in set(itertools.permutations(string))))
permutations('aabb')
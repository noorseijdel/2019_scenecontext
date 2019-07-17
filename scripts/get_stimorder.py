import itertools
stuff = (1, 2, 3)
p=0
for permutation in itertools.permutations(stuff,3):
    print(permutation)
    p += 1

print p

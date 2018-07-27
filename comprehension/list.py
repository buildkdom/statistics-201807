elements = [x * 2 for x in range(11)]
print(elements)

vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)

print([(x / amount)+1 for x in vals])
from math import sqrt
non_squars = [x for x in range(101) if sqrt(x)**2 != x]
print (non_squars)

print(int(sqrt(14)))
print(int(sqrt(14))**2)

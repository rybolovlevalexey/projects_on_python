import math
sp1 = list(i for i in range(51, 101))
sp2 = list(i for i in range(1, 51))
res = 1
for elem in sp1:
    res *= elem
for elem in sp2:
    res /= elem
print(res)
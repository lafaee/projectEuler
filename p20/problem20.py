# Factorial digit sum

import math

a = math.factorial(100)
b = str(a)

s = 0

for i in range(len(b)):
    s = s + int(b[i])

print(s)

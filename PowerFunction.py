'''
Implement pow(A, B) % C. In other words, given A, B and C, Find (AB % C).
Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

Input 1:
A = 2
B = 3
C = 3

Input 2:
A = 3
B = 3
C = 1

Output 1:
2

Output 2:
0
'''
def powmod(a, exp, m):
    if exp==0:
        return (1)

    p = powmod(a, exp//2, m)

    if (exp%2==0):
        return (p*p) % m
    else:
        return (p*p*a) % m

a, exp, m = [int(x) for x in input().split()]
print(powmod(a, exp, m))


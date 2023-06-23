# Given a rope of length n, you need to find maximum number of pieces you can make such
# that length of every piece is in set {a,b,c} for given values of a,b,c

def max_cuts(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = max(max_cuts(n-a, a, b, c), max_cuts(n -
              b, a, b, c), max_cuts(n-c, a, b, c))
    if res == -1:
        return -1
    return res + 1


print(max_cuts(5, 2, 5, 1))
print(max_cuts(23, 12, 9, 11))
print(max_cuts(5, 4, 2, 6))

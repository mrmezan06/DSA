# write function to calculate factorial of a number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))

# write function to calculate factorial of a number using tail recursion


def factorial_tr(n, k=1):
    if n == 0:
        return k
    return factorial_tr(n-1, k*n)


print(factorial_tr(5))

# 1 Write a recursive function to print number from n to 1.

def print_number(n):
    if n == 0:
        print()
        return
    print(n, end=" ")
    print_number(n-1)


print_number(5)

# 2 Write a recursive function to print number from 1 to n.


def print_series(n):
    if n == 0:
        return
    print_series(n-1)
    print(n, end=" ")


print_series(5)
print()

# 3 Make the No. 2 program more efficient.


def print_series_tr(n, i=1):
    if n == 0:
        return
    print(i, end=" ")
    print_series_tr(n-1, i+1)


print_series_tr(5)
print()
# tr means tail recursion

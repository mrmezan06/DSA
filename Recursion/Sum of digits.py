# Write a recursive function to find sum of digits of a number.

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)


result = sum_of_digits(12345)
print(result)

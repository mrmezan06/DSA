# Write a recursive function to check if a string is palindrome or not.

def check_palindrome(s, i=0):
    if i == len(s)//2:
        return True
    if s[i] != s[len(s)-1-i]:
        return False
    return check_palindrome(s, i+1)


print(check_palindrome("ABCBA"))
print(check_palindrome("ABCDA"))

# Solution 2


def palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome(s, start+1, end-1)

# Solution 3 Non-recursive way


def isPalindrome(s):
    return s == s[::-1]


print(palindrome("ABCBA", 0, 4))
print(check_palindrome("ABCDA"))

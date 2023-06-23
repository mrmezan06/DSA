# Given n people in a circle, every kth person is killed.
# Find the last survivor.

def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n-1, k) + k - 1) % n + 1


print(josephus(7, 3))
print(josephus(8, 2))

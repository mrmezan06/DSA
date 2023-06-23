# Given a string, print of all subset of it.(in any order)

def find_subset(s, curr=" ", i=0):
    if i == len(s):
        print(curr, end=" ")
        return
    find_subset(s, curr, i+1)
    find_subset(s, curr+s[i], i+1)


print(find_subset("ABC"))

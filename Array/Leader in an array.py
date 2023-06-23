# Leader in an array
# Sample input: 5, 3, 20, 15, 8, 3
# Sample output: 20, 15, 8, 3

def leaderInArray(a):
    n = len(a)
    res = []
    leader = a[n - 1]
    res.append(leader)
    for i in range(n - 2, -1, -1):
        if a[i] > leader:
            leader = a[i]
            res.append(leader)
            # range(start, stop, step)
    for i in range(len(res) - 1, -1, -1):
        print(res[i], end=" ")
    print()


leaderInArray([5, 3, 20, 15, 8, 3])

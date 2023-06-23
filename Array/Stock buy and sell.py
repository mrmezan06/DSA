# Stock buy and sell
# Sample Input: 1, 5, 3, 8, 12
# Sample Output: 13
# Sample Input: 10, 5, 3
# Sample Output: 0
# Sample Input: 1, 2, 5
# Sample Output: 4

def stock_buy_and_sell(a):
    n = len(a)
    profit = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            profit += a[i] - a[i - 1]
    return profit


print(stock_buy_and_sell([1, 5, 3, 8, 12]))
print(stock_buy_and_sell([10, 5, 3]))
print(stock_buy_and_sell([1, 2, 5]))

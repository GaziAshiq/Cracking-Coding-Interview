def max_profit(prices):
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        else:
            profit = max(profit, prices[i] - buy)
    return profit


print(max_profit(prices=[7, 1, 5, 3, 6, 4]))

# Knapsack problem/0-1
def knapsack(items, max_weight):
    dp = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(1, max_weight + 1):
            item_weight = items[i - 1]["weight"]
            item_value = items[i - 1]["value"]
            if item_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[len(items)][max_weight]
items = [
    {"name": "item1", "weight": 2, "value": 3},
    {"name": "item2", "weight": 3, "value": 4},
    {"name": "item3", "weight": 4, "value": 5},
    {"name": "item4", "weight": 5, "value": 6}
]
max_weight = 5
print(knapsack(items, max_weight))
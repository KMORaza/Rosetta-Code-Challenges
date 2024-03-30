# Knapsack problem/Unbounded
def max_value_knapsack(items, max_weight, max_volume):
    dp = [[0] * (max_volume + 1) for _ in range(max_weight + 1)]
    for i in range(len(items)):
        for w in range(items[i]['weight'], max_weight + 1):
            for v in range(items[i]['volume'], max_volume + 1):
                dp[w][v] = max(dp[w][v], dp[w - items[i]['weight']][v - items[i]['volume']] + items[i]['value'])
    return dp[max_weight][max_volume]
items = [
    {'name': 'item1', 'value': 10, 'weight': 2, 'volume': 3},
    {'name': 'item2', 'value': 20, 'weight': 3, 'volume': 4},
    {'name': 'item3', 'value': 30, 'weight': 4, 'volume': 5}
]
max_weight = 5
max_volume = 7
print(max_value_knapsack(items, max_weight, max_volume))
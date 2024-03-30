# Knapsack problem/Bounded
def knapsack_bounded(items, max_weight):
    table = [0] * (max_weight + 1)
    for item in items:
        for count in range(1, item['pieces'] + 1):
            for weight in range(max_weight, item['weight'] - 1, -1):
                table[weight] = max(table[weight], table[weight - item['weight']] + item['value'])
    return table[max_weight]
items = [
    {'name': 'item1', 'pieces': 2, 'weight': 3, 'value': 6},
    {'name': 'item2', 'pieces': 1, 'weight': 2, 'value': 4},
    {'name': 'item3', 'pieces': 3, 'weight': 5, 'value': 10}
]
max_weight = 8
print(knapsack_bounded(items, max_weight))
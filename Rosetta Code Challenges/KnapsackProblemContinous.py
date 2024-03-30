# Knapsack problem/Continuous
def knapsack_max_value(items, max_weight):
    items.sort(key=lambda x: x['value'] / x['weight'], reverse=True)
    total_value = 0
    total_weight = 0
    for item in items:
        if total_weight + item['weight'] <= max_weight:
            total_value += item['value']
            total_weight += item['weight']
        else:
            remaining_weight = max_weight - total_weight
            fraction = remaining_weight / item['weight']
            total_value += fraction * item['value']
            total_weight += fraction * item['weight']
            break
    return total_value, total_weight
items = [
    {'name': 'Steak', 'weight': 5, 'value': 100},
    {'name': 'Chicken', 'weight': 3, 'value': 50},
    {'name': 'Pork', 'weight': 2, 'value': 30},
    {'name': 'Bacon', 'weight': 1, 'value': 20}
]
max_weight = 7
max_value, total_weight = knapsack_max_value(items, max_weight)
print("Maximum value =", max_value)
print("Total weight of selected items =", total_weight)
# Deepcopy
def deep_copy(obj):
    if isinstance(obj, dict):
        copied_dict = {}
        for key, value in obj.items():
            copied_dict[key] = deep_copy(value)
        return copied_dict
    elif isinstance(obj, list):
        copied_list = []
        for item in obj:
            copied_list.append(deep_copy(item))
        return copied_list
    elif isinstance(obj, tuple):
        copied_tuple = tuple(deep_copy(item) for item in obj)
        return copied_tuple
    else:
        return obj
original = {
    'a': 1,
    'b': [2, 3, 4],
    'c': {'d': 5, 'e': [6, 7]}
}
copied = deep_copy(original)
print("Original:", original)
print("Deep copy:", copied)
copied['a'] = 100
copied['b'].append(999)
copied['c']['e'].append(888)
print("\nModified deep copy:")
print("Original:", original)
print("Deep copy:", copied)
# Hash from two arrays
def arr_to_obj(keys, values):
    if len(keys) != len(values):
        raise ValueError("Arrays must be of equal length")
    hash_obj = {keys[i]: values[i] for i in range(len(keys))}
    return hash_obj
first_arr = [1, 2, 3]
second_arr = ["a", "b", "c"]
hash_obj = arr_to_obj(first_arr, second_arr)
print(hash_obj)
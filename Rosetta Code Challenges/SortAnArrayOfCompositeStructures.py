# Sort an array of composite structures
def sort_array_by_key(objects):
    sorted_array = sorted(objects, key=lambda obj: obj.key)
    return sorted_array
class Object:
    def __init__(self, key):
        self.key = key
objects = [
    Object(5),
    Object(2),
    Object(7),
    Object(1)
]
sorted_objects = sort_array_by_key(objects)
for obj in sorted_objects:
    print(obj.key)
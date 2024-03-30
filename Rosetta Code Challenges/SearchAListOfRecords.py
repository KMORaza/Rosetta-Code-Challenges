# Search a list of records
def find_record_index(records, attribute_name, attribute_value):
    for index, record in enumerate(records):
        if attribute_name in record and record[attribute_name] == attribute_value:
            return index
    return -1
records = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 35}
]
attribute_name = "name"
attribute_value1 = "Alice"
attribute_value2 = "Rocky"
print(find_record_index(records, attribute_name, attribute_value1))
print(find_record_index(records, attribute_name, attribute_value2)) 
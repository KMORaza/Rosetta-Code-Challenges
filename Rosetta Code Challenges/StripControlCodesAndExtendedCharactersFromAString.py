# Strip control codes and extended characters from a string
import re
def strip_control_and_extended_characters(input_string):
    pattern = r'[\x00-\x1F\x7F]|[^ -~]'
    stripped_string = re.sub(pattern, '', input_string)
    return stripped_string
input_string = "Hello\x1B\x1F\x7F World! ±"
stripped_string = strip_control_and_extended_characters(input_string)
print("Original String:", input_string)
print("Stripped String:", stripped_string)
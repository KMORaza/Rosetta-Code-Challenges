# Word wrap
def wrap_text(text, width):
    lines = []
    for line in text.splitlines():
        while len(line) > width:
            space_index = line.rfind(' ', 0, width)
            if space_index == -1:
                space_index = width
            lines.append(line[:space_index].strip())
            line = line[space_index:].lstrip()
        lines.append(line.strip())
    return '\n'.join(lines)
text = "Wrap text using a more sophisticated algorithm such as the Knuth and Plass TeX algorithm. If your language provides this, you get easy extra credit, but you must reference documentation indicating that the algorithm is something better than a simple minimum length algorithm."
wrapped_text = wrap_text(text, 80)
print(wrapped_text)
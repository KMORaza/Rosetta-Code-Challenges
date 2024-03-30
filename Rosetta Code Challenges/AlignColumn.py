# Align Columns
def align_columns(text, alignment):
    column_widths = [0] * max(len(line.split('$')) for line in text)
    for line in text:
        words = line.split('$')
        for i, word in enumerate(words):
            column_widths[i] = max(column_widths[i], len(word))
    aligned_lines = []
    for line in text:
        words = line.split('$')
        aligned_words = []
        for i, word in enumerate(words):
            width_diff = column_widths[i] - len(word)
            if alignment == 'right':
                aligned_word = ' ' * width_diff + word
            elif alignment == 'center':
                left_spaces = ' ' * (width_diff // 2)
                right_spaces = ' ' * (width_diff - width_diff // 2)
                aligned_word = left_spaces + word + right_spaces
            else:
                aligned_word = word + ' ' * width_diff
            aligned_words.append(aligned_word)
        aligned_lines.append(' '.join(aligned_words))
    return '\n'.join(aligned_lines)
test_text = [
    'Given$a$text$file$of$many$lines',
    'where$fields$within$a$line$',
    'are$delineated$by$a$single$"dollar"$character',
    'write$a$program',
    'that$aligns$each$column$of$fields',
    'by$ensuring$that$words$in$each$',
    'column$are$separated$by$at$least$one$space.',
    'Further,$allow$for$each$word$in$a$column$to$be$either$left$',
    'justified,$right$justified',
    'or$center$justified$within$its$column.'
]
aligned_text = align_columns(test_text, 'right')
print(aligned_text)
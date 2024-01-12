
def find_characters_around_substring(s, substring, n, direction='after'):
    index = s.find(substring)

    if index == -1:
        return "Substring not found in the given string."

    if direction == 'before':
        start_index = max(0, index - n)
        result = s[start_index:index]
    elif direction == 'after':
        end_index = min(len(s), index + len(substring) + n)
        result = s[index + len(substring):end_index]
    else:
        return "Invalid direction. Choose 'before' or 'after'."

    return result
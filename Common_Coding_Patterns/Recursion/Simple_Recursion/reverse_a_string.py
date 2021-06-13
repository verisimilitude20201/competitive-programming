def reverse_a_string(string):
    reversed_str_chars = []
    reverse_string_recursive(string, reversed_str_chars, len(string) - 1)
    return "".join(reversed_str_chars)


def reverse_string_recursive(string, reversed_str_chars, index):
    if index < 0:
        return
    reversed_str_chars.append(string[index])
    reverse_string_recursive(string, reversed_str_chars, index - 1)


print(reverse_a_string("Abhijit"))
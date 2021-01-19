"""
Problem:
-------
Write a method to replace all space characters in a string with %20. Assume that string has sufficient space at the end to hold any
additional characters. 

Complexity:
---------

replace_spaces_with_percent_201 --> 
    Time: O(N)
    Space: O(N)

replace_spaces_with_percent_202 --> 
    Time: O(N)
    Space: O(N + 2*s) -> Where s is the space count in between words. 


"""


def replace_spaces_with_percent_201(string, length_of_string):
    characters = []
    for i in range(1, len(string)):
        current_character = string[i - 1]
        next_character = string[i]
        if current_character == next_character == " ":
            continue
        characters.append("%20" if current_character == " " else current_character)

    return "".join(characters)


def replace_spaces_with_percent_202(string, true_length_of_string):
    space_count = 0
    for character in string:
        if character == " ":
            space_count += 1

    for i in reversed(range(len(string))):
        if string[i] != " ":
            break
        space_count -= 1

    index = true_length_of_string + space_count * 2
    characters = [None] * index

    for i in reversed(range(true_length_of_string)):
        character = string[i]
        if character == " ":
            characters[index - 1] = "0"
            characters[index - 2] = "2"
            characters[index - 3] = "%"
            index -= 3
        else:
            characters[index - 1] = character
            index -= 1

    return "".join(characters)



print(replace_spaces_with_percent_201("Mr John Smith   ", 13))
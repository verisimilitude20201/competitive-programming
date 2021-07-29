"""
Explanation:
-----------
Input
-----
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
M r   J o h n   S m i  t  h  

Output
------
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
M r % 2 0 J o h n %  2  0 S  m  i  t  h 

Complexity:
----------
Time: O(true_length)
Space: O(true_length + 2 * space_count)


"""
def urlify(string, true_length):
    space_count = 0
    for i in range(true_length):
        if string[i] == " ":
            space_count += 1

    index = true_length + 2 * space_count
    char_array = [None] * index
    for j in range(true_length - 1, -1, -1):
        if string[j] == " ":
            char_array[index - 1] = "0"
            char_array[index - 2] = "2"
            char_array[index - 3] = "%"
            index -= 3
        else:
            char_array[index - 1] = string[j]
            index -= 1

    return "".join(char for char in char_array if char is not None)


print(urlify("Mr John Smith   ", 13))
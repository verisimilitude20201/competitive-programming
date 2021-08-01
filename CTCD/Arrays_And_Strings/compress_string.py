"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
def compress_string(string):
    i = 0
    j = 1

    compressed_array = []
    while j < len(string):
        counter = 1
        while j < len(string) and string[i] == string[j]:

            counter += 1
            j += 1

        compressed_array.append(str(counter) + "" + string[i])
        i = j
        j += 1
    compressed_string = "".join(char for char in compressed_array)
    if len(compressed_string) < len(string):
        return compressed_string
    return string


print(compress_string("aabcccccaaa"))
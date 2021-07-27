"""
Complexity:
----------
Time: O(N log N)
Space: O(N)

"""
def is_string_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = "".join(sorted(list(string1)))
    string2 = "".join(sorted(list(string2)))

    return string1 == string2


print(is_string_permutation("ABA", "AAB"))
print(is_string_permutation("ABA", "ABC"))

"""
Complexity:
----------
Time: O(min(len(string1), len(string2)))
Space: O(1)
"""
def is_one_or_zero_edit_away(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    if abs(l1 - l2) > 1:
        return False

    found_difference = False
    s1 = string1 if l1 < l2 else string2
    s2 = string2 if l1 < l2 else string1
    index1 = 0
    index2 = 0
    while index1 < l1 and index2 < l2:
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True
            if l1 == l2:
                index1 += 1
        else:
            index1 += 1
        index2 += 1

    return True


print(is_one_or_zero_edit_away("pale", "ple"))
print(is_one_or_zero_edit_away("pales", "pale"))
"""
Complexity:
----------
Space: O(N)
Time: O(2N + 3N) ~ O(N) 
"""
def is_string_rotation(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 == 0 or len2 == 0 or len1 != len2:
        return False
    s = s1 + s1
    return s.find(s2) != -1


def main():
    print(is_string_rotation("waterbottle", "erbottlewat"))



main()
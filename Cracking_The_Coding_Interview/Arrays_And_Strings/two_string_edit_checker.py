"""
Problem:
-------
Check if two strings are zero or one edits away from each other.

For example:
    pales pale --> True, one 's' absent
    pale bale  --> True, 'b' needs to be replaced with 'p'

Complexity:
---------
Time: O(max(S1, S2))
Space: O(1)

"""

class TwoStringEditChecker:

    def __init__(self, string1, string2):
        self._string1 = string1
        self._string2 = string2

    def are_strings_zero_or_one_edits_away(self):
        absolute_difference_in_length = abs(len(self._string1) - len(self._string2))
        if absolute_difference_in_length == 0:
            return self._is_zero_or_one_edit_away()
        elif absolute_difference_in_length == 1:
            return self._is_zero_or_one_insert_away()

        return False

    def _is_zero_or_one_edit_away(self):
        is_zero_or_one_edit_away = False
        for i in range(len(self._string1)):
            char_i = self._string1[i]
            if self._string2[i] != char_i:
                if is_zero_or_one_edit_away:
                    return False
                is_zero_or_one_edit_away = True

        return True

    def _is_zero_or_one_insert_away(self):
        index1 = 0
        index2 = 0
        while index1 < len(self._string1) and index2 < len(self._string2):
            if self._string1[index1] != self._string2[index2]:
                if index1 != index2:
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1

        return True


tsec = TwoStringEditChecker("pale", "bale")
print(tsec.are_strings_zero_or_one_edits_away())

tsec1 = TwoStringEditChecker("pales", "pale")
print(tsec1.are_strings_zero_or_one_edits_away())


tsec2 = TwoStringEditChecker("pale", "bake")
print(tsec2.are_strings_zero_or_one_edits_away())
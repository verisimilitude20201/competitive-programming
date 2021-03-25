"""
Problem
-------
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example:
------
Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Approach:
--------
Check for overlapping intervals after sorting. If at least one overlapping interval is found, return False.

a.     A1   A2
         B1   B2    ===> B1 >= A1 and B1 <= A2 ===> B overlaps with A


b.     A1      A2
         B1 B2    ===> B1 >= A1 and B1 <= A2 ==>  B overlaps with A


c.      A1  A2      
                  =====> A1 >= B1 and A1 <= B2 ===> A overlaps with B
     B1   B2

d.   A1A2      =====> A1 >= B1 and A1 <= B2   ===>  A overlaps with B      
    B1   B2 



Complexity
---------
Time: O(N log N)
Space: O(1)

"""
def can_attend_all_appointments(intervals):
    if len(intervals) == 1:
        return True
    if len(intervals) == 0:
        return False

    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])
    interval_a = intervals[0]
    for i in range(1, len(intervals)):
        interval_b = intervals[i]
        b_overlaps_a = interval_a[start] < interval_b[start] < interval_a[end]
        a_overlaps_b = interval_b[start] < interval_a[start] < interval_b[end]
        if b_overlaps_a or a_overlaps_b:
            return False
        interval_a = intervals[i]
    return True


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()


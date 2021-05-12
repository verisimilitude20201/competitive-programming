"""
Problem
-------
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example:
-------
N = 1
-----
 (

 ()

N = 2
-----
    (

((      ()

(()        ()(

(())       ()()

Approach
-------
0) result = [], queue = [], ParenthesisString(str="", openCount=0, closeCount=0), num=2


1) result = [], queue = [ParenthesisString(str="", openCount=0, closeCount=0), ], ParenthesisString(str="", openCount=0, closeCount=0), num=2


2) while queue has entries

     i) ps = ParenthesisString(str="", openCount=0, closeCount=0), queue = []
        ps.openCount < num i.e 0 < 2
        queue = [ParenthesisString(str="(", openCount=1, closeCount=0)]
        ps.openCount > ps.closeCount i.e 1 > 0
        queue = [ParenthesisString(str="(", openCount=1, closeCount=0), ParenthesisString(str="()", openCount=1, closeCount=1)]

     ii) ps = ParenthesisString(str="(", openCount=1, closeCount=0), queue = [ParenthesisString(str="()", openCount=1, closeCount=1)]
         ps.openCount < num i.e 1 < 2
         queue = [ParenthesisString(str="()", openCount=1, closeCount=1), ParenthesisString(str="((", openCount=2, closeCount=0)]
         ps.openCount > ps.closeCount i.e 1 > 0
         queue = [ParenthesisString(str="()", openCount=1, closeCount=1), ParenthesisString(str="((", openCount=2, closeCount=0), ParenthesisString(str="()", openCount=1, closeCount=1)]


     iii) ps = ParenthesisString(str="()", openCount=1, closeCount=1), queue = [ParenthesisString(str="((", openCount=2, closeCount=0), ParenthesisString(str="()", openCount=1, closeCount=1)]
         ps.openCount < num i.e 1 < 2
         queue = [ParenthesisString(str="((", openCount=2, closeCount=0), ParenthesisString(str="()", openCount=1, closeCount=1), ParenthesisString(str="()(", openCount=2, closeCount=1)]
         ps.openCount > ps.closeCount i.e 1 > 1
         # Don't add a closing brace

      iv) ps = ParenthesisString(str="((", openCount=2, closeCount=0), queue = [ParenthesisString(str="()", openCount=1, closeCount=1)]
         ps.openCount < num i.e 1 < 2, don't add any further (
         queue = [ParenthesisString(str="()", openCount=1, closeCount=1)]
         ps.openCount > ps.closeCount i.e 2 > 0
         queue = [ParenthesisString(str="()", openCount=1, closeCount=1), ParenthesisString(str="(()", openCount=2, closeCount=1)]


      v) ps = ParenthesisString(str="()", openCount=1, closeCount=1), queue = [ParenthesisString(str="(()", openCount=2, closeCount=1)]
         ps.openCount < num i.e 1 < 2
         queue = [ParenthesisString(str="(()", openCount=2, closeCount=1), ParenthesisString(str="()(", openCount=2, closeCount=1)]
         ps.openCount > ps.closeCount i.e 1 > 1, don't add a closing brace


       vi) ps = ParenthesisString(str="(()", openCount=2, closeCount=1), queue = [ParenthesisString(str="()(", openCount=2, closeCount=1)]
           ps.openCount < num i.e 2 < 2, don't add an opening parenthesis now
           ps.openCount > ps.closeCount so 2 > 1
           queue = [ParenthesisString(str="()(", openCount=2, closeCount=1), ParenthesisString(str="(())", openCount=2, closeCount=2)]

       vii) ps = ParenthesisString(str="()(", openCount=2, closeCount=1), queue = [ParenthesisString(str="(())", openCount=2, closeCount=2)]
            ps.openCount < num i.e 2 < 2, don't add an opening parenthesis now
            ps.openCount > ps.closeCount so 2 > 1
            queue = [ParenthesisString(str="(())", openCount=2, closeCount=2), ParenthesisString(str="()()", openCount=2, closeCount=2)]


       viii. result = ["(())", "()()"]

Complexity:
----------
Space: O(N * 2^N). We contenate parenthesis N times. And we get about 2^N combinations of parenthesis. Of them, the ordered ones are < 2^N, but we can consider the worst-case complexity 
here
Time: O(N * 2^N). Without caring for the ordering ( a closing ')' can come after every '(' ) there can be 2^N combinations. Ordered ones < 2^N. This forms the nodes of a binary 
tree. We have 2^N leaf nodes and 2^N - 1 intermediate nodes. Furthermore, we also do the concatenation so asymptotic complexity is O(N * 2^N). Not completely accurate but is okay
The actual complexity is O(4^N/sqrt(N)) which is bounded by a Catalan number.  

"""


from collections import deque


class ParenthesisString:
    def __init__(self, string, open_count, close_count):
        self.string = string
        self.open_count = open_count
        self.close_count = close_count


def generate_valid_parenthesis(num):
    result = []
    queue = deque()
    ps = ParenthesisString("", 0, 0)
    queue.append(ps)
    while queue:
        ps = queue.popleft()
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.string)
        if ps.open_count < num:
            queue.append(ParenthesisString(ps.string + "(", ps.open_count + 1, ps.close_count))
        if ps.open_count > ps.close_count:
            queue.append(ParenthesisString(ps.string + ")", ps.open_count, ps.close_count + 1))
    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parenthesis(2)))

    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parenthesis(3)))


main()

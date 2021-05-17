"""
Problem
-------
Given an expression containing digits and operations (+, -, *), 
Find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses

Example:
-------
Input: "1+2*3"
Output: 7, 9
Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

Approach
--------
0) 1 + 2 * 3

(1 + 2) * 3 = 9



I) Frame-I


1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = diff_ways_to_evaluate_expression("1")
        rightPart = diff_ways_to_evaluate_expression("2 * 3")




2) diff_ways_to_evaluate_expression(), input = "1"
--------------------------------------------------
   result = []
   result = [1]



II)  

1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = [1]
        rightPart = diff_ways_to_evaluate_expression("2 * 3")



2) diff_ways_to_evaluate_expression(), input = "2 * 3"
------------------------------------------------------
      result = []

     i) i = 0, i < 3
        char = 2

     ii) i = 1, i < 3
         char = "*"
         leftPart = diff_ways_to_evaluate_expression("2")
         rightPart = diff_ways_to_evaluate_expression("3")


3)  diff_ways_to_evaluate_expression(), input = "2"
---------------------------------------------------
    result = [2]

4) diff_ways_to_evaluate_expression(), input = "3"
    result = [3]

III) 

1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = [1]
        rightPart = diff_ways_to_evaluate_expression("2 * 3")



2) diff_ways_to_evaluate_expression(), input = "2 * 3"
------------------------------------------------------
      result = []

     i) i = 0, i < 3
        char = 2

     ii) i = 1, i < 3
         char = "*"
         leftPart = [2]
         rightPart = [3]
         result = [6]

     iii) i = 2
          char = 3

IV) 

1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = [1]
        rightPart = [6]
        result = [7]
    iii) i = 2, char = 2
    iv) i = 3, char = *
        leftPart = diff_ways_to_evaluate_expression("1 + 2")
        rightParts = diff_ways_to_evaluate_expression("3")

2) diff_ways_to_evaluate_expression(), input = "1 + 2"
------------------------------------------------------
    result = []
    i) i = 0, i < 3, char = 1
    ii) i = 1, i < 3, char = +
        leftPart =  diff_ways_to_evaluate_expression("1")
        rightPart = diff_ways_to_evaluate_expression("2")


3) diff_ways_to_evaluate_expression(), input = "1"
------------------------------------------------------
   result = [1]

4) diff_ways_to_evaluate_expression(), input = "2"
--------------------------------------------------
    result = [2]

V) 

1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = [1]
        rightPart = [6]
        result = [7]
    iii) i = 2, char = 2
    iv) i = 3, char = *
        leftPart = diff_ways_to_evaluate_expression("1 + 2")
        rightParts = diff_ways_to_evaluate_expression("3")

2) diff_ways_to_evaluate_expression(), input = "1 + 2"
------------------------------------------------------
    result = []
    i) i = 0, i < 3, char = 1
    ii) i = 1, i < 3, char = +
        leftPart =  [1]
        rightPart = [2]
        result = [3]
    iii) i = 2, char = 3

VI) 

1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = [1]
        rightPart = [6]
        result = [7]
    iii) i = 2, char = 2
    iv) i = 3, char = *
        leftPart = 3
        rightParts = diff_ways_to_evaluate_expression("3")

2) diff_ways_to_evaluate_expression(), input = "3"
--------------------------------------------------
result = [3]


VII)

1) diff_ways_to_evaluate_expression(), input = "1 + 2 * 3"
---------------------------------------------------------
    result = []
    i in 5
    
    i) i = 0, char = 1
    ii) i = 1, char = "+"
        leftPart = [1]
        rightPart = [6]
        result = [7]
    iii) i = 2, char = 2
    iv) i = 3, char = *
        leftPart = 3
        rightParts = 3
        result = [7, 9]
    v) i = 4, char = 3

result = [7, 9]

Complexity:
----------
Time: O(N * 2^N)
Space: O(2 ^ N)

Actual time and space complexity of this algorithm is given by a Catalan number -> O(4^N / sqrt(N))
"""


def diff_ways_to_evaluate_expression(input):
  result = []
  # base case: if the input string is a number, parse and add it to output.
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(0, len(input)):
      char = input[i]
      if not char.isdigit():
        # break the equation here into two parts and make recursively calls
        leftParts = diff_ways_to_evaluate_expression(input[0:i])
        rightParts = diff_ways_to_evaluate_expression(input[i+1:])
        for part1 in leftParts:
          for part2 in rightParts:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

main()
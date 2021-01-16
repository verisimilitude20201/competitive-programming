"""
Problem:
-------
Find all positive integers a, b, c and d such that a^3 + b^3 = c^3 + d^3 for n from 1 to 1000 

Complexity
---------
Space complexity: O(1) for all
Time:
   compute_equation() - O(N^4) Brute force
   compute_equation_cubic1(): O(N^3)
   compute_equation_quadratic(): O(N^2)

"""

import math


def compute_equation(n=1000):
    for a in range(n):
        cube_a = math.pow(a, 3)
        for b in range(n):
            cube_b = math.pow(b, 3)
            for c in range(n):
                cube_c = math.pow(c, 3)
                for d in range(n):
                    cube_d = math.pow(d, 3)
                    if cube_a + cube_b == cube_c + cube_d:
                        print(a, b, c, d)


def compute_equation_cubic1(n=1000):
    for a in range(n):
        cube_a = pow(a, 3)
        for b in range(n):
            cube_b = pow(b, 3)
            for c in range(n):
                cube_c = pow(c, 3)
                d = pow(cube_a + cube_b + cube_c, 1/3)
                if cube_a + cube_b == cube_c + d:
                    print(a, b, c, d)


def compute_equation_quadratic(n=1000):
    map = {}
    for a in range(n):
        cube_a = pow(a, 3)
        for b in range(n):
            cube_b = pow(b, 3)
            result = cube_b + cube_a
            map[result] = (a, b)

    for c in range(n):
        cube_c = pow(c, 3)
        for d in range(n):
            cube_d = pow(d, 3)
            pair = map.get(cube_c + cube_d)
            print(pair, c, d)

compute_equation_cubic2()




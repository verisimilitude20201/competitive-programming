
class Solution:
    def cleanRoom(self, robot):
        visited = set()
        # up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                new_d = (d + i) % 4
                new_x = cell[0] + directions[new_d][0]
                new_y = cell[1] + directions[new_d][1]
                new_cell = (new_x, new_y)
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    goback()
                
                robot.turnRight()

        backtrack()

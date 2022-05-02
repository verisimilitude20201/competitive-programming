class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []

        index_sum = defaultdict(list)
        diagonals = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                num = mat[i][j]
                index_sum[i + j].append(num)

        for i_sum, elements in index_sum.items():
            if i_sum % 2 == 0:
                [diagonals.append(x) for x in elements[::-1]]
            else:
                [diagonals.append(x) for x in elements]

        return diagonals
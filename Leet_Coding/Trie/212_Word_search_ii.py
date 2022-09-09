"""
Complexity:
----------
Time: O(M * (4 * 3 ^ (L - 1))) -->
    M is the number of cells of the board. 
    L is the maximum length of the word.
    4 * 3 ^ L - 1 -> 
        4 because we have 4 directions to explore. 
        3 ^ L - 1 comes from the fact that if we have 3 matching cells, we will traverse 
        branches ^ depth (3 ^ L - 1) 
Space: O(N)
"""
class Solution:
    WORD_DELIMITER = '$'

    def __init__(self):
        self._trie = {}

        self.matched_words = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.construct_trie(words)
        self.find_words(board, words)

        return self.matched_words

    def construct_trie(self, words: List[int]) -> None:
        for word in words:
            node = self._trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[Solution.WORD_DELIMITER] = word

    def find_words(self, board: List[List[str]], words: List[int]) -> None:
        row_num = len(board)
        col_num = len(board[0])
        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] in self._trie:
                    self._find_word_backtrack(board, i, j, self._trie)

    def _find_word_backtrack(self, board: List[List[str]], row, col, node):
        letter = board[row][col]
        current_node = node[letter]
        word_match = current_node.pop(Solution.WORD_DELIMITER, False)
        if word_match:
            self.matched_words.append(word_match)
        board[row][col] = "#"
        row_num = len(board)
        col_num = len(board[0])
        for (row_offset, col_offset) in [(1, 0), (-1, 0), (0, 1), [0, -1]]:
            new_row = row + row_offset
            new_col = col + col_offset
            if new_row < 0 or new_row >= row_num or new_col < 0 or new_col >= col_num:
                continue
            if board[new_row][new_col] not in current_node:
                continue
            self._find_word_backtrack(board, new_row, new_col, current_node)

        board[row][col] = letter
"""
Complexity:
----------
Time: O(N)
Space: O(N)

"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color != newColor:
            self.fill_color_dfs(image, color, newColor, sr, sc)
        return image
    
    def fill_color_dfs(self, image: List[List[int]], color: int, newColor: int, sr: int, sc: int) -> List[List[int]]:
        if image[sr][sc] == color:
            image[sr][sc] = newColor
            if sr >= 1:
                self.fill_color_dfs(image, color, newColor, sr - 1, sc)
            if sc >= 1:
                self.fill_color_dfs(image, color, newColor, sr, sc - 1)
            if sr + 1 < len(image):
                self.fill_color_dfs(image, color, newColor, sr + 1, sc)
            if sc + 1 < len(image[0]):
                self.fill_color_dfs(image, color, newColor, sr, sc + 1)
            return image
        
"""
Complexity:
---------
Time: O(N log N)
Space: O(log N)

"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_paths_with_sum(root, target_sum):
    if root is None:
        return 0

    path_count_from_root = count_paths_with_sum_from_node(root, target_sum, 0)
    path_count_from_left_tree = count_paths_with_sum(root.left, target_sum)
    path_count_from_right_tree = count_paths_with_sum(root.right, target_sum)

    return path_count_from_root + path_count_from_left_tree + path_count_from_right_tree


def count_paths_with_sum_from_node(node, target_sum, current_sum):
    if node is None:
        return 0
    current_sum += node.value

    total_paths = 0
    if current_sum == target_sum:
        total_paths += 1

    total_paths += count_paths_with_sum_from_node(node.left, target_sum, current_sum)
    total_paths += count_paths_with_sum_from_node(node.right, target_sum, current_sum)

    return total_paths


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.right = TreeNode(-3)
    root.right.right = TreeNode(11)
    count_paths_with_sum(root, 8)

main()
"""
Explanation:
-----------
Variation of 2-Sum Problem.

Complexity:
---------
Time: O(N)
Space: O(log(N))
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_paths_with_sum(root, target_sum):
    return count_paths_with_sum_recursive(root, target_sum, {}, 0)


def count_paths_with_sum_recursive(root, target_sum, path_count_sum_mapping, running_sum):
    if root is None:
        return 0
    running_sum += root.value
    total = running_sum - target_sum
    total_paths = path_count_sum_mapping.get(total, 0)
    if running_sum == target_sum:
        total_paths += 1
    increment_hash_table(path_count_sum_mapping, running_sum, 1)
    total_paths += count_paths_with_sum_recursive(root.left, target_sum, path_count_sum_mapping, running_sum)
    total_paths += count_paths_with_sum_recursive(root.right, target_sum, path_count_sum_mapping, running_sum)
    increment_hash_table(path_count_sum_mapping, running_sum, -1)

    return total_paths


def increment_hash_table(path_count_sum_mapping, running_sum, delta):
    new_count = path_count_sum_mapping.get(running_sum, 0) + delta
    if new_count == 0:
        del path_count_sum_mapping[running_sum]
    else:
        path_count_sum_mapping[running_sum] = new_count


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
    print(count_paths_with_sum(root, 8))

main()
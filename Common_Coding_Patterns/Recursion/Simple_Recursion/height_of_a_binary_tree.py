def find_height_of_a_binary_tree(root):
    if root is None:
        return 0

    l_height = find_height_of_a_binary_tree(root.left)
    r_height = find_height_of_a_binary_tree(root.right)

    return 1 + max(l_height, r_height)
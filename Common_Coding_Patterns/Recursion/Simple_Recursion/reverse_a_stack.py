"""
Problem:
-------
Reverse a stack

Complexity:
----------
Time: O(N^2)
Space: O(1)

"""
def reverse_a_stack(stack):
    reverse_a_stack_recursive(stack)

    return stack


def insert_at_bottom(stack, current_temp):
    if len(stack) == 0:
        stack.append(current_temp)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, current_temp)
        stack.append(temp)


def reverse_a_stack_recursive(stack):
    if len(stack) != 0:
        temp = stack.pop()
        reverse_a_stack_recursive(stack)
        insert_at_bottom(stack, temp)


print(reverse_a_stack([1, 2, 3, 4]))

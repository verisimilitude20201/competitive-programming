def sum_of_a_list_non_tail_recursive(list1):
    if len(list1) == 0:
        return 0

    return list1[0] + sum_of_a_list_non_tail_recursive(list1[1:])


def sum_of_a_list_tail_recursive(list1, l_sum = 0):
    if len(list1) == 0:
        return l_sum

    l_sum += list1[0]

    return sum_of_a_list_tail_recursive(list1[1:], l_sum)


print(sum_of_a_list_non_tail_recursive([1, 2, 3, 4]))
print(sum_of_a_list_tail_recursive([1, 2, 3, 4]))



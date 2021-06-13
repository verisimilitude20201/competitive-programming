def reverse_list(list1):
    low = 0
    high = len(list1) - 1
    reverse_list_recursive(list1, low, high)

    return list1


def reverse_list_recursive(list1, low, high):
    if low == high:
        return
    list1[low], list1[high] = list1[high], list1[low]
    reverse_list_recursive(list1, low + 1, high -1)


print(reverse_list(["h", "e", "l", "l", "o"]))
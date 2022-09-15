def bubble_sort(generic_list):
    is_sorted = False
    passes = len(generic_list) - 1

    while not is_sorted:
        is_sorted = True
        for i in range(passes):
            if (generic_list[i] > generic_list[i + 1]):
                temp = generic_list[i]
                generic_list[i] = generic_list[i + 1]
                generic_list[i + 1] = temp
                is_sorted = False
        passes -= 1
        yield True

    return generic_list

print(bubble_sort([3,5,6,2,10,18,1]))
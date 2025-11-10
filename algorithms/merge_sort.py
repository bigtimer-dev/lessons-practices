# merge sort have a Big O complexity of nlogn
# take in mind that this allocate more resources than any other merge bz recursion create new list until base case
# its faster than bubble sort and insertion sort
# DIVIDE AND CONQUER
def merge_sort(
    unsorted_list=[
        34,
        531,
        51,
        353,
        123,
        516243,
        46214,
        46,
        245,
        45,
        32,
        46,
        78,
        5,
        24,
        56,
    ],
):
    if len(unsorted_list) == 1:  # base case to stop recursion
        return unsorted_list
    median_list = len(unsorted_list) // 2
    half_a = merge_sort(unsorted_list[0:median_list])
    half_b = merge_sort(unsorted_list[median_list:])
    return merge(half_a, half_b)


def merge(half_a, half_b):
    merge_list = []
    while len(half_a) != 0 and len(half_b) != 0:
        if half_a[0] < half_b[0]:
            merge_list.append(half_a[0])
            del half_a[0]
        else:
            merge_list.append(half_b[0])
            del half_b[0]

    while len(half_a):
        merge_list.append(half_a[0])
        del half_a[0]

    while len(half_b):
        merge_list.append(half_b[0])
        del half_b[0]

    return merge_list


def main():
    print(merge_sort())


if __name__ == "__main__":
    main()

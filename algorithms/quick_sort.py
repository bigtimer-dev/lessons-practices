# Quick sort Big O complexity is in average nlogn if we dont pick the highest or the smaller value of the list we need to sort
# in worst case is n^2
#
#
def quick_sort(array, low, high):
    if high <= low:  # base case
        return
    pivot = switching(array, low, high)
    quick_sort(array, pivot + 1, high)
    quick_sort(array, low, pivot - 1)


def switching(array, low, high):
    median = (low + high) // 2  # selecting the median of 3 to avoid worst case
    if array[low] < array[median] and array[median] < array[high]:
        array[high], array[median] = array[median], array[high]

    if array[median] < array[low] and array[low] < array[high]:
        array[high], array[low] = array[low], array[high]

    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1  # returning the pivot for the use of recursive in the other parts


def main():
    array = [
        2,
        35,
        62,
        42672,
        234,
        13,
        674,
        72,
        123,
        45,
        756,
        3244,
        784,
        324,
        52,
        13,
        676,
        46,
        224,
        67563,
        4474,
        556,
        252,
        44333,
    ]
    low = 0
    high = len(array) - 1
    quick_sort(array, low, high)
    print(array)  # since im mutatting the array with quick sort just return it


if __name__ == "__main__":
    main()

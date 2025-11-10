# Quick sort Big O complexity is in average nlogn if we dont pick the highest or the smaller value of the list we need to sort
# in worst case is n^2
#
#
def quick_sort(
    array=[4, 34, 24, 4, 32, 6, 52, 53, 42, 54, 79, 765, 4545, 663, 5, 532, 45, 6, 36],
):
    low = 0
    high = len(array) - 1
    if high <= low:  # base case
        return
    pivot = switching(array, low, high)
    quick_sort(array, pivot + 1, high)
    quick_sort(array, low, pivot - 1)
    return array


def switching(array, start, end):
    pivot = end
    for j in range(len(array)):
        i = j - 1

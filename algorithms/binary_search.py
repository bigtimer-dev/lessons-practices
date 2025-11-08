import sys
import ast
# a binary search is has a Big O complexity of O(log(n))  bz it divide in half the size of the input
# DATA need to be sorted for a binary search to work bz the algorithms rely in that nature of the input DATA


def binary_search(list_sorted, target_value):
    my_list = list_sorted  # out list need to be sorted before hand

    low_val = 0  # lower value of the list

    high_val = len(my_list)  # higher value of the list

    while high_val >= low_val:
        median = (
            low_val + high_val
        ) // 2  # we want entire number to access the mid of the list
        if my_list[median] == target_value:
            print(
                f"the target_value is at index: {median}"
            )  # since we found it lets get out of here
            break

        if my_list[median] > target_value:
            high_val = (
                median - 1
            )  # since the median value of the list is higher than target_value we need to decresease our high_val to be 1 less than median
            continue

        if my_list[median] < target_value:
            low_val = (
                median + 1
            )  # since the median value is less than our target_value we increased the low_val to be median + 1 so we dont include median but the higher than it.


def main():
    if len(sys.argv) < 2:
        print(
            "Please like this Usage: script.py '[1,2,3...int]' target_to_found_in_list"
        )
        return

    if len(sys.argv) == 2:
        my_string = sys.argv[1]
        try:
            my_list = ast.literal_eval(my_string)
            if isinstance(my_list, list):
                print("The list work as expected")
            else:
                print("The list inserted is not a valid list")
                sys.exit(1)

        except (ValueError, SyntaxError) as e:
            print(f"Error parsing string list:{e}")
            return

    target_value = int(sys.argv[2])
    my_list = ast.literal_eval(sys.argv[1])
    binary_search(my_list, target_value)


if __name__ == "__main__":
    main()

# Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order
# Bubble sort is slow his Big O complexity is n^2
def main():
    input_list = [
        2,
        5,
        7,
        23,
        62,
        7345,
        345,
        2347,
        2345,
        3247,
        5573,
        2345,
        7457,
        455,
        224,
        5,
        2435,
    ]  # unorder list
    swapping = True  # to keep track when a swap occur
    end = len(input_list)  # length of the list to be able to iterate over all items
    while swapping:  # while to know when we finish operating all the list
        swapping = False  # set swapping to false that way if a change happen we put again to True
        for i in range(
            1, end
        ):  # start from one index ahead to be able to take the value to comprate with
            if (
                input_list[i - 1] > input_list[i]
            ):  # comparing index 0:end-1 with index 1:end of the list
                input_list[i - 1], input_list[i] = (
                    input_list[i],
                    input_list[i - 1],
                )  # swapping the value if the of index 0 to index 1 bz 0 is bigger
                swapping = True  # since a swap happen we put swapping to true again
        end -= 1  # reduce the end bz the total number of iteration cant be more than the len of the list in the wrost case
    return input_list  # returning the list


if __name__ == "__main__":
    print(main())

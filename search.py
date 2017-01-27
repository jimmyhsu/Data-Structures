#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below

    # check to see that index is within the array, else return none
    if len(array) > index:
        search_value = array[index]
    else:
        return None

    # as long as search doesn't match item call self with an incremented index, else return it
    if search_value is not item:
        return linear_search_recursive(array, item, index + 1)
    else:
        return index

    # fancy try/except way shown in class, does the array length checking
    # faster to do exceptions in python

    # try:
    #     our_value = array[index]
    #     if our_value == item:
    #         return index
    #     else:
    #         return linear_search_recursive(array, item, index+1)
    # except IndexError:
    #     return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    # setup left and right
    left = 0
    right = len(array) - 1

    # as long as the left is less/equal than the right and hasn't crossed over
    while left <= right:

        # find the middle of current set by averaging right and left
        middle = (left + right) / 2  # should give int

        if array[middle] is item:  # return the index if the item is found
            return middle
        elif array[middle] > item:  # since middle is greater than item, check items less than the middle
            right = middle - 1
        elif array[middle] < item:  # since middle is less than item, check items greater than the middle
            left = middle + 1

    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # check to see if it's the first time run
    if left is None or right is None:
        return binary_search_recursive(array, item, 0, len(array) - 1)

    # item not found, the right and left have crossed over
    if right < left:
        return None

    # find the middle of current set by averaging right and left
    middle = (right + left) / 2  # should give int

    if array[middle] is item:  # item is the right item, return it
        return middle
    elif array[middle] > item:  # item is less than what is at index of new middle
        return binary_search_recursive(array, item, left, middle - 1)  # set the new right to check items less than the current middle
    else:
        return binary_search_recursive(array, item, middle + 1, right)  # set the new right to check items more than the current middle

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below

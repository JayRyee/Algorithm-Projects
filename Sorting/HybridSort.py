"""
Name:   Jon Ryan
PID:    A51304061
"""


def quick_sort(unsorted, threshold, start, end, reverse=False):
    """
    Sorts a list in place, using subdivision and insertion sort
    :param unsorted: list to be sorted
    :param threshold: length of sub list at which to use insertion
    :param start: start index
    :param end: end index
    :param reverse: True for high->low order
    :return: no return
    """
    if reverse is False:
        if (end - start) > threshold:
            sub = subdivide(unsorted, start, end, reverse)
            quick_sort(unsorted, threshold, start, sub-1, reverse)
            quick_sort(unsorted, threshold, sub+1, end, reverse)
        else:
            insertion_sort(unsorted, start, end, reverse)

    elif reverse is True:
        if (end - start) > threshold:
            sub = subdivide(unsorted, start, end, reverse)
            quick_sort(unsorted, threshold, start, sub-1, reverse)
            quick_sort(unsorted, threshold, sub+1, end, reverse)
        else:
            insertion_sort(unsorted, start, end, reverse)


def subdivide(unsorted, start, end, reverse):
    """
    Function to divide a list in place, with elements split on pivot low to high
    :param unsorted: list to subdivide
    :param start: start index
    :param end: end index
    :param reverse: True for high->low order
    :return: returns index of pivot element
    """
    pivot = find_pivot(unsorted, start, end)
    # left -> low
    left = start
    # right -> high
    right = end

    if reverse is False:

        # Test if element is < or > then pivot
        # Fill in left and right side from outside to inside
        # Stick pivot element in place after sides are in place
        while True:

            # Element is less than the pivot element
            while left <= right and unsorted[right] > pivot:
                # controll block if find pivot
                right -= 1

            while left <= right and unsorted[left] < pivot:
                left += 1

            if left < right:
                unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
                if unsorted[left] == unsorted[right]:
                    left += 1
            else:
                break

        return right

    elif reverse is True:
        # Test if element is < or > then pivot
        # Fill in left and right side from outside to inside
        # Stick pivot element in place after sides are in place
        while True:

            # Element is less than the pivot element
            while left <= right and unsorted[right] < pivot:
                right -= 1
            while left <= right and unsorted[left] > pivot:
                left += 1

            if left < right:
                unsorted[right], unsorted[left] = unsorted[left], unsorted[right]
                if unsorted[left] == unsorted[right]:
                    right -= 1
            else:
                break

        return left


def find_pivot(unsorted, start, end):
    """
    Function to find pivot element
    :param unsorted: list to find pivot of
    :param start: start index
    :param end: end index
    :return: returns pivot value
    """

    if (end-start) < 2:
        if unsorted[start] is None:
            return unsorted[end]
        else:
            return unsorted[start]

    m_pos = round((start + end)/2)
    center = unsorted[m_pos]
    left = unsorted[start]
    right = unsorted[end]

    # Center is the median
    if left < center < right:
        return center

    # Left is median
    if center < left < right or right < left < center:
        return left

    # Right is median
    if center < right < left or left < right < center:
        return right

    return center


def insertion_sort(unsorted, start, end, reverse):
    """
    Function to perform insertion sort
    :param unsorted: list to sort
    :param start: start index
    :param end: end index
    :param reverse: True for high->low order
    :return: returns None or not at all
    """
    i = start

    if end - start < 0:
        return None

    elif reverse is False:
        for i in range(end+1):
            curr = unsorted[i]
            pos = i

            # Swap every element in list by 1
            while pos > 0 and unsorted[pos-1] > curr:
                unsorted[pos] = unsorted[pos-1]
                pos = pos - 1

            unsorted[pos] = curr

    elif reverse is True:
        for i in range(end+1):
            curr = unsorted[i]
            pos = i

            # Swap every element in list by 1
            while pos > 0 and unsorted[pos-1] < curr:
                unsorted[pos] = unsorted[pos-1]
                pos = pos - 1

            unsorted[pos] = curr


def largest_sequential_difference(lst):
    """
    Function to find largest difference between 2 elements of a sorted list
    :param lst: list to sort, and find L.S.D of
    :return: returns value of largest difference
    """
    if len(lst) >= 2:
        diff = -1

        quick_sort(lst, len(lst)//100, 0, len(lst)-1, False)

        length = len(lst)
        i = 1
        for i in range(length):
            curr_diff = lst[i] - lst[i-1]
            if curr_diff > diff:
                diff = curr_diff

        return diff

    else:
        return None

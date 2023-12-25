def max_unsorted_subarray(n, arr):
    """
    This function takes an array of integers and its size as input and finds the maximum unsorted subarray within it.
    The function prints the start and end indices of the unsorted subarray. If the array is already sorted,
    the function prints -1.

    :param n: The size of the input array.
    :param arr: The input array of integers.
    :return: None. The function prints the result instead of returning it.
    """
    # Create a sorted copy of the input array for comparison
    sorted_arr = sorted(arr)

    # Initialize start and end indices to -1
    start, end = -1, -1

    # Iterate over the array from the beginning to find the first out-of-place element
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            start = i
            break

    # Iterate over the array from the end to find the last out-of-place element
    for i in range(n - 1, -1, -1):
        if arr[i] != sorted_arr[i]:
            end = i
            break

    # If the start and end indices are the same, it means the array is already sorted. Print -1 in this case.
    # Otherwise, print the start and end indices (incremented by 1 to adjust for 0-based indexing).
    if start == -1 and end == -1:
        print(-1)
    else:
        print(start + 1, end + 1)


# Read the size of the array from the input
input_n = int(input())

# Read the array of integers from the input. The array is expected to be space-separated.
input_arr = list(map(int, input().split()))

# Call the function with the user's input.
max_unsorted_subarray(input_n, input_arr)

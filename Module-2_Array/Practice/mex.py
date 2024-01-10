"""
You are given an array A of non-negative integers of size N. You have to find the minimum non-negative integer which is not present in the array.

Input: The input consists of two lines. The First one having one integer N. Second line contains N space separated
integers between 0 and 10^9

Output:
Print the minimum non-negative integer which is not present in the array.

Constraints:
1≤≤ N≤≤10^5

Example 1:
Input:
6
1 2 0 4 4 6
Output:
3

Example 2:
Input:
3
1 2 3
Output:
0
"""


def fill(arr):
    maximum = max(arr)
    check = [0] * (maximum + 1)

    for i in range(len(arr)):
        check[arr[i]] = 1

    for i in range(len(check)):
        if check[i] == 0:
            return i
    return maximum + 1


input_n = int(input())
input_arr = list(map(int, input().split()))
print(fill(input_arr))

"""
You are given an array of integers. Where all the elements are different except one, your task is to find that element.

Input
The input consists of two lines. First one having one integer N. Second line contains N space seperated integers between 1 and N.

Output
Output a single integer which occured twice in the array.

Constraints
2 ≤≤ N ≤≤ 5000
Every integer of the array is between 1 and N

Example 1:
Input:
4
1 2 3 2
Output:
2

Example 2:
Input:
6
1 2 5 4 3 5
Output:
5
"""


def duplicate(arr):
    # My solution
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            if arr[i] == j:
                return arr[i]


# another solution
def duplicate_2(arr):
    # efficient solution
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None


# another solution
def duplicate_3(arr):
    # more efficient
    check = [0] * len(arr)

    for i in range(len(arr)):
        if check[arr[i]] == 1:
            return arr[i]
        else:
            check[arr[i]] = 1


input_n = int(input())
input_arr = list(map(int, input().split()))
print(duplicate(input_arr))

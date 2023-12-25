def multiply(a, b):
    """
    Task: Two
    Time complexity: O(b)
    Space complexity: O(b)
    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)


print(multiply(4, 5))
print(multiply(3, 3))
print(multiply(0, 2))

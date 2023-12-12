# Task 2
def sum_of_a_b(a, b):
    """
    Task 2: sum of two numbers
    here time complexity is O(n)
    here space complexity is O(1)
    """
    if a > 0 and b <= 100000:
        result = 0
        if a < b:
            for i in range(a, b + 1):
                result = result + i
        else:
            for i in range(b, a + 1):
                result = result + i
        return result


print(f'sum of A and B: {sum_of_a_b(10, 6)}')

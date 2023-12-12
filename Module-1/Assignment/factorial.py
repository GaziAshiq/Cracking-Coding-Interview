# Task 1
def factorial(number):
    """
    Task 1: Factorial
    Here Time complexity is O(n)
    Here space complexity is O(1)
    """
    if 1 <= number <= 10:
        result = 1
        for i in range(1, number + 1):
            result = result * i
        return result


print(f'factorial: {factorial(4)}')

def string_indices(text, indices):
    """
        Task 1
        You are given a string s and an integer array indices of the same length. The string s will be shuffled such
        that the character at the ith position moves to indices[i] in the shuffled string. Return the shuffled string.

        Time complexity: O(n)
        Space complexity: O(1)
    """
    result = []
    if 1 <= len(text) == len(indices) <= 100:
        for i in indices:
            result.append(text[i])
        return ''.join(result)
    else:
        return 0


print(string_indices(text="mamacode", indices=[4, 5, 6, 7, 0, 1, 2, 3]))
print(string_indices(text="dosta", indices=[4, 0, 1, 2, 3]))
print(string_indices(text="abc", indices=[1, 0, 2]))

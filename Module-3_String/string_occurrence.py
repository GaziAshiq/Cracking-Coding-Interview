def occurrence(haystack, needle):
    """
        Task 2:
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack. Also, mention the Time and Space Complexity of your solution

        Time complexity: O(n)
        Space complexity: O(1)
    """
    needle_len = len(needle)
    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i
    return -1


print(occurrence(haystack="sadbutsad", needle="sad"))
print(occurrence(haystack="codemama", needle="ostad"))

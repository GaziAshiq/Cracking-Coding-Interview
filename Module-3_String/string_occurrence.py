def occurrence(haystack, needle):
    """
        Task 2:
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack. Also, mention the Time and Space Complexity of your solution

        Time complexity: O(log n)
        Space complexity: O(1)
    """
    needle_hash = hash(needle)
    needle_len = len(needle)
    for i in range(0,len(haystack), needle_len):
        current_hash = hash(haystack[i:needle_len])
        if needle_hash == current_hash:
            return i
        else: return -1

print(occurrence(haystack = "sadbutsad", needle = "sad"))
print(occurrence(haystack = "codemama", needle = "ostad"))

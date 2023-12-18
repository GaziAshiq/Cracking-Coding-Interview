# Task 1:
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the
character at the ith position moves to indices[i] in the shuffled string. Return the shuffled string.

Also, mention the Time and Space Complexity of your solution

Constraints:
s.length == indices.length == n
1 <= n <= 100
s consists of only lowercase English letters.
0 <= indices[i] < n
All values of indices are unique.

Example 1:
Input: s = "mamacode", indices = [4,5,6,7,0,1,2,3]
Output: "codemama"
Explanation: As shown, "mamacode" becomes "codemama" after shuffling.

Example 2:
Input: s = "dosta", indices = [4,0,1,2,3]
Output: "ostad"
Explanation: After shuffling, each character remains in its position.

Example 3:
Input: s = "abc", indices = [1,0,2]
Output: "bac"
Explanation: After shuffling, each character remains in its position.


# Task 2:
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Also, mention the Time and Space Complexity of your solution

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "codemama", needle = "ostad"
Output: -1
Explanation: "ostad" did not occur in "codemama", so we return -1.

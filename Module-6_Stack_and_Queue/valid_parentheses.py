# class Solution:
#     # my solution
#     def isValid(self, s: str) -> bool:
#         li = list()
#
#         for i in s:
#             if i == '(' or i == '{' or i == '[':
#                 li.append(i)
#             else:
#                 if not li:
#                     return False
#                 opening = li[-1]
#                 li.pop()
#
#                 if i == ')' and opening != '(':
#                     return False
#                 elif i == '}' and opening != '{':
#                     return False
#                 elif i == ']' and opening != '[':
#                     return False
#
#         if not li:
#             return True
#         return False
#
#
# class Solution:
#     # simple solution
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {")": "(", "}": "{", "]": "["}
#
#         for char in s:
#             if char in mapping:
#                 if not stack or mapping[char] != stack.pop():
#                     return False
#             else:
#                 stack.append(char)
#
#         return not stack


class Solution(object):
    """
    A class used to represent a solution for validating parentheses in a string.

    ...

    Methods
    -------
    isValid(s: str) -> bool
        Validates if the input string has correctly nested and ordered parentheses.
    """

    def isValid(self, s):
        """
        Validates if the input string has correctly nested and ordered parentheses.

        Parameters
        ----------
        s : str
            A string containing just the characters '(', ')', '{', '}', '[' and ']'

        Returns
        -------
        bool
            True if the input string has valid parentheses, False otherwise

        """

        # Initialize an empty list to use as a stack
        stack = []

        # Define a dictionary to map each closing bracket to its corresponding opening bracket
        bracket_pairs = {')': '(', '}': '{', ']': '['}

        # Iterate over each character in the input string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_pairs.values():
                stack.append(char)
            # If the character is a closing bracket, check if the stack is empty or if the top element of the stack
            # doesn't match the corresponding opening bracket for the current closing bracket
            elif char in bracket_pairs.keys():
                if not stack or stack.pop() != bracket_pairs[char]:
                    # If either condition is true, return False
                    return False
            else:
                # If the character is neither an opening bracket nor a closing bracket, return False
                return False

        # After iterating over all characters in the string, check if the stack is empty
        # If it is, return True, indicating that the string has valid parentheses
        # If the stack isn't empty, return False
        return not stack

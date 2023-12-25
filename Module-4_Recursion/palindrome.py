def is_palindrome(s):
    """
    Task : One
    Time complexity: O(n)
    Space complexity: O(n)
    :param s: string
    :return: bool
    """
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


print(is_palindrome("madam"))
print(is_palindrome("adam"))
print(is_palindrome("tenet"))

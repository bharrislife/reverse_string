"""
Chapter 1: Reverse a String
From "Learn Python and Get a Job... Guaranteed" by Betty Harris
Interview Framework Series — Python interview question #1

Run it from the command line:
    python3 reverse_string.py
"""

def reverse_string(s):
    """Reverse a string using Python slicing. O(n) time, O(n) space."""
    return s[::-1]


def reverse_string_loop(s):
    """Reverse a string without slicing, using a loop. O(n) time, O(n) space."""
    result = ""
    for char in s:
        result = char + result
    return result


def reverse_in_place(chars):
    """
    Reverse a list of characters in place, using two pointers.
    O(n) time, O(1) space — lists are mutable, strings are not.
    """
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars


def check_username(username):
    """Ship It project: Palindrome-Friendly Username Checker."""
    cleaned = username.lower()
    if cleaned == cleaned[::-1]:
        return f"'{username}' is a palindrome username!"
    else:
        return f"'{username}' is not a palindrome."


if __name__ == "__main__":
    print(reverse_string("hello"))
    # Output: olleh

    print(reverse_string_loop("hello"))
    # Output: olleh

    print(reverse_in_place(list("hello")))
    # Output: ['o', 'l', 'l', 'e', 'h']

    for name in ["Anna", "BettyB", "Level", "PythonDev"]:
        print(check_username(name))


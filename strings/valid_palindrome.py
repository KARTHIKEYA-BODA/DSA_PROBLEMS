"""
Problem: Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Approach (Two Pointers):
- Place two pointers: `left` at index 0 and `right` at the last index.
- Move pointers inward, skipping non-alphanumeric characters using `.isalnum()`.
- Compare characters at both pointers case-insensitively using `.lower()`.
- If mismatch occurs, return False. If pointers meet or cross, return True.

Time Complexity: O(n) - Single pass traversing inwards from both ends.
Space Complexity: O(1) - Constant auxiliary space without creating a copy of the filtered string.
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    test_1 = "A man, a plan, a canal: Panama"
    test_2 = "race a car"
    print(f"'{test_1}' -> is_palindrome: {is_palindrome(test_1)}")
    print(f"'{test_2}' -> is_palindrome: {is_palindrome(test_2)}")
    assert is_palindrome(test_1) is True
    assert is_palindrome(test_2) is False

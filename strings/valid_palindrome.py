# Check if a string is a palindrome, ignoring non-letters and case


def is_palindrome(s):
    left = 0
    right = len(s) - 1

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
    test1 = "A man, a plan, a canal: Panama"
    test2 = "race a car"
    print("Test 1:", is_palindrome(test1))
    print("Test 2:", is_palindrome(test2))
    assert is_palindrome(test1) is True
    assert is_palindrome(test2) is False

"""
Problem: Valid Anagram
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

Approach (Frequency Count):
- An anagram requires strings of identical length with identical character frequencies.
- First verify lengths; if len(s) != len(t), immediately return False.
- Count the frequency of each character in both strings using a hash map (or collections.Counter).
- Compare the frequency maps.

Time Complexity: O(n) - Single pass over both strings to count frequencies.
Space Complexity: O(1) - Constant auxiliary space since alphabet size is bounded (e.g. 26 lowercase English letters).
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    print(f"'{s1}' & '{t1}' -> is_anagram: {is_anagram(s1, t1)}")
    print(f"'{s2}' & '{t2}' -> is_anagram: {is_anagram(s2, t2)}")
    assert is_anagram(s1, t1) is True
    assert is_anagram(s2, t2) is False

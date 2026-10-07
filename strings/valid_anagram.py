# Check if two strings are anagrams


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts or counts[ch] == 0:
            return False
        counts[ch] -= 1

    return True


if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    print("Is anagram:", s1, t1, "->", is_anagram(s1, t1))
    print("Is anagram:", s2, t2, "->", is_anagram(s2, t2))
    assert is_anagram(s1, t1) is True
    assert is_anagram(s2, t2) is False

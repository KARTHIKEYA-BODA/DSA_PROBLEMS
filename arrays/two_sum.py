"""
Problem: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Assume each input has exactly one solution, and you may not use the same element twice.

Approach:
- Use a hash map (dictionary) to store each number and its index as we iterate through the list.
- For each number `num`, compute its complement: `target - num`.
- If the complement already exists in the dictionary, we have found our pair and return their indices.
- Otherwise, record `num: index` into the dictionary and continue.

Time Complexity: O(n) - Single pass through the array with O(1) average dictionary lookups.
Space Complexity: O(n) - Storing up to n elements in the dictionary.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two Sum: nums={nums}, target={target} -> indices={result}")
    assert result == [0, 1]

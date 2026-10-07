"""
Problem: Maximum Subarray (Kadane's Algorithm)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Approach (Kadane's Algorithm):
- Track two values while traversing:
  1. `current_sum`: maximum subarray sum ending at current position (either current element alone, or previous current_sum + current element).
  2. `max_sum`: maximum sum found across all subarrays seen so far.
- If `current_sum` drops below the current element itself, starting fresh from the current element is optimal.

Time Complexity: O(n) - Single pass through the array.
Space Complexity: O(1) - Only constant extra variables used.
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0
    max_sum = current_sum = nums[0]
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_sub_array(nums)
    print(f"Maximum Subarray: nums={nums} -> max_sum={result}")
    assert result == 6  # Subarray [4, -1, 2, 1] has the largest sum = 6

# Find the contiguous subarray with the largest sum


def max_sub_array(nums):
    if not nums:
        return 0

    max_sum = nums[0]
    current_sum = nums[0]

    for x in nums[1:]:
        # pick the larger between starting new or adding to current sum
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_sub_array(nums)
    print("Max subarray sum:", result)
    assert result == 6

"""
Problem: Merge Sort
Sort an array of comparable elements in ascending order using divide-and-conquer.

Approach (Divide and Conquer):
- Divide: Split the unsorted list at the midpoint into two halves.
- Conquer: Recursively sort each sub-half until subarrays of size <= 1 are reached (trivially sorted).
- Combine: Merge the two sorted subarrays by comparing leading elements and collecting them in ascending order.

Time Complexity: O(n log n) - Guaranteed in all cases (best, average, worst) as tree depth is log n and merge work at each level is O(n).
Space Complexity: O(n) - Requires auxiliary memory to hold the merged elements.
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    return _merge(left_sorted, right_sorted)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    sorted_sample = merge_sort(sample)
    print(f"Original: {sample}")
    print(f"Sorted:   {sorted_sample}")
    assert sorted_sample == sorted(sample)

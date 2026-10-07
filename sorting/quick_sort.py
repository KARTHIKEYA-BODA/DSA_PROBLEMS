"""
Problem: Quick Sort
Sort an array of comparable elements in ascending order using in-place partitioning.

Approach (Divide and Conquer with Lomuto Partitioning):
- Choose the last element of the current subarray as the pivot.
- Partitioning: Iterate over elements, swapping any element smaller than or equal to pivot to the front section.
- Place pivot at its final sorted boundary index.
- Recursively apply quicksort to the left partition (elements < pivot) and right partition (elements > pivot).

Time Complexity:
- Average / Best Case: O(n log n) - Occurs when pivot splits array roughly in half.
- Worst Case: O(n^2) - Occurs with unbalanced splits (e.g. already sorted list with fixed end pivot).
Space Complexity: O(log n) auxiliary stack space on average for recursive frames.
"""
from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    def _quick_sort(low: int, high: int):
        if low < high:
            pivot_idx = _partition(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)

    def _partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    result = quick_sort(sample.copy())
    print(f"Original: {sample}")
    print(f"Sorted:   {result}")
    assert result == [1, 5, 7, 8, 9, 10]

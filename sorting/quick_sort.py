# Quick sort implementation


def quick_sort(arr):
    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    sort(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    result = quick_sort(sample.copy())
    print("Original:", sample)
    print("Sorted:  ", result)
    assert result == [1, 5, 7, 8, 9, 10]

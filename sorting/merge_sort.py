# Merge sort implementation


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add the remaining items
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    sorted_sample = merge_sort(sample)
    print("Original:", sample)
    print("Sorted:  ", sorted_sample)
    assert sorted_sample == sorted(sample)

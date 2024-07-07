def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
if __name__ == "__main__":
    # Test the merge sort function
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted list:", unsorted_list)
    
    sorted_list = merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)
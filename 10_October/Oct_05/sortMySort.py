import random
import math

def introsort(arr):
    max_depth = 2 * math.floor(math.log2(len(arr)))
    _introsort_helper(arr, 0, len(arr) - 1, max_depth)

def _introsort_helper(arr, start, end, max_depth):
    if end - start <= 1:
        return
    elif max_depth == 0:
        heapsort(arr, start, end)
    else:
        p = partition(arr, start, end)
        _introsort_helper(arr, start, p - 1, max_depth - 1)
        _introsort_helper(arr, p + 1, end, max_depth - 1)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapsort(arr, start, end):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for start in range((end - start) // 2 - 1, -1, -1):
        sift_down(start, end)

    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(0, end - 1)

# Test the sorting algorithm
if __name__ == "__main__":
    # Generate a list of 1000 random integers
    test_array = [random.randint(1, 1000) for _ in range(1000)]
    
    print("Original array (first 10 elements):", test_array[:10])
    introsort(test_array)
    print("Sorted array (first 10 elements):", test_array[:10])
    
    # Verify if the array is sorted
    print("Is the array sorted?", all(test_array[i] <= test_array[i+1] for i in range(len(test_array)-1)))
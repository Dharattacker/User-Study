def bubble_sort(arr):
    n = len(arr)
    # Outer loop for each element in the list
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array (bubble):", bubble_sort(arr))

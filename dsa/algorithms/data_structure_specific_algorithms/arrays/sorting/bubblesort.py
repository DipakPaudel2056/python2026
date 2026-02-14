# so this is basic of the  sorting algorithm,
# although it is not efficientt for large data ssett it is easier to understand

# the core idea is to step troug the list and compare the next element, if it is greater than the next element swap them, if not move to the nextt element and repeat the process until the end of the list is reached, then repeat the whole process until no more swaps are needed

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # flag to check if any swapping occurs
        swapped = False
        for j in range(0, n-i-1):
            # compare adjacent elements
            if arr[j] > arr[j+1]:
                # swap if the element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # if no swapping occurred, the list is already sorted
        if not swapped:
            break

# so what would be the time complexity of this algorithm, it is O(n^2) in the worst and average case, and O(n) in the best case when the list is already sorted, because we only need to make one pass through the list to check if it is sorted

# let's test the bubble sort algorithm
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)
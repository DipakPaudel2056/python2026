# it is also the simple sorting algorithm taking 2 part, one is sorted and another one is not sorted,
# the idea is to take one element from the unsorted part and insert it into the correct position in the sorted part, repeat this process until all elements are sorted

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr.pop(i)
        
        for j in range(i-1,-1,-1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)
    return arr      

# the time complexity of insertion sort is O(n^2) in the worst and average case, and O(n) in the best case when the list is already sorted, because we only need to make one pass through the list to check if it is sorted
# let's test the insertion sort algorithm
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)
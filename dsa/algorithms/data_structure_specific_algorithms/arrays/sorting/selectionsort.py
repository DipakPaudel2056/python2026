# the idea behind selection sort is to go through the list using two loops,
# the outer loop will iterate through the list and inner loop will find the minimum value in the remaining list and they swap the position 
# untill they reach the end of the list

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = arr[i]
        min_index = i
        for j in range(i+1, n):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# the time complexity of selection sort is O(n^2) in all cases because it always requires two nested loops to complete the sorting process, regardless of the initial order of the elements in the list
# let's test the selection sort algorithm
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
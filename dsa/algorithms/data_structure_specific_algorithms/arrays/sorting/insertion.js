// let's work in insertion sort algorithm in javascript
function insertionSort(arr) {
  let n = arr.length;   
    for (let i = 1; i < n; i++) {
        let key = arr[i];
        let j = i - 1;      
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }   
        arr[j + 1] = key;
    }   
    return arr;
}
// let's test the insertion sort algorithm
let arr = [12, 11, 13, 5, 6];
console.log("Unsorted array: " + arr);
console.log("Sorted array: " + insertionSort(arr));
// selection sort
function selectionSort(arr) {
  let n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let min = arr[i];
    let min_index = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < min) {
        min = arr[j];
        min_index = j;
      }
    }
    [arr[i], arr[min_index]] = [arr[min_index], arr[i]];
  }
  return arr;
}

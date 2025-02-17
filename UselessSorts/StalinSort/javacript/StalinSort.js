function stalinSort(unsorted_array) {
  let sorted_array = [];
  let i = 0;
  let j = 1;

  sorted_array.push(unsorted_array[0]);

  while (j < unsorted_array.length) {
    if (sorted_array[i] <= unsorted_array[j]) {
      sorted_array.push(unsorted_array[j]);
      i++;
      j++;
    } else {
      j++;
    }
  }

  return sorted_array;
}

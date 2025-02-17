function createArray(array_length, array_range) {

  let unsortedArray = [];

  for (var i = 0; i < array_length; i++) {
    unsortedArray.push(Math.floor(Math.random() * array_range))
  }

  return unsortedArray;
}

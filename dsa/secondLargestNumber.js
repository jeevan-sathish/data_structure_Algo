// Find Second Largest Number

function FindSecondLargestNumber(arr) {
  let largest = arr[0];
  let smallest = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
      if (arr[i] < smallest) {
        smallest = arr[i];
      }
    }
  }
  return smallest;
}

const array = [2, 5, 9, 4, 3];
const result = FindSecondLargestNumber(array);
console.log(result);

//Reverse the array
function ReverseArray(arr) {
  let rev = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    rev.push(arr[i]);
  }
  return rev;
}
const array = [1, 2, 3, 4, 5];
const result = ReverseArray(array);
console.log(result);

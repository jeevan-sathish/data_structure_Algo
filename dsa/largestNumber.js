// find largest number

function FindLargestNumber(num) {
  let largest = num[0];
  for (let i = 0; i < num.length; i++) {
    if (num[i] > largest) {
      largest = num[i];
    }
  }
  return largest;
}

const number = [10, 4, 7, 2, 9];
const result = FindLargestNumber(number);
console.log(result);

// find smallest number

function FindSmallestNumber(num) {
  let smallest = num[0];
  for (let i = 0; i < num.length; i++) {
    if (num[i] < smallest) {
      smallest = num[i];
    }
  }
  return smallest;
}

const numbers = [2, 5, 0, 1, 4, 7];
const result = FindSmallestNumber(numbers);
console.log(result);

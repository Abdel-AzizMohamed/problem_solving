// ###### Solution 1
function repeats(arr) {
  let result = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr.filter((ele) => ele === arr[i]).length === 1) result += arr[i];
  }

  return result;
}

// ###### Solution 2
function repeats(arr) {
  return arr.reduce(
    (acc, cur) =>
      arr.filter((ele) => ele === cur).length === 1 ? acc + cur : acc,
    0
  );
}

// ###### Solution 3
function repeats(arr) {
  return (
    2 * Array.from(new Set(arr)).reduce((a, c) => a + c) -
    arr.reduce((a, c) => a + c)
  );
}

// ###### Video Link:
// ###### Problem Link: https://www.codewars.com/kata/59f11118a5e129e591000134/train/javascript

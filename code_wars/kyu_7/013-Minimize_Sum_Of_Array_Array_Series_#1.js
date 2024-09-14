// ###### Solution 1
function minSum(arr) {
  const sort_arr = arr.sort((a, b) => a - b);
  let result = 0;

  for (let i = 0; i < arr.length / 2; i++)
    result += sort_arr[i] * sort_arr[arr.length - 1 - i];

  return result;
}

// ###### Solution 2
function minSum(arr) {
  const sort_arr = arr.sort((a, b) => a - b);
  return arr
    .slice(0, arr.length / 2)
    .reduce((a, c, i) => a + c * sort_arr[arr.length - 1 - i], 0);
}

// ###### Video Link:
// ###### Problem Link: https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/javascript

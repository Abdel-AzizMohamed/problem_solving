// ###### Solution 1
function findLongest(array) {
  let result = array[0];

  for (let i = 1; i < array.length; i++) {
    if (String(array[i]).length > String(result).length) result = array[i];
  }

  return result;
}

// ###### Solution 2
function findLongest(array) {
  return array.reduce((acc, cur) =>
    String(acc).length < String(cur).length ? cur : acc
  );
}
// ###### Link:
// ###### Problem Link: https://www.codewars.com/kata/58daa7617332e59593000006/train/javascript

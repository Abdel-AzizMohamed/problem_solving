// ###### Solution 1 (Takes a lot of time)
function triangular(n) {
  if (n <= 0) return 0;
  let result = 0;

  for (let i = 1; i <= n; i++) result += i;

  return result;
}

// ###### Solution 2
function triangular(n) {
  return n <= 0 ? 0 : Math.floor((n * (n + 1)) / 2);
}

// ###### 09
// ###### Problem Link: https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/javascript

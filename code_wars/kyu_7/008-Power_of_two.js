// ###### Solution 1

function isPowerOfTwo(n) {
  for (let i = 0; 2 ** i <= n; i++) {
    if (2 ** i === n) return true;
  }
  return false;
}
// ###### Solution 2

function isPowerOfTwo(n) {
  return Math.log2(n) % 1 === 0;
}

// ###### 08
// ###### Problem Link: https://www.codewars.com/kata/534d0a229345375d520006a0/train/javascript

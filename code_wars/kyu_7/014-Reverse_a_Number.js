// ###### Solution 1
function reverseNumber(n) {
  let result = "";
  const sign = n < 0 ? -1 : 1;
  n = String(Math.abs(n));

  for (let i = 0; i < n.length; i++) result = n[i] + result;

  return sign * Number(result);
}
// ###### Video Link:
// ###### Problem Link: https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/javascript

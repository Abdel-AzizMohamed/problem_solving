//###### Solution 1
var uniqueInOrder = function (iterable) {
  let unique_seq = [];

  for (let i = 0; i < iterable.length; i++) {
    if (i === 0 || iterable[i] !== iterable[i - 1])
      unique_seq.push(iterable[i]);
  }

  return unique_seq;
};

//###### Solution 2
var uniqueInOrder = function (iterable) {
  if (typeof iterable === "string" || iterable instanceof String)
    iterable = iterable.split("");
  return iterable.filter((ele, i) => i === 0 || ele !== iterable[i - 1]);
};

//###### Link: Video 008
//###### Problem Link: https://www.codewars.com/kata/54e6533c92449cc251001667/train/javascript

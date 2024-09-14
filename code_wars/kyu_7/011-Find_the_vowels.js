// ###### Solution 1
function vowelIndices(word) {
  const vowels = new Set(["a", "e", "i", "o", "u", "y"]);
  let result = [];
  word = word.toLowerCase();

  for (let i = 0; i < word.length; i++) {
    if (vowels.has(word[i])) result.push(i + 1);
  }

  return result;
}

// ###### Solution 2
function vowelIndices(word) {
  const vowels = new Set(["a", "e", "i", "o", "u", "y"]);
  return word
    .toLowerCase()
    .split("")
    .map((ele, ind) => (vowels.has(ele) ? ind + 1 : 0))
    .filter((ele) => ele);
}
// ###### Video Link:
// ###### Problem Link: https://www.codewars.com/kata/5680781b6b7c2be860000036/train/javascript

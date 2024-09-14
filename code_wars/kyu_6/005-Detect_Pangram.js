// ###### Solution 1
function isPangram(string) {
  const letters = Array.from({ length: 26 }, (_, index) =>
    String.fromCharCode(`${index + 97}`)
  );

  string = string.toLowerCase();

  for (let i = 0; i < letters.length; i++) {
    if (!string.includes(letters[i])) return false;
  }

  return true;
}

// ###### Video Link:
// ###### Problem Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

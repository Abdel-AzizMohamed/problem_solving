//###### Solution 1
function pigIt(str) {
  let result = [];
  const words = str.split(" "),
    pun = new Set([",", ".", "!", "?"]);

  for (let i = 0; i < words.length; i++) {
    if (pun.has(words[i][0])) {
      result.push(words[i]);
      continue;
    }
    result.push(words[i].slice(1) + words[i][0] + "ay");
  }

  return result.join(" ");
}

//###### Solution 1
function pigIt(str) {
  const pun = new Set([",", ".", "!", "?"]);
  return str
    .split(" ")
    .map((ele) => (pun.has(ele[0]) ? ele : `${ele.slice(1)}${ele[0]}ay`))
    .join(" ");
}

// ###### Problem Link: https://www.codewars.com/kata/513e08acc600c94f01000001/train/javascript

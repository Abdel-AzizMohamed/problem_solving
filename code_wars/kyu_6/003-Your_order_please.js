// ###### JS ######
// ###### Solution 1
function order(words) {
  let words_split = words.split(" "),
    result = [...Array(words_split.length)];

  for (let i = 0; i < words_split.length; i++) {
    let num = words_split[i].match(/\d/)[0];
    result[Number(num)] = words_split[i];
  }

  return result;
}

// ######

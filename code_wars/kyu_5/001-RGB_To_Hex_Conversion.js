//###### Solution 1
function rgb(r, g, b) {
  let hexTable = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
  };
  return [r, g, b]
    .map((color) => {
      color = color > 255 ? 255 : color < 0 ? 0 : color;
      return (
        hexTable[String(Math.floor(((color / 256) % 1) * 16))] +
        hexTable[String(Number(color % 16))]
      );
    })
    .join("");
}

//###### Solution 2
function rgb(r, g, b) {
  return [r, g, b]
    .map((color) => {
      color = Math.min(255, Math.max(color, 0));
      let hex = color.toString(16).toUpperCase();
      return hex.length === 1 ? "0" + hex : hex;
    })
    .join("");
}

// ###### Link:
// ###### Problem Link: https://www.codewars.com/kata/513e08acc600c94f01000001/train/javascript

// ###### Solution 1
function findNeedle(haystack) {
  let needleIndex = -1;

  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === "needle") {
      needleIndex = i;
      break;
    }
  }

  return `found the needle at position ${needleIndex}`;
}

// ###### Solution 2
function findNeedle(haystack) {
  return `found the needle at position ${haystack.indexOf("needle")}`;
}

// ###### Video Link:
// ###### Problem Link: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/javascript

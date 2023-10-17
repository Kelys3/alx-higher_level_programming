#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let e = 0; e < list.length; e++) {
    if (list[e] === searchElement) {
      count++;
    }
  }
  return count;
};

#!/usr/bin/node
exports.esrever = function (list) {
  const listReverse = [];

  for (let r = list.length - 1; r >= 0; r--) {
    listReverse.push(list[r]);
  }

  return listReverse;
};

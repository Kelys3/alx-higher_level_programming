#!/usr/bin/node
const dict = require('./101-data').dict;

const userIds = Object.entries(dict);
const ocrs = Object.values(dict);
const newData = [...new Set(ocrs)];
const newDict = {};
for (const j in newData) {
  const list = [];
  for (const k in userIds) {
    if (userIds[k][1] === newData[j]) {
      list.unshift(userIds[k][0]);
    }
  }
  newDict[newData[j]] = list;
}
console.log(newDict);

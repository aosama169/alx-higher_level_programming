#!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const uniqueVal = [...new Set(vals)];
const nDict = {};

for (const j in uniqueVal) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === uniqueVal[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  nDict[uniqueVal[j]] = list;
}

console.log(nDict);

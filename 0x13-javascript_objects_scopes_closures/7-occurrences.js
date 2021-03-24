#!/usr/bin/node
// Write a function that returns the number of ocurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i in list) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};

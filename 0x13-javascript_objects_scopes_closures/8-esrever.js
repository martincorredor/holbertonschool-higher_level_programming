#!/usr/bin/node
// Write a function that reverses a list
exports.esrever = function (list) {
  let copyList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    copyList.join(list[i]);
  }
  return (copyList);
};

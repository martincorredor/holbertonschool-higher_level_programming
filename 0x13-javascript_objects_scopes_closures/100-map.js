#!/usr/bin/node
// Return new list must be created with each value equal to the value of the initial list
// multipled by the index in the list

const list = require('./100-data').list;

console.log(list);
console.log(list.map((x, index) => x * index));
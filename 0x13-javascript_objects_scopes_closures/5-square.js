#!/usr/bin/node
// Write a class Square that defines an square and inherits from Rectangle class
const Rectangle = require("./4-rectangle");
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

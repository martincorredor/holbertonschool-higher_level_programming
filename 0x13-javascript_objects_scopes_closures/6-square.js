#!/usr/bin/node
// Write a class Square that defines an square and inherits from Rectangle class
const SquareParent = require("./5-square");

module.exports = class Square extends SquareParent {
  // Method that prints the rectangle with parameter c or 'X'
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

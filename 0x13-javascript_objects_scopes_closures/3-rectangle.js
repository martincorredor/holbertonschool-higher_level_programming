#!/usr/bin/node
//
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }
// Method that prints the rectangle with 'X' 
  print () {
    for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
    }
  }
};

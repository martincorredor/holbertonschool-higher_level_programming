#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
// If w or h is equal to 0 or not a positive integer, create an empty object
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
      console.log("X".repeat(this.width));
    }
  }

  // Method that changes the width and height values
  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  // Method that multiplies width and height values for two
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};

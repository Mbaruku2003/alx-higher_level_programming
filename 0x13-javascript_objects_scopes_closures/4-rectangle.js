#!/usr/bin/node
/* defines a rectangle */
class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }

  rotate () {
    const j = this.width;
    this.width = this.height;
    this.height = j;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;

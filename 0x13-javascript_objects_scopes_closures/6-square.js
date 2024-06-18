#!/usr/bin/node
/* defines a square and inherits from Square of 5-square.js */
const ssquare = require('./5-square.js');
class Square extends ssquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;

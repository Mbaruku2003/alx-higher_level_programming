#!/usr/bin/node
/* defines a square and inherits from Rectangle of 4-rectangle.js */
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;

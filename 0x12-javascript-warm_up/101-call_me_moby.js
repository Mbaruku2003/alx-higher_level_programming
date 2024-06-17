#!/usr/bin/node
/* executes x times a function. */
exports.callMeMoby = function (x, functions) {
  for (let i = 0; i < x; i++) {
    functions();
  }
};

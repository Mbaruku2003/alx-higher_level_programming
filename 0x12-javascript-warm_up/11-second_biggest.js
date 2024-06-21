#!/usr/bin/node
/* searches the second biggest integer in the list of arguments. */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2).map(Number);
  const secondarr = array.sort(function (a, b) { return b - a; })[1];
  console.log(secondarr);
}

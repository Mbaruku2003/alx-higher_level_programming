#!/usr/bin/node
/* computes and prints a factorial */
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(Number(factorial(process.argv[2])));

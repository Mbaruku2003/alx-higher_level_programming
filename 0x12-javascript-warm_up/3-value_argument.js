#!/usr/bin/node
/* prints the first argument passed to it: */
if (process.argv[1] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[1]);
}

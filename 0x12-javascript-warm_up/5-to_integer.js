#!/usr/bin/node
/*  prints My number: <first argument converted in integer> */
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}

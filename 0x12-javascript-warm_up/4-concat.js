#!/usr/bin/node
/* prints two arguments passed to it, in the following format is */
let firstword;
firstword = process.argv[2];
firstword += ' is ';
firstword += process.argv[3];
console.log(firstword);

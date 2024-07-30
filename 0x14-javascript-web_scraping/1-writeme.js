#!/usr/bin/node
const fs = require('fs');
const thefile = process.argv(2);
const content = process.argv(3);
if (!content || !thefile) {
  console.error();
  process.exit(1);
}
fs.readFile(thefile, utf-8, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});

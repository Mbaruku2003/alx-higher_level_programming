#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
if (!filepath) {
  console.error();
  process.exit(1);
}
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

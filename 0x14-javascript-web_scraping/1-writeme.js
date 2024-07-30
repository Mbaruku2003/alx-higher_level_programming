#!/usr/bin/node
const fs = require('fs');
if (process.argv.length !== 4) {
  console.error();
  process.exit(1);
}
const filepath = process.argv[2];
const stringtobewritten = process.argv[3];
fs.writeFile(filepath, stringtobewritten, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    console.log(`${filepath}`);
  }
});

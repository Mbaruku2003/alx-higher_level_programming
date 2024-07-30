#!/usr/bin/node
const fs = require('fs');
function writeFile(filepath, content) {
	fs.writeFile(filepath, content, 'utf8', (err) => {
		if (err) {
			console.error(err);
		}
	}
if (process.argv.length !== 4) {
	console.error()
	process.exit(1);
}

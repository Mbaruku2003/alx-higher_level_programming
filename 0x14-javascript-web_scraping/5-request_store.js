#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
if (!url || !path) {
	console.error();
}
request(url, (error, response, body) =>
	fs.writeFile(path, response.body , 'utf8', function(err) { if (err) {
			console.error();
		}
	}));

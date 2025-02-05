#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
reques.get(url, (error, response, body) => {
	if (error) {
		console.error()
	}
	console.log('code: ', response.statusCode);
});

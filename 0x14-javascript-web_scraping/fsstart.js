#!/usr/bin/node
const fs = require('fs')
fs.unlink('trial.js', function(err) {
	if (err) throw err;
	console.log('trial.js Deleted\n')
});

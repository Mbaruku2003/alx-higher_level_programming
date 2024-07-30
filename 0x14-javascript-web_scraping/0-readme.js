const fs = require('fs');
// Get the file path from the first argenment
const filepath = process.argv[2];
if (!filepath) {
  process.exit(1);
}
// Read the file content in utf8 encoding
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading th file:', err);
  } else {
    console.log(data);
  }
});

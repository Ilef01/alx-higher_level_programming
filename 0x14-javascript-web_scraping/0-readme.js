#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];

if (!file) {
  console.error('No file provided');
}
fs.readFile(file, 'utf-8', function (error, data) {
  if (error) {
    console.error('Error reading file: ', error);
    process.exit(1);
  }
  console.log(data);
});

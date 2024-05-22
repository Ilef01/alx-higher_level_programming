#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

if (!file) {
  console.error('No file provided');
  process.exit(1);
}

if (!string) {
  console.error('No string provided');
  process.exit(1);
}

fs.writeFile(file, string, 'utf-8', function (error) {
  if (error) {
    console.error('Error writing to file: ', error);
    process.exit(1);
  }
});

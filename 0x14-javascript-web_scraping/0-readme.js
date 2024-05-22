#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];

if (!file) {
  console.error('No file provided');
  process.exit(1);
}
fs.readFile(file, 'utf-8', function (error, data) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  console.log('body', data);
});

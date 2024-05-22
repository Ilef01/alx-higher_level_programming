#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

try {
  fs.writeFileSync(file, string, 'utf-8');
} catch (error) {
  console.error('Error writing to file: ', error);
  process.exit(1);
}

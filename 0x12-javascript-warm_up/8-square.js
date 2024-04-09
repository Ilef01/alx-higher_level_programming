#!/usr/bin/node
const argv = process.argv;
const size = argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) { process.stdout.write('X'); }
    process.stdout.write('\n');
  }
}

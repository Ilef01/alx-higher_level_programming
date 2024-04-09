#!/usr/bin/node

function add (a, b) {
  console.log(Number(a) + Number(b));
}

const argv = process.argv;
const a = argv[2];
const b = argv[3];
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  add(a, b);
}

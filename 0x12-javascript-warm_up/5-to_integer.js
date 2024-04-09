#!/usr/bin/node
const { argv } = process;
const arg = argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number:', Number(arg));
}

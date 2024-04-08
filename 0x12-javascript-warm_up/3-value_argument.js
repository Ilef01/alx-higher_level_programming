#!/usr/bin/node
const { argv } = process;
if (!argv[2]) { console.log('No argument'); }
console.log(argv[2]);

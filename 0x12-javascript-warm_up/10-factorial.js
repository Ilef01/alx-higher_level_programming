#!/usr/bin/node
function factoriel (x) {
  if (x === 1 || x === 0 || isNaN(x)) {
    return (1);
  } else {
    return (Number(x) * factoriel(Number(x) - 1));
  }
}
const argv = process.argv;
const x = argv[2];
console.log(factoriel(x));

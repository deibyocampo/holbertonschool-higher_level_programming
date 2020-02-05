#!/usr/bin/node
const argum = parseInt(process.argv[2], 10);

if (isNaN(argum)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < argum; i++) {
    console.log('C is fun');
  }
}

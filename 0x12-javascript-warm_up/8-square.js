#!/usr/bin/node
const argum = parseInt(process.argv[2], 10);
const row = [];
if (isNaN(argum)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < argum; x++) {
    row.push('X');
  }
  for (let y = 0; y < argum; y++) {
    console.log(row.join(' '));
  }
}

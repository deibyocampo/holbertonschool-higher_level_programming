#!/usr/bin/node
const index = process.argv;
if (index[2] === undefined) {
  console.log('No argument');
} else {
  console.log(index[2]);
}

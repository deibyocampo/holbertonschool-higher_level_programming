#!/usr/bin/node
let index = process.argv.slice(2);
if (index < 1) {
  console.log('No argument');
} else {
  console.log(`${index}`);
}

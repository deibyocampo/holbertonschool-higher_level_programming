#!/usr/bin/node
const index = process.argv.slice(2);
if (index < 1) {
  console.log('No argument');
}
if (index !== 1) {
  console.log(`${index}`);
}

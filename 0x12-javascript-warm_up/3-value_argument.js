#!/usr/bin/node
const index = process.argv.slice(2);
if (index == '') {
  console.log('No argument');
}
else {
  console.log(index.toString());
}

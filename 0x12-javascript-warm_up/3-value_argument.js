#!/usr/bin/node
const index = process.argv.slice(2);
if (index.length < 1) { console.log('No argument'); } else { console.log(`${index}`); }

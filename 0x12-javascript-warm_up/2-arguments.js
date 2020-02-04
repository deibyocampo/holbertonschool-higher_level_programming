#!/usr/bin/node
const index = process.argv.slice(2);
if (index.length < 1) { console.log('No argument'); }

if (index.length === 1) { console.log('Argument found'); }

if (index.length >= 2) { console.log('Arguments found'); }

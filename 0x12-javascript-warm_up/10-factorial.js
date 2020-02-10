#!/usr/bin/node
const args = process.argv;

function factorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

if (isNaN(args[2])) {
  console.log('1');
} else {
  const num = factorial(parseInt(args[2], 10));
  console.log(num);
}

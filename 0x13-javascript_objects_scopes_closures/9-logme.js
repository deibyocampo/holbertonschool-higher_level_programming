#!/usr/bin/node
// prints the number of arguments already

let size = 0;
exports.logMe = function (item) {
  console.log(size + ': ' + item);
  size++;
};

#!/usr/bin/node
// in process

exports.esrever = function (list) {
  let size = list.length - 1;
  for (let i = 0; i <= size; i++) {
    const temp = list[size];
    list[size] = list[i];
    list[i] = temp;
    size--;
  }
  return (list);
};

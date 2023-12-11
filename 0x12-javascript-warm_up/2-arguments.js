#!/usr/bin/node

// Write a script that prints a message depending of the number of arguments passed:

const num = process.argv.length;
console.log(num === 2
  ? 'No argument'
  : num === 3
    ? 'Argument found'
    : 'Arguments found'
);

#!/usr/bin/node

// Write a script that prints the first argument passed to it:

const myVar = process.argv;
console.log(
  myVar[2] === undefined
    ? 'No argument'
    : myVar[2]
);

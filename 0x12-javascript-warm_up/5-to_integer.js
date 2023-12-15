#!/usr/bin/node

// Write a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:

const myVar = process.argv;
console.log(
  myVar[2] === undefined || isNaN(parseInt(myVar[2]))
    ? 'Not a number'
    : 'My number: ' + parseInt(myVar[2])
);

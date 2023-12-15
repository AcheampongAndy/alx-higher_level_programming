#!/usr/bin/node

// Write a script that prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)

const myVar = process.argv;
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(myVar[2]), parseInt(myVar[3])));

#!/usr/bin/node

// Write a script that prints two arguments passed to it, in the following format:

const myVar = process.argv;
console.log(myVar[2] + ' is ' + myVar[3]);

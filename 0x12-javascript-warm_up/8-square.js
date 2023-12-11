#!/usr/bin/node

// Write a script that prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square

const myVar = process.argv;
if (myVar[2] === undefined || Number.isNaN(parseInt(myVar[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(myVar[2]); i++) {
    let row = '';
    for (let j = 0; j < parseInt(myVar[2]); j++) {
      row += 'X';
    }
    console.log(row);
  }
}

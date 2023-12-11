#!/usr/bin/node

// Write a script that prints x times “C is fun”
// Where x is the first argument of the script
// If the first argument can’t be converted to an integer,
// print “Missing number of occurrences”

const myVar = process.argv;
if (myVar[2] === undefined || Number.isNaN(parseInt(myVar[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(myVar[2]); i++) {
    console.log('C is fun');
  }
}

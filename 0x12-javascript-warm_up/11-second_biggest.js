#!/usr/bin/node

// Write a script that searches the second biggest integer in the list of arguments.
// You can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0

function sortNumber (array) {
  const integers = array.map(Number);
  const sortedArray = [...new Set(integers)].sort((a, b) => b - a);
  return sortedArray;
}
if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  console.log(sortNumber(args)[1]);
}

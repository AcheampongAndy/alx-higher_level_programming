#!/usr/bin/node
// Write a script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively

function factorial (number) {
  if (number === 0 || number === 1 || Number.isNaN(number)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
const myVar = process.argv;
console.log(factorial(parseInt(myVar[2])));

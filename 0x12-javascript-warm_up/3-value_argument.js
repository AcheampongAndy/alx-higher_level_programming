#!/usr/bin/node

const count = process.argv.length;
console.log(count === 2 ? "No Argument": `${process.argv[2:]}`);

#!/usr/bin/node

/*
 * Write a script that imports a dictionary of occurrences by user
 * id and computes a dictionary of user ids by occurrence.
      * Your script must import dict from the file 101-data.js
      * In the new dictionary
            * A key is a number of occurrence
            * A value is the list of user ids
      * Print the new dictionary at the end
 */

const data = require('./101-data.js');
const oldDict = data.dict;
const newDict = {};
for (const [occurrence, index] of Object.entries(oldDict)) {
  if (newDict[index] === undefined) {
    newDict[index] = [occurrence];
  } else {
    newDict[index].push(occurrence);
  }
}
console.log(newDict);

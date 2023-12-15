#!/usr/bin/node

/*
 * Write a function that returns the number of occurrences in a list:
     * Prototype: exports.nbOccurences = function (list, searchElement)
 */

exports.nbOccurences = function (list, searchElement) {
  let iterate = 0;
  for (const element of list) {
    if (element === searchElement) {
      iterate += 1;
    }
  }
  return iterate;
};

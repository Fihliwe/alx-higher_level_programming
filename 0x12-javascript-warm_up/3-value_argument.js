#!/usr/bin/node
// Prints the firsr argument passed on to it

if (process.argv[2] === undefined) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}

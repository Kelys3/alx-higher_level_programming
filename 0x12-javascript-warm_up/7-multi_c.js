#!/usr/bin/node
const digits = Math.floor(Number(process.argv[2]));
if (isNaN(digits)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < digits; x++) {
    console.log('C is fun');
  }
}

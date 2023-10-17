#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let l = 0; l < size; l++) {
    let row = '';
    for (let b = 0; b < size; b++) row += 'X';
    console.log(row);
  }
}

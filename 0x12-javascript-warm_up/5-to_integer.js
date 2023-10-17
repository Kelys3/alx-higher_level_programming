#!/usr/bin/node
const digits = Math.floor(Number(process.argv[2]));
console.log(isNaN(digits) ? 'Not a number' : `My number: ${digits}`);

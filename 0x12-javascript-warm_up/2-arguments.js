#!/usr/bin/node
let i = 0;
while (process.argv[i] !== undefined) {
  i = i + 1;
}
if (i <= 2) {
  console.log('No argument');
} else if (i === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

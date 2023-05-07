#!/usr/bin/node

/**
 * a script that prints a square
 */
  const size = Math.floor(Number(process.argv[2]));
  let squareIndicator = "";
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        squareIndicator += 'X';
      }
      if (i !== size - 1) {
        squareIndicator += '\n';
      }
    }
    console.log(squareIndicator);
    
  }

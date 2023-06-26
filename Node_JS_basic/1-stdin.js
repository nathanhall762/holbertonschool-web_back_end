// 1-stdin.js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

rl.on('line', (name) => {
  if (name === '') {
    console.log('Your name is: undefined\n');
    rl.close();
  } else {
    console.log(`Your name is: ${name}`);
  }
  console.log('This important software is now closing');
  process.exit(0);
});

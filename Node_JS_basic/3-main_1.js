const countStudents = require('./3-read_file_async');

const x = countStudents('database.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });
console.log('After!');
console.log(x);
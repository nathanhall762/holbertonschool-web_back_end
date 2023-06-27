// 7.
const express = require('express');
const countStudents = require('./3-read_file_async');

const databasePath = 'database.csv';

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const studentsDict = await countStudents(databasePath);

    const studentsOutput = [];
    let totalStudents = 0;

    for (const field in studentsDict) {
      if (Object.prototype.hasOwnProperty.call(studentsDict, field)) {
        const { numStudents, names } = studentsDict[field];
        const studentList = names.join(', ');

        studentsOutput.push(`Number of students in ${field}: ${numStudents}. List: ${studentList}`);
        totalStudents += numStudents;
      }
    }

    console.log(`Number of students: ${totalStudents}`);

    res.send(`This is the list of our students\nNumber of students: ${totalStudents}\n${studentsOutput.join('\n')}`);
  } catch (error) {
    res.status(500).send(`Error: ${error.message}`);
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;

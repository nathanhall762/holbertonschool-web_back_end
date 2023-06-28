// 5.
const http = require('http');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2];

const app = http.createServer(async (req, res) => {
  const { method, url } = req;

  if (method === 'GET' && url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (method === 'GET' && url === '/students') {
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

      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${totalStudents}\n`);

      for (let i = 0; i < studentsOutput.length - 1; i += 1) {
        res.write(`${studentsOutput[i]}\n`);
      }

      if (studentsOutput.length > 0) {
        res.write(studentsOutput[studentsOutput.length - 1]);
      }
    } catch (error) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end(`This is the list of our students
Cannot load the database`);
    }

    res.end();
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;

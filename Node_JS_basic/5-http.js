// 5.
const http = require('http');
const countStudents = require('./3-read_file_async');

const databasePath = 'database.csv';

const app = http.createServer(async (req, res) => {
  const { method, url } = req;

  if (method === 'GET' && url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!\n');
  } else if (method === 'GET' && url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    try {
      const studentsDict = await countStudents(databasePath);

      const fields = Object.keys(studentsDict);
      const lastFieldIndex = fields.length - 1;

      fields.forEach((field, index) => {
        const { numStudents, names } = studentsDict[field];
        const studentList = names.join(', ');

        res.write(`Number of students in ${field}: ${numStudents}. List: ${studentList}`);

        if (index !== lastFieldIndex) {
          res.write('\n');
        }
      });
    } catch (error) {
      res.end(`Error: ${error.message}`);
    }

    res.end();
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not found\n');
  }
});

app.listen(1245);

module.exports = app;

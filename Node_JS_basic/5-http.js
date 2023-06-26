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
      await countStudents(databasePath);
    } catch (error) {
      res.end(`Error: ${error.message}`);
      return;
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

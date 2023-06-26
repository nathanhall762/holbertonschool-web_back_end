// 3.
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.trim().split('\n');
        const students = {};

        for (let i = 1; i < lines.length; i += 1) {
          const line = lines[i].trim();
          if (line !== '') {
            const [firstname, , , field] = line.split(',');

            if (!students[field]) {
              students[field] = [];
            }

            students[field].push(firstname);
          }
        }

        console.log(`Number of students: ${lines.length - 1}`);

        for (const field in students) {
          if (Object.prototype.hasOwnProperty.call(students, field)) {
            console.log(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
          }
        }

        resolve();
      }
    });
  });
}

module.exports = countStudents;

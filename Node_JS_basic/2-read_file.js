// 2.
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    const students = [];

    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line !== '') {
        const [firstname, lastname, age, field] = line.split(',');

        if (!students[field]) {
          students[field] = [];
        }

        students[field].push(firstname);
      }
    }

    console.log(`Number of students: ${lines.length - 1}`);

    for (const field in students) {
      console.log(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;

const readDatabase = require('../utils');

class StudentsController {

	static getAllStudents(req, res) {
		const student = readDatabase('../../database.csv');
		let returnString = 'This is our list of students';
		student.CS.names.sort();
		student.SWE.names.sort();
		res.send(`${returnString}\nNumber of students in CS: ${student.CS.names.length}. List: ${student.CS.names.join(', ')}\nNumber of students in SWE: ${student.SWE.names.length}. List: ${student.SWE.names.join(', ')}`);
	}

	// TODO: add method getAllStudentsByMajor
}
interface Student {
	firstName: string;
	lastName: string;
	age: number;
	location: string;
  }
  
  let student1: Student = {
	firstName: "John",
	lastName: "Doe",
	age: 25,
	location: "New York"
  };
  
  let student2: Student = {
	firstName: "Jane",
	lastName: "Doe",
	age: 22,
	location: "Los Angeles"
  };
  
  let studentsList: Student[] = [student1, student2];
  
  let table = document.createElement("table");
  
  for (let i = 0; i < studentsList.length; i++) {
	let row = table.insertRow();
	let firstNameCell = row.insertCell();
	let locationCell = row.insertCell();
	firstNameCell.innerHTML = studentsList[i].firstName;
	locationCell.innerHTML = studentsList[i].location;
  }
  
  document.body.appendChild(table);
  
interface DirectorInterface {
    workFromHome(): string;
    getCoffeeBreak(): string;
    workDirectorTasks(): string;
}

interface TeacherInterface {
    workFromHome(): string;
    getCoffeeBreak(): string;
    workTeacherTasks(): string;
}

class Director implements DirectorInterface {
    workFromHome(): string {
        return 'Working from home';
    }

    getCoffeeBreak(): string {
        return 'Getting a coffee break';
    }

    workDirectorTasks(): string {
        return 'Getting to director tasks';
    }
}

class Teacher implements TeacherInterface {
    workFromHome(): string {
        return 'Cannot work from home';
    }

    getCoffeeBreak(): string {
        return 'Cannot have a break';
    }

    workTeacherTasks(): string {
        return 'Getting to work';
    }
}

const createEmployee = (salary: number | string): Director | Teacher => {
    if (typeof salary === 'number' && salary < 500) {
        return new Teacher();
    } else {
        return new Director();
    }
}
const isDirector = (employee: Director | Teacher): employee is Director => {
    return (employee as Director).workDirectorTasks !== undefined;
}

const executeWork = (employee: Director | Teacher) => {
    if (isDirector(employee)) {
        employee.workDirectorTasks();
    } else {
        employee.workTeacherTasks();
    }
}

type Subjects = "Math" | "History";

const teachClass = (todayClass: Subjects): string => {
    if (todayClass === "Math") {
        return "Teaching Math";
    } else if (todayClass === "History") {
        return "Teaching History";
    }
}


const empl = createEmployee(200);
console.log(empl);
const work = executeWork(empl);
console.log(work);
console.log(teachClass("Math"));
const employee = createEmployee(200);
console.log(employee.workFromHome()); // prints "Cannot work from home"
console.log(employee.getCoffeeBreak()); // prints "Cannot have a break"
console.log(executeWork(employee)); // prints "Getting to work"
console.log(teachClass("Math")); // prints "Teaching Math"

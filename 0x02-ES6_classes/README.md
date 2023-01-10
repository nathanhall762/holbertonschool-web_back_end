# 0x02-ES6_classes

## How does one define a Class in JS?
 In JavaScript, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). Classes in JavaScript are created using the `class` keyword, and it typically follows the same structure as in other object-oriented programming languages.

For example, a class for creating a Person object might be defined like this:

```kotlin
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}
```

The `constructor` function is a special function that is automatically called when a new object is created from the class. In this example, the constructor sets the initial values for the name and age properties of the Person object.

Once the class is defined, it can be used to create new objects like this:

```javascript
let john = new Person('John Doe', 30);
```

And we can access the attributes:

```javascript
console.log(john.name); // "John Doe"
console.log(john.age); // 30
```

It's worth noting that the class definition creates a single shared function object which is used as the prototype for new objects, so that we do not need to re-create methods each time a new object is created.

## How does one add methods to a class in JS?
 To add methods to a class in JavaScript, you can define them inside the class definition, after the constructor. For example, you might add a method to the Person class that prints out the person's name and age:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  display() {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
  }
}
```

In this example, we added a method called `display`, which is accessible on any objects created from the class.

Methods can also be added to classes using the prototype object after the class is defined, like this:

```javascript
Person.prototype.display = function () {
  console.log(`Name: ${this.name}, Age: ${this.age}`);
};
```

Both of this way would have the same behavior, if you call the method display on the john object :

```scss
john.display() // "Name: John Doe, Age: 30"
```

It's important to note that, when you add methods to the prototype, all instances of the class will share the same function instance. This means that if you later modify the method, that change will be reflected in all instances of the class, and it can be an effective way to implement inheritance.

## Why and how does one add a static method to a class in JS?
 A static method in JavaScript is a method that is associated with the class itself, rather than with instances of the class. This means that a static method can be called on the class, without needing to first create an instance of the class.

To create a static method, you use the `static` keyword before the method name in the class definition:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  display() {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
  }
  static createPerson(name, age) {
    return new Person(name, age);
  }
}
```

In this example, we added a static method called `createPerson` which creates a new Person object and return it. And it can be used like this:

```javascript
let john = Person.createPerson('John Doe', 30);
```

Static methods are often used to create utility functions that don't need to be associated with any specific object. They can also be used to organize code in a more logical way, to create factory methods, etc.

One important thing to note, is that you cannot use the keyword `this` inside a static method, since there is no instance of the class to provide the context for the method. But you can use the class name to call other methods or variables that you defined on the class.

## How does one extend a class from another in JS?
 In JavaScript, you can use the `extends` keyword to create a new class that inherits from an existing class. This allows you to reuse the code in the existing class and extend it with additional properties and methods.

For example, you might create a new class called `Employee` that inherits from the `Person` class:

```javascript
class Employee extends Person {
  constructor(name, age, title) {
    super(name, age); // call the parent constructor
    this.title = title;
  }
  display() {
    console.log(`Name: ${this.name}, Age: ${this.age}, Title: ${this.title}`);
  }
}
```

In this example, the `Employee` class has a constructor that takes an additional `title` parameter, and it calls the `super` function to call the constructor of the parent class.
`Employee` class also has a `display` method which is the same as the `Person` class but it also display the title of the employee.

When you create an instance of the `Employee` class, it will have all the properties and methods of the `Person` class, plus any additional properties and methods that you added to the `Employee` class:

```javascript
let jane = new Employee('Jane Smith', 25, 'Manager');
jane.display();
```

It would display:

```yaml
Name: Jane Smith, Age: 25, Title: Manager
```

It's worth noting that the class inheritance in javascript is different than the class inheritance in classical OOP languages, the class `extends` keyword creates a prototype-based inheritance, which is different than the class-based one.

## What is metaprogramming and symbols?
 Metaprogramming is a programming technique where the program has the ability to manipulate or modify its own structure and behavior at runtime. In JavaScript, this can be achieved through the use of symbols, which are unique and immutable values that can be used as property keys on objects.

Symbols can be created using the `Symbol()` function, like this:

```javascript
const id = Symbol();
```

Once a symbol is created, it can be used to define properties on an object that are not enumerable, and that won't be affected by code that iterates over all properties of an object or uses the `in` operator to check for the existence of a property.

```bash
let obj = {};
obj[id] = "my-unique-value";
```

Symbols can also be used to define methods that cannot be overridden by subclasses, using the `Symbol.for()` method. The `Symbol.for()` method returns a shared symbol that can be used across multiple parts of the code. Like this:

```javascript
const mySymbol = Symbol.for('mySymbol');
class MyClass {
  [mySymbol]() {
    // my unique method
  }
}
```

In addition to symbols, JavaScript also has `getters`, `setters` and `Proxies` to perform metaprogramming. These features allows you to define logic to run whenever a property is accessed or modified, which can be used to create objects that behave like other types of objects, or to add additional functionality to existing objects.

Overall metaprogramming allows developers to add powerful functionalities to their code, making it more dynamic, but should be used with care as it also can make code harder to understand and reason about.

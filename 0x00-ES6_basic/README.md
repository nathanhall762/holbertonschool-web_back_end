# 0x00. ES6 Basics

ES6, also known as ECMAScript 6 or ECMAScript 2015, is a major update to the JavaScript programming language. It was released in 2015 and introduced many new features that have greatly improved the language and made it easier to use.

One of the most notable new features introduced in ES6 is the concept of constants. A constant is a value that cannot be re-assigned or re-declared once it has been set. This is in contrast to variables, which can be re-assigned and re-declared. Constants are useful for values that should not be changed, such as configuration settings or math constants.

Another new feature introduced in ES6 is block-scoped variables. Prior to ES6, variables in JavaScript were function-scoped, which meant that they were only accessible within the function in which they were declared. With block-scoped variables, variables are only accessible within the block of code in which they are declared, which makes it easier to manage variable scope.

Arrow functions are another new feature introduced in ES6. They are a shorthand way of writing functions and are often used in combination with other ES6 features such as default function parameters. Default function parameters allow you to specify default values for function arguments, which can be overridden if necessary.

ES6 also introduced rest and spread function parameters. Rest parameters allow you to capture an indefinite number of arguments as an array, while spread parameters allow you to expand an array into individual arguments. These features can be particularly useful when working with variadic functions or when working with arrays.

String templating is a new feature in ES6 that allows you to easily insert variables into strings. This is done using template literals, which are strings that are surrounded by backticks (\`) instead of quotes. Template literals can contain placeholders for variables, which are indicated by a dollar sign and curly braces (e.g. ${variable}).

Object creation and properties have also been improved in ES6. The object literal syntax has been enhanced to allow for more concise and expressive object creation. Additionally, ES6 introduced computed property names, which allow you to use expressions to define the keys of an object.

Finally, ES6 introduced iterators and for-of loops, which make it easier to iterate over collections of data such as arrays and objects. Iterators are objects that implement a next() method, which returns the next value in the collection. For-of loops automatically call the next() method of an iterator until there are no more values to be returned.

Overall, ES6 has introduced many new features that have greatly improved the JavaScript language and made it easier to use. Whether you are a seasoned JavaScript developer or just getting started, there is much to learn and enjoy with ES6.

## What is ES6?
ES6, also known as ECMAScript 6 or ECMAScript 2015, is a major update to the JavaScript programming language. It was released in 2015 and introduced many new features that have greatly improved the language and made it easier to use.

JavaScript is a programming language that is commonly used in web development to add interactivity to websites. It is supported by all modern web browsers and is an essential tool for web developers.

ES6 is the sixth major update to JavaScript and was the first update to the language in more than five years. It introduced many new features that were designed to make the language more powerful and easier to use. Some of these features include:

Constants: ES6 introduced the concept of constants, which are values that cannot be re-assigned or re-declared once they have been set. This is in contrast to variables, which can be re-assigned and re-declared. Constants are useful for values that should not be changed, such as configuration settings or math constants.

Block-scoped variables: Prior to ES6, variables in JavaScript were function-scoped, which meant that they were only accessible within the function in which they were declared. With block-scoped variables, variables are only accessible within the block of code in which they are declared, which makes it easier to manage variable scope.

Arrow functions: Arrow functions are a shorthand way of writing functions and are often used in combination with other ES6 features such as default function parameters. Default function parameters allow you to specify default values for function arguments, which can be overridden if necessary.

Rest and spread function parameters: ES6 introduced rest and spread function parameters, which allow you to capture an indefinite number of arguments as an array (rest parameters) or expand an array into individual arguments (spread parameters). These features can be particularly useful when working with variadic functions or when working with arrays.

String templating: String templating is a new feature in ES6 that allows you to easily insert variables into strings. This is done using template literals, which are strings that are surrounded by backticks (\`) instead of quotes. Template literals can contain placeholders for variables, which are indicated by a dollar sign and curly braces (e.g. ${variable}).

Object creation and properties: ES6 introduced enhancements to the object literal syntax, which allow for more concise and expressive object creation. Additionally, ES6 introduced computed property names, which allow you to use expressions to define the keys of an object.

Iterators and for-of loops: ES6 introduced iterators and for-of loops, which make it easier to iterate over collections of data such as arrays and objects. Iterators are objects that implement a next() method, which returns the next value in the collection. For-of loops automatically call the next() method of an iterator until there are no more values to be returned.

Overall, ES6 has introduced many new features that have greatly improved the JavaScript language and made it easier to use. Whether you are a seasoned JavaScript developer or just getting started, there is much to learn and enjoy with ES6.

## What is the difference between a constant and a variable in JavaScript?
In JavaScript, a constant is a value that cannot be re-assigned or re-declared once it has been set. This is in contrast to variables, which can be re-assigned and re-declared. Constants were introduced in ES6 (ECMAScript 6), which is the latest version of the JavaScript language.

To declare a constant in JavaScript, you use the const keyword followed by the name of the constant and its value. For example:
 ```
const PI = 3.14;

```

Once you have declared a constant, you cannot re-assign or re-declare it. If you try to do so, you will get a syntax error. For example:
```
const PI = 3.14;
PI = 3.14159;  // This will cause a syntax error
const PI = 3.14159;  // This will also cause a syntax error

```

On the other hand, variables can be re-assigned and re-declared as needed. To declare a variable in JavaScript, you use the var keyword followed by the name of the variable and its value. For example:
```
var x = 10;
x = 20;  // This is allowed
var x = 20;  // This is also allowed

```

In addition to const and var, there is also the let keyword, which is similar to var but is block-scoped rather than function-scoped. This means that a let variable is only accessible within the block of code in which it is declared. For example:
```
if (true) {
  let x = 10;
  // x is accessible within this block of code
}
// x is not accessible outside of the block of code

```

Block-scoped variables are a useful feature in JavaScript because they make it easier to manage variable scope. Prior to the introduction of const and let, all variables in JavaScript were function-scoped, which means that they were only accessible within the function in which they were declared. This can lead to problems when trying to manage large and complex codebases, as it can be difficult to keep track of which variables are accessible in which parts of the code.

In general, it is recommended to use const for values that should not be changed and let for values that will be modified. var should be avoided whenever possible, as it has been superseded by const and let.

In summary, the main difference between a constant and a variable in JavaScript is that a constant cannot be re-assigned or re-declared, while a variable can be. Constants are useful for values that should not be changed, such as configuration settings or math constants, while variables are useful for values that will be modified.

## What are arrow functions and some function parameters that are default to them?
Arrow functions are a shorthand way of writing functions in JavaScript. They were introduced in ES6 (ECMAScript 6), which is the latest version of the JavaScript language.

Arrow functions are often used in combination with default function parameters, which allow you to specify default values for function arguments. Default function parameters are a feature of ES6 that make it easier to write functions that have optional arguments.

To define an arrow function with default function parameters, you use the following syntax:
```
const functionName = (arg1 = defaultValue1, arg2 = defaultValue2, ...) => {
  // function body
};

```

For example, consider the following function that calculates the area of a rectangle:
```
const calculateRectangleArea = (width = 1, height = 1) => {
  return width * height;
};

```

In this example, the calculateRectangleArea function has two default function parameters: width and height. If these arguments are not provided when the function is called, their default values of 1 will be used. For example:
```
calculateRectangleArea();  // Returns 1 (1 * 1)
calculateRectangleArea(2);  // Returns 2 (2 * 1)
calculateRectangleArea(2, 3);  // Returns 6 (2 * 3)

```

As you can see, default function parameters make it easy to write functions that have optional arguments. This can be particularly useful when you want to provide default values for arguments that may not always be needed.

Arrow functions also have a shorter syntax that can be used when the function consists of a single expression:
```
const functionName = (arg1, arg2, ...) => expression;

```

For example, consider the following arrow function that calculates the square of a number:
```
const square = x => x * x;

```

In this example, the square function has a single argument (x) and consists of a single expression (x * x). This function can be called as follows:
```
square(2);  // Returns 4
square(3);  // Returns 9

```

Overall, arrow functions are a useful feature in JavaScript that make it easier to write concise and expressive functions. When used in combination with default function parameters, they can make it easy to write functions that have optional arguments.

## What are the rest and spread function parameters?
Rest and spread function parameters are features of JavaScript that were introduced in ES6 (ECMAScript 6), which is the latest version of the language. They allow you to capture an indefinite number of arguments as an array (rest parameters) or expand an array into individual arguments (spread parameters).

Rest parameters are indicated by three dots (...) followed by the name of the parameter. They allow you to capture an indefinite number of arguments as an array. For example:
```
function sum(...numbers) {
  let total = 0;
  for (const number of numbers) {
    total += number;
  }
  return total;
}

console.log(sum(1, 2, 3, 4, 5));  // Outputs 15

```

In this example, the sum function has a rest parameter called numbers, which captures all of the arguments passed to the function as an array. The function then iterates over the numbers array and calculates the sum of all of the elements.

Spread parameters, on the other hand, are indicated by three dots (...) followed by an array. They allow you to expand an array into individual arguments. For example:
```
function sum(x, y, z) {
  return x + y + z;
}

const numbers = [1, 2, 3];
console.log(sum(...numbers));  // Outputs 6

```

In this example, the sum function has three arguments: x, y, and z. The numbers array is expanded into individual arguments using the spread operator, which allows the sum function to be called with the elements of the numbers array as arguments.

Rest and spread function parameters are useful features in JavaScript because they allow you to work with variadic functions (functions that accept an indefinite number of arguments) and make it easier to manipulate arrays. They can be particularly useful when working with higher-order functions (functions that operate on other functions) or when working with functional programming techniques.

Overall, rest and spread function parameters are powerful features of JavaScript that allow you to capture and expand an indefinite number of arguments. They can be particularly useful when working with variadic functions or when manipulating arrays.

## What is string templating in ES6?
String templating is a feature of JavaScript that was introduced in ES6 (ECMAScript 6), which is the latest version of the language. It allows you to easily insert variables into strings and create templates for generating strings.

To use string templating, you use template literals, which are strings that are surrounded by backticks (`) instead of quotes. Template literals can contain placeholders for variables, which are indicated by a dollar sign and curly braces (e.g. ${variable}).

For example, consider the following code that uses string concatenation to create a string:
```
const name = 'John';
const message = 'Hello, ' + name + '!';
console.log(message);  // Outputs 'Hello, John!'

```

This code works, but it can be difficult to read and is prone to errors. Instead, you can use string templating to create the same string as follows:
```
const name = 'John';
const message = `Hello, ${name}!`;
console.log(message);  // Outputs 'Hello, John!'

```

As you can see, string templating makes it easy to insert variables into strings and makes the code easier to read.

In addition to inserting variables into strings, you can also use string templating to create templates for generating strings. For example, consider the following code that generates a list of names:
```
const names = ['John', 'Jane', 'Mike'];
let list = '<ul>';
for (const name of names) {
  list += `<li>${name}</li>`;
}
list

```

## What is object creation and what are some of their properties?
Object creation and properties are fundamental concepts in JavaScript, and ES6 (ECMAScript 6), the latest version of the language, introduces several enhancements that make it easier to create and work with objects.

To create an object in JavaScript, you use the Object constructor or object literal syntax. The Object constructor is a function that returns a new object when called. For example:
```
const obj = new Object();

```

Alternatively, you can use object literal syntax to create an object. Object literal syntax is a shorthand way of creating an object by specifying its properties and values as a list of key-value pairs. For example:
```
const obj = {
  key1: value1,
  key2: value2,
  ...
};

```

In ES6, object literal syntax has been enhanced to allow for more concise and expressive object creation. For example, you can now use computed property names to define the keys of an object using expressions. Computed property names are indicated by square brackets ([]). For example:
```
const key = 'name';
const obj = {
  [key]: 'John',  // Computed property name
  age: 30
};

```

In this example, the key variable is used as the key for the name property of the obj object.

In addition to computed property names, ES6 also introduced shorthand properties, which allow you to omit the key when the key is the same as the variable name. For example:
```
const name = 'John';
const age = 30;
const obj = { name, age };

```

In this example, the name and age variables are used as the keys and values for the name and age properties of the obj object, respectively.

Overall, ES6 introduces several enhancements to object creation and properties that make it easier to create and work with objects. These enhancements include computed property names and shorthand properties, which allow you to create more concise and expressive objects.

## What are iterators and for-of loops in JavaScript?
Iterators and for-of loops are features of JavaScript that were introduced in ES6 (ECMAScript 6), which is the latest version of the language. They allow you to iterate over the elements of an object and perform a specific action for each element.

An iterator is an object that defines a method called next, which returns the next element in the object and a boolean value indicating whether the iterator is finished. To create an iterator, you need to define an object with a next method. For example:
```
const iterator = {
  arr: [1, 2, 3],
  next() {
    return {
      value: this.arr.shift(),
      done: this.arr.length === 0
    };
  }
};

```

In this example, the iterator object has an arr property that contains an array of numbers and a next method that returns the first element of the arr array and a boolean value indicating whether the iterator is finished.

To use an iterator, you can call the next method repeatedly until the iterator is finished. For example:
```
let result = iterator.next();
while (!result.done) {
  console.log(result.value);
  result = iterator.next();
}

```

This code will output the elements of the arr array one at a time until the iterator is finished.

For-of loops are a simpler way of iterating over the elements of an object using an iterator. To use a for-of loop, you use the following syntax:
```
for (const element of object) {
  // code to be executed for each element
}

```

For example, you can use a for-of loop to iterate over the elements of the iterator object as follows:
```
for (const element of iterator) {
  console.log(element);
}

```

This code will output the elements of the arr array one at a time, just like the previous example.

Iterators and for-of loops are useful features in JavaScript because they allow you to easily iterate over the elements of an object and perform a specific action for each element. They can be particularly useful when working with arrays, strings, and other objects that have a finite number of elements.

Overall, iterators and for-of loops are powerful features of JavaScript that allow you to iterate over the elements of an object and perform a specific action for each element. They can be particularly useful when working with arrays, strings, and other iterable objects.


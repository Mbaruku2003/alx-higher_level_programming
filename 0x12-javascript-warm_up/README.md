introduction to javascript
we use console.log to print an  output
we use const to initalise a variale that does not change.
process is a global object that can be accesed by any module requiring it.
process is an instance of EventEmmiter.
	2-arguenments.js
	--.length--
used to find the length of a string
it starts counting from 1
if passed to an array, it finds the number of elements of the array
if passed to a string it finds the number of letters in the string however, an empty string returns zero.
it returns the number of keys in an object/dictionary
we used === because this forces for strict equality
== is used in matters of type coersion where there need not be the specific type but the type can be converted to the right type for comparison
	3-value_argument.js
we can use process.argv[index]
we can use it to test wheather a certain index is present
undefined is used to test for falsyness it occurs when a variable has no value  but has been declared
undefined is also given out when a function does not hav a return value
	5-to_integer.js
isNaN() is used to check wheather  aparameter is a string that can be changed to an integer
parseInt() is used to turn a value that is a string to an int
undefined is used to test wheather an arguenment existed
	8-square.js
.repeat() is used to repeat something other number of times
	9-add.js
we used Number which returns NaN when not defined
we first defined the function add and initialised a variable c that will add the two parameters
outside the function we called the function to work on the arguenments turned to numbers
	10-factorial.js
i learned that in recursion we call the function in itself
recursion must have a basecase
	11-second_biggest.js
.slice(start, end) is used to reprictae a copy of the array and does not modify the original list
.map creates a copy of the original lst with all elements changed e.g const doubledNumbers = numbers.map((num) => num * 2)

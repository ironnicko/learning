// Wass up

console.log("Hello");

console.log("Kill you")

let a;//let is for initializing

console.log(a)


a = 87;

a = "Poopy pants"

console.log(a);

const gg = 885;

console.log(gg);


console.log("Gigi", "Hadid");


let first, second, third, mix;

first = 1;
second = 2;
third = 3;
mix = [first, second, third];
console.log(mix);
console.log("wassup", "lessgedid", 24);

// find the length of a string

console.log(4 === 2*2);

let a = "nikhil";

console.log(a.length)// a function to find the length of the item

// string slicing

const a = "Nikhil";
console.log(a[3]);

// string functions

console.log("GG man".toUpperCase());
console.log("HEY".toLowerCase());
console.log("man".endsWith("n"));
const gg="Game Over";//can't be changed once declared

//"var" a is global scope while "let" is for declaration inside the scope

// Dictionaries are objects in JS
var person = {
	name: "Nikhil",
	age: 17
};
let name1 = window.prompt("Enter your name");
person.name = name1;
console.log(person.name);
// or you can use person["name"]

var array = ["one", 2];
array[0] = 1;
console.log(array, array.length);

//FUNCTIONS

function greet(name, lastname){
	console.log(name, lastname);
}
//greet("Nikhil", "Ivannan");

function square(number){
	return number**2;
}
console.log(square(2));

//IF-ELSE loops which i figured out by myself

let i=0;

if (i<10){
  console.log(i);
  i++;
}
  else{
    console.log(i**2);
  }

//WHILE loops again by moi

while(i<10){
  console.log(i);
  i++;
}

//samething in FOR loop by moi

for (;i<10;){
  console.log(i);
}

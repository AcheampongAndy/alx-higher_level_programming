#!/usr/bin/node

let num1;
let num2;

function add(num1, num2){
	let answer = num1 + num2;
	console.log(answer);
}

add(Math.floor(Number(process.argv[2])), Math.floor(Number(process.argv[3])));

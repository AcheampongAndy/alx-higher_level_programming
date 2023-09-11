#!/usr/bin/node

const count = process.argv[2];
if (isNaN(count)){
	console.log("Missing size");
}else{
	for (let i = 0; i < count; i++){
		let row = "";
		for(let i = 0; i < count; i++) row += "x";
			console.log(row);
	}
}

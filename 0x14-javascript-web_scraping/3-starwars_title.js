#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const episode = process.argv[2];

request(url + episode, function(erorr, response, body) {
	if (error) {
		console.log(error);
	} else if (response.statusCode === 200){
		const jsonResponse = JSON.parse(body);
		console.log(jsonResponse.title);
	} else {
		console.log('Error code: ' + response.statusCode);
	}
});

#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const API_URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(API_URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.error('Error code:', response.statusCode);
  }
});

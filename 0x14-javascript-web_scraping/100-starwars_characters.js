#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + movieId, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  for (const c of characters) {
    request.get(c, function (charErr, charRes, charBody) {
      if (charErr) {
        console.log(charErr);
      }
      const characterInfo = JSON.parse(charBody);
      console.log(characterInfo.name);
    });
  }
});

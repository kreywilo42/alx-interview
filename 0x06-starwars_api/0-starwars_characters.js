#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(url, (err, res, body) => {
  if (err) return err;
  character(JSON.parse(body).characters, 0);
});

const character = (characters, index) => {
  request(characters[index], (err, res, body) => {
    if (err) return err;
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      character(characters, index + 1);
    }
  });
};

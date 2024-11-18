#!/usr/bin/node

const request = require('request');

function fetchCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          const characterData = JSON.parse(body);
          resolve(characterData);
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
}


async function getCharacters(movieId) {
  try {
    const filmUrl = `https://swapi.dev/api/films/${movieId}`;
    request(filmUrl, async (error, response, body) => {
        if(error){
            console.error("Error:", error);
            return;
        }
        const filmData = JSON.parse(body);
        for (const characterUrl of filmData.characters) {
            try {
                const characterData = await fetchCharacterName(characterUrl);
                console.log(characterData.name);
            } catch(err) {
                console.log("Character fetch error:", error);
            }
        }
    });
  } catch (error) {
    console.error("Error:", error);
  }
}



const movieId = process.argv[2];
if (!movieId) {
  console.error("Please provide a movie ID.");
} else {
  getCharacters(movieId);
}

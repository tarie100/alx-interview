#!/usr/bin/node
const request = require('request');

// Function to fetch characters of a Star Wars movie
function fetchMovieCharacters(movieId) {
    // URL for fetching movie details
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

    // Making a GET request to fetch movie details
    request(movieUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }
        // Parsing JSON response
        const movieData = JSON.parse(body);
        // Fetching characters list
        const charactersList = movieData.characters;

        // Array to hold character names
        const characterNames = [];

        // Fetching character details and pushing names into array
        const fetchCharacterDetails = (characterUrl, callback) => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                    return;
                }
                const characterData = JSON.parse(body);
                characterNames.push(characterData.name);
                callback();
            });
        };

        // Fetching character details in parallel
        const fetchPromises = charactersList.map(characterUrl => {
            return new Promise((resolve) => {
                fetchCharacterDetails(characterUrl, resolve);
            });
        });

        // Once all character details are fetched, print the names
        Promise.all(fetchPromises).then(() => {
            characterNames.forEach((name, index) => {
                console.log(name);
            });
        });
    });
}

// Usage: Pass the movie ID as the first argument
const movieId = process.argv[2]; // Taking movie ID from command line argument
fetchMovieCharacters(movieId);


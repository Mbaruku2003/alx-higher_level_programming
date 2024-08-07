#!/usr/bin/env node
// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.get(url, function(data) {
        const movies = data.results;
        movies.forEach(function(movie) {
            const listitems = $('<li></li>').text(movie.title);
            $('#list_movies').append(listitems);
        });

        });
    })
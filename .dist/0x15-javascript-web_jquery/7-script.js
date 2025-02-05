#!/usr/bin/env node
// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.get(url, function(data) {
        const charactername = data.name;
        $('#character').text(charactername);
    });
});

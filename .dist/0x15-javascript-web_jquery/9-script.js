#!/usr/bin/env node
// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function(data) {
        const helloTranslation = data.hello;
        $('#hello').text(helloTranslation);
    });
});
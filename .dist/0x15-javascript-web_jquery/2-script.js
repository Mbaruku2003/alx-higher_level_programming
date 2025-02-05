#!/usr/bin/env node
// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    // Set up a click event handler for the <div>
    $('#red_header').click(function() {
        $('header').css('color', '#FF0000');
    });
});
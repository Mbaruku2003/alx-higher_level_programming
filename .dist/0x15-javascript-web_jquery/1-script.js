#!/usr/bin/node

// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    // select the <header> element and update its text color to red
    $('header').css('color', '#FF0000');
})
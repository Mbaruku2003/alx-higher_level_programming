#!/usr/bin/env node
// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    $('update_header').click(function() {
        $('header').text('New Header!!!');
    });
});
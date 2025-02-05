#!/usr/bin/env node
// ensure the DOM is fully loaded before running the script
$(document).ready(function() {
    //Create a new <li> element with the text "item"
    $('DIV#add_item').click(function() {
        const theItem = $('<li>Item</li>');
        $('UL.my_list').append(theItem);
    });
});
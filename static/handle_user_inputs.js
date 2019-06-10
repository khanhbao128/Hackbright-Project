
"use strict";



function showList() {
    console.log('List of Clinics in `response`:')


}


function handleUserInputs(response) {
  // evt.preventDefault();

    const userInputs = {
        'location': $('#location').val(),

    $.post('/get-state-city', userInputs, showList);

};

// $.post('/get-state-city', userInputs, showUserInputs);


$('#user_input_form').on('submit', handleUserInputs);


// Creating a table using Ajax, JS

$(function() {
    $.each(response, function(i, item) {
        const $tr = $('<tr>').append(
            $('<td>').text(item.r),
            $('<td>').text(item.content),
            $('<td>').text(item.UID)
        ); //.appendTo('#records_table');
        console.log($tr.wrap('<p>').html());
    });
});








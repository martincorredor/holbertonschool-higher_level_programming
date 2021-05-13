//Toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
//Using JQuery API
$('#toggle_header').click(function() {
    $('header').toggleClass('red green');
});
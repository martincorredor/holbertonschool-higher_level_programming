//Updates the text of the <header> element to "New header!!"
//when the user clicks on DIV#update_header
$('#update_header').click(function () {
    $('HEADER').replaceWith('New Header!!!');
});

//Adds a <li> element to a list when the user clicks on the tag DIV#add_item
//The new element is <li>Item</li>
//The new element must be added to UL.my_list
$('#add_item').click(function () {
    $('ul.my.list').append($('<li></li>').text('Item'));
});

src="https://code.jquery.com/jquery-3.2.1.min.js"
id="add_item"
$('#add_item').click(function() {
    const newItem = $('<li>').text('Item');
    $('ul.my_list').append(newItem);
});
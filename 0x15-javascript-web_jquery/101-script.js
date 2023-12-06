src="https://code.jquery.com/jquery-3.2.1.min.js"
$(document).ready(function() {
    $('#add_item').click(function() {
        const newItem = $('<li>').text('Item');
        $('ul.my_list').append(newItem);
    });
    $('#remove_item').click(function() {
        $('ul.my_list li:last-child').remove();
    });
    $('#clear_list').click(function() {
        $('ul.my_list').empty();
    });
});





src="https://code.jquery.com/jquery-3.2.1.min.js"
$(document).ready(function() {
$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    type: "GET",
    dataType: "json",
})

.done(function(data) {
    $('#hello').text(data.hello);
})
.fail(function(xhr, status, errorThrown) {
    alert("Sorry, there was a problem!");
    console.log(`Error: ${errorThrown}`);
    console.log(`Status: ${status}`);
    console.dir(xhr);
})
.always(function(xhr, status) {
    alert("The request is complete!");
})
});


 
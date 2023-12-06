src="https://code.jquery.com/jquery-3.2.1.min.js"
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    type: "GET",
    dataType: "json",
})
.done(function(data) {
    $('#character').text(data.name);
})
.fail(function(xhr, status, errorThrown) {
    alert("Sorry, there was a problem!");
    console.log("Error: " + errorThrown);
    console.log("Status: " + status);
    console.dir(xhr);
})
.always(function(xhr, status) {
    alert("The request is complete!");
});

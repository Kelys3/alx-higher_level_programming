src="https://code.jquery.com/jquery-3.2.1.min.js"
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    type: "GET",
    dataType: "json",
})
.done(function(data) {
    data.results.forEach(function(movie) {
        $('#list_movies').append(`<li>${movie.title}</li>`);
    });
})
.fail(function(xhr, status, errorThrown) {
    alert("Sorry, there was a problem!");
    console.log(`Error: ${errorThrown}`);
    console.log(`Status: ${status}`);
    console.dir(xhr);
})
.always(function(xhr, status) {
    alert("The request is complete!");
});

 
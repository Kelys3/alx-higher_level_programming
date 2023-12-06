$(document).ready(function() {
    $('#btn_translate').click(function() {
        const languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://hellosalut.stefanbohacek.dev/?',
            data: { lang: languageCode },
            type: 'GET',
            dataType: 'json'
        })
        .done(function(data) {
            $('#hello').text(data.hello);
        })
        .fail(function(xhr, status, error) {
            console.error(`Error: ${error}`);
        });
    });
});
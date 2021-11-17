
function save_city(e) {

    let params = new URLSearchParams(document.location.search);
    var cityId = params.get("id");

    e.preventDefault();
    $.ajax({
        data: JSON.stringify({
            // city: $("#cityname").text(),
            id: cityId,
        }),
        type: 'POST',
        url: '/save_city',
        contentType: 'application/json',
        success: function (data) {
            console.log(data)
            if (data.error) {
                alert(data.error);
            }
            else {
                $("#save_city").css('display', 'None')
                $("#unsave_city").css('display', 'block')

                $('#successMessage').text('Saved');
                $("#successMessage").css('display', 'block');
                if ($("#successMessage").hasClass('alert-danger')) {
                    $("#successMessage").removeClass('alert-danger')
                }
                $("#successMessage").addClass('alert-primary')
            }
        }

    })
};

function unsave_city(e) {

    let params = new URLSearchParams(document.location.search);
    var cityId = params.get("id");

    e.preventDefault();
    $.ajax({
        data: JSON.stringify({
            // city: $("#cityname").text(),
            id: cityId,
        }),
        type: 'POST',
        url: '/unsave_city',
        contentType: 'application/json',

        success: function (data) {
            console.log(data)
            if (data.error) {
                alert(data.error);
            }
            else {
                $("#unsave_city").css('display', 'None')
                $("#save_city").css('display', 'block')
                $('#successMessage').text('Removed');
                $("#successMessage").css('display', 'block');
                if ($("#successMessage").hasClass('alert-primary')) {
                    $("#successMessage").removeClass('alert-primary')
                }
                $("#successMessage").addClass('alert-danger')
            }
        }

    })
};

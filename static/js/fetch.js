$(document).ready(function () {

    // filter city
    $('.searchresults').css('display', 'none');
    $('#cityInput').keyup(filterCity);

    // If query is provided - linked from account.html
    let params = new URLSearchParams(document.location.search);
    var cityId = params.get("id");
    var cityName = params.get("name");

    if (cityId !== null) {

        $.ajax({
            data: JSON.stringify({
                id: cityId,
                name: cityName,
            }),
            type: 'POST',
            url: '/fetch',
            contentType: 'application/json',
            success: function (data) {
                if (data.error) {
                    alert(data.error);
                }
                else {
                    var template = $("#result_template").html()
                    var html = Mustache.to_html(template, data);
                    $("#result").html(html);

                    // save button
                    console.log('cityId', cityId, 'cityName', cityName)
                    $("#save_city").submit(save_city);
                    // unsave button
                    $("#unsave_city").submit(unsave_city);
                };

                if (data.session) {
                    if (data.saved == true) {
                        $("#save_city").css('display', 'None');
                    }
                    else {
                        $("#unsave_city").css('display', 'None');
                    }
                }
                else {
                    $("#save_city").css('display', 'None');
                    $("#unsave_city").css('display', 'None');
                    $('#successMessage').text('Login to save');
                    if ($("#successMessage").hasClass('alert-danger')) {
                        $("#successMessage").removeClass('alert-danger')
                    }
                    $("#successMessage").addClass('alert-primary')
                    $("#successMessage").css('display', 'block');
                }

            }
        });
    }

    //By default, submit button is disabled
    // $("#city_submit").prop('disabled', true);

    // $("#city").keyup(() => {
    //     if ($("#city").val().length > 0) {
    //         $("#city_submit").prop('disabled', false);
    //     }
    //     else {
    //         $("#city_submit").prop('disabled', true);
    //     }
    // })

    // $("form").submit(function (e) {
    //     e.preventDefault();

    //     $.ajax({
    //         data: JSON.stringify({
    //             city: $("#city").val(),
    //         }),
    //         type: 'POST',
    //         url: '/fetch',
    //         contentType: 'application/json',
    //         success: function (data) {
    //             if (data.error) {
    //                 alert(data.error);
    //             }
    //             else {
    //                 var template = $("#result_template").html()
    //                 var html = Mustache.to_html(template, data);
    //                 $("#result").html(html);
    //                 $("#city").val('');
    //                 $("#city_submit").prop('disabled', true);

    //                 // unsave button
    //                 $("#unsave_city").submit(unsave_city);

    //                 // save button
    //                 $("#save_city").submit(save_city);

    //                 if (data.session) {
    //                     if (data.saved == true) {
    //                         $("#save_city").css('display', 'None');
    //                     }
    //                     else {
    //                         $("#unsave_city").css('display', 'None');
    //                     }
    //                 }
    //                 else {
    //                     $("#save_city").css('display', 'None');
    //                     $("#unsave_city").css('display', 'None');
    //                     $('#successMessage').text('Login to save');
    //                     if ($("#successMessage").hasClass('alert-danger')) {
    //                         $("#successMessage").removeClass('alert-danger')
    //                     }
    //                     $("#successMessage").addClass('alert-primary')
    //                     $("#successMessage").css('display', 'block');
    //                 }

    //             }
    //         }

    //     });
    // });
});

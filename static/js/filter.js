function filterCity() {

    var inp, filter, ul, li, i, a, txtValue;
    inp = $('#cityInput').val();
    filter = inp.toUpperCase();
    ul = document.getElementById("myUL");

    if (inp.length > 0) {

        $.ajax({
            contentType: 'application/json',
            type: 'POST',
            url: "/filter_cities",
            data:
                JSON.stringify({
                    city: filter,
                }),
            success: function (data) {
                // remove
                ul.innerHTML = '';
                // add
                for (i = 0; i < data.length; i++) {

                    li = document.createElement("li");
                    a = document.createElement("a");
                    a.setAttribute("id", data[i]['id'])
                    a.setAttribute("href", `/?name=${data[i]['name']}&id=${data[i]['id']}`)
                    a.innerHTML = `${data[i]['name']}, ${data[i]['state']}, ${data[i]['country']}`;
                    li.appendChild(a);
                    ul.appendChild(li);
                    $('.searchresults').css('display', 'block');
                }
            }

        });

    }
    else {
        ul.innerHTML = '';
        $('.searchresults').css('display', 'none')
    }
};

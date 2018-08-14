// function send_with_ajax(data, url, func,type="POST") {
//     console.log(url);
//     $.ajax({
//         url: url,
//         data: data,
//         type: type,
//         dataType: 'text',
//         success: func,
//         error: function () {
//             console.log("error")
//         }
//     });
//
// }


var checked = {};


$('#orderBy').change(function () {
    checked["orderby"] = this.value;
    send_with_ajax(checked,url,function (response) {
            jQuery("main").empty();
            jQuery("main").html(response);
            if (data["orderby"]) {
                $('#orderBy').val(data["orderby"]);
                delete checked["orderby"];
            }
        });

    console.log("DADADADADAD");
});
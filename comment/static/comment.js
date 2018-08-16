$(document).on("submit", "#addComment", function (event) {
    event.preventDefault();
    console.log(event.target.attributes.action.value);
    var data = $(event.target).serializeArray();
    var some = data[3].value.replace(/\s\s+/g, ' ');

    if (data[3].value !== "" && some !== " "){


    send_with_ajax(data, "/comments/add/" + event.target.attributes.action.value, function (response) {
        $("#commentText").empty();
        // document.getElementById("#commentText").innerHTML = "";
        // $(".comments-section").append(response);
    });
    }
    else{
        console.error("Попытка отправить пустую форму или кучу пробелов");
    }

});

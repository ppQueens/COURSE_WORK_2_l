$(document).on("submit", "#addComment", function (event) {
    event.preventDefault();
    console.log(event.target.attributes.action.value);
    send_with_ajax($(event.target).serializeArray(), "/comments/add/" + event.target.attributes.action.value, function (response) {
        $("commentText").val("");
        $(".comments-section").append(response);
    });

});

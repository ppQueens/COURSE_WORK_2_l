//CART
$(document).on("click", function (event) {
    if ($(event.target).hasClass("modal-backdrop")) {
        $("#cartModal").modal("hide");
    }
});


$(document).on("change", ".itemQuant", function (event) {
    $(event.target).prop("disabled", true);
    var data = {
        "csrfmiddlewaretoken": csrftoken,
        "quantity": event.target.value,
        "update": "False",
    };
    send_with_ajax(data, $(event.target.parentNode).data("url"), function (response) {
        var $container = jQuery(".cart-content");

        $container.html(response);
        $(event.target).prop("disabled", false);
        // $("#cartModal").modal();

    });

});

$(document).on("submit", ".cartRemove", function (event) {
    event.preventDefault();
    console.log("REMOVE");
    send_with_ajax($(event.target).serializeArray(), event.target.action, function (response) {
        $(event.target.parentNode).remove();
        $(".full_amount").html(response);
    });
    console.log(event.target.attributes.action.nodeValue);
});

$(document).on("click", "a[href='/cart/show/']", function (event) {

    $(this).attr("href", "javascript:;");

    event.preventDefault();
    send_with_ajax("", "/cart/show/", function (response) {
        var $container = $(".cart-content");
        $container.html(response);

        // if (!$("exampleModalLong").data('bs.modal')) {
        $("#cartModal").modal();

        // }

    }, "GET");

});

$(document).on('hide.bs.modal', '#cartModal', function () {
    console.log("HELLO");
    $("a[href='javascript:;']").attr("href", "/cart/show/");
});
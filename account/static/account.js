$(document).on("submit", "#login_form", function (e) {
    e.preventDefault();
    send_with_ajax($(this).serializeArray(), "/account/login/", function (response, status, xhr) {
        if (xhr.getResponseHeader("Content-Type") !== "text") {

            $(".userbar").html(response);
        }
        else {

            $this = $(".from-server");
            $this.popover({
                content: response,
                delay: {"show": 0, "hide": 3000},
                template: '<div class="popover" role="tooltip"><div class="arrow"></div><h3 class="popover-header"></h3><div class="popover-body rgrwgrw"></div></div>',
            }).popover("toggle");

            setTimeout($this.popover("toggle"), 5000);
        }


    });

});

$(document).on("click", "#logout", function (e)  {
    e.preventDefault();
    send_with_ajax("", "/account/logout/", function (response) {
        $(".userbar").html(response);
    }, "GET");

});

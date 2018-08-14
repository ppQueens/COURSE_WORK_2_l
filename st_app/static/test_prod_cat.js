jQuery(function ($) {

    //
    if (location.href.includes('fitering')){

    var url_params_values = (location.href.split("filtering=1")[1]).split("&").slice(1);
    console.log(url_params_values);
    jQuery.each((url_params_values), function (key, value) {
        var par_val = value.split("=");
        $(".dropdown_layered_nav_"+par_val[0].split("_")[1]).val(par_val[1]);
         console.log(par_val[1]);

    });
    }

//     jQuery('.dropdown_product_cat').change(function () {
//         if (jQuery(this).val() != '') {
//             var this_page = '';
//             var home_url = 'localhost:8000';
//             if (home_url.indexOf('?') > 0) {
//                 this_page = home_url + '&product_cat=' + jQuery(this).val();
//             } else {
//                 this_page = home_url + '?product_cat=' + jQuery(this).val();
//             }
//             location.href = this_page;
//         }
//
//     });

    var class_filter = [
        'series', 'frequency', 'screen-mode', 'socket', 'chipset', 'memory-socket', 'max-ram-gb',
        'socket-type', 'cores', 'threads', 'cache', 'ram-type', 'ram-capacity', 'channel-kit',
        'hdd-capacity', 'ram-voltage', 'hdd-speed', 'ssd-capacity', 'form-factor', 'read-speed', 'write-speed',
        'ssd-height', 'gpu-chip', ',memory-size', 'memory-type', 'gpu-interface', 'smps-power', 'smps-pci-express',
        'sata-power-connector', 'modular', 'energy-efficient', 'screen-size', 'resolution', 'hdmi', 'brightness',
        'contrast-ratio', 'color', 'ytype', 'mechanical-keyboard', 'maximum-dpi', 'motherboard-compatibility',
        'brand'
    ];

    jQuery.each(class_filter, function (key, value) {
        var dropd = '.dropdown_layered_nav_' ;
        jQuery(dropd + value).change(function () {
            var is_filter = '?filtering=1';
            var everywhere = 'filter_';
            var rep = '&'+everywhere+value+'=(\\w+[^&?]+\\w+)';
            var slug = jQuery(this).val();

            var e_v = '&'.concat(everywhere,value);
            if (slug == "any") {
                var href = location.href.replace(new RegExp(rep), "");
                if(!(href.match(/[0-9][&][a-z]/) != null)) {
                    console.log("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZz");
                    href = href.replace(new RegExp('\\?(.*)[0-9]'), "");
                }
                location.href = href;
                return;
                //return;
                //jQuery(this).


            }
            //"составить выражение на отлов строки ?orderby=chtoto? "// требуется для перемещения строки в конец
            //orderby всегда вконце
            var re_order = "\\?&[\\w]+=[\\w-]+";
            var t = location.href.match(new RegExp(re_order),"");

            if (!(location.href.includes(is_filter))) { //indexOf(is_filter) > 0
                if(!(location.href.includes("?&orderby")))
                    location.href += is_filter + e_v + '=' + slug;
                else{

                    location.href = is_filter+e_v + '=' + slug + t;
                }
            }
            else {

                if (!(location.href.includes(e_v))){
                    location.href = location.href.replace(new RegExp(re_order),"") +e_v + '=' + slug + t[0];

                }

                else {

                    console.log(rep);
                    var re = new RegExp(rep);
                    location.href = location.href.replace(re, e_v.concat('=',slug));

                }


            }



        });

    });
    var or = "orderby";
    jQuery("."+or).change(function () {
            var sel = jQuery(this).val();

            if (location.href.includes(or)) {
                //составить регулярное выражение для отлова ?orderby=chtoto(конец строки)
              var rep = "\\^?&".concat(or,"=(.*)");
              location.href = location.href.replace(location.href.match(new RegExp(rep))[1], sel);

            }
            else{
                location.href += "?&".concat(or,"=",sel);
            }


            //a("select.orderby").closest("form").submit()}

        }
    );


// "jQuery(function(a){a(\".woocommerce-ordering\").on(\"change\",\"select.orderby\",function(){a(this).closest(\"form\").submit()}),a(\"input.qty:not(.product-quantity input.qty)\").each(function(){var b=parseFloat(a(this).attr(\"min\"));b>=0&&parseFloat(a(this).val())<b&&a(this).val(b)})});";





        // a("input.qty:not(.product-quantity input.qty)").each(function(){var b=parseFloat(a(this).attr("min"));b>=0&&parseFloat(a(this).val())<b&&a(this).val(b)})});

    //
    // jQuery('.dropdown_layered_nav_series').change(function () {
    //     var slug = jQuery(this).val();
    //     if (!$.contains(location.href,'?filtering=1&filter_series='))
    //         if (location.href.lastIndexOf("?") > 0){
    //             location.href += '&filter_series=' + slug;
    //         }
    //        else{
    //              location.href += '?filtering=1&filter_series=' + slug;
    //         }
    // });

    // jQuery('.dropdown_layered_nav_frequency').change(function () {
    //     var slug = jQuery(this).val();
    //      if (!$.contains(location.href,'?filtering=1&filter_frequency='))
    //         if (location.href.lastIndexOf("?") > 0){
    //             location.href += '&filter_frequency=' + slug;
    //         }
    //        else{
    //              location.href += '?filtering=1&filter_frequency=' + slug;
    //         }
    // });
//
//
});
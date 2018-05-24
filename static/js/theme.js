
(function ($) {
    "use strict";
    /*==========================================================================
     // Silder 
     =========================================================================*/
    if ($('.slider').length > 0) {
        $('.slider').owlCarousel({
            singleItem: true
        });
    }
    /*==========================================================================
     // Silder 
     =========================================================================*/
    if ($('#map').length > 0) {
        var map;
        map = new GMaps({
            el: '#map',
            lat: 51.4584218,
            lng: -0.0813982,
            zoomControlOpt: {
                style: 'SMALL',
                position: 'TOP_LEFT'
            },
            scrollwheel: false,
            zoom: 16,
            zoomControl: false,
            panControl: false,
            streetViewControl: false,
            mapTypeControl: false,
            overviewMapControl: false,
            clickable: false
        });
        map.addMarker({
            lat: 51.4584218,
            lng: -0.0813982,
            icon: "images/mapmarkar.png"
        });
    }
    /*==========================================================================
     // Left Menu
     =========================================================================*/
    var tt = true;
    $("#leftTrigger").on('click', function (e) {
        e.preventDefault();
        if (tt)
        {
            $('body').addClass('menuOpened');
            tt = false;
        } else
        {
            $(this).removeClass('active').fadeIn('fast');
            $('body').removeClass('menuOpened');
            tt = true;
        }
    });
    $(".leftclose").on('click', function (e) {
        e.preventDefault();
        $("#leftTrigger").removeClass('active').fadeIn('fast');
        $('body').removeClass('menuOpened');
        tt = true;
    });

    $('.leftmainnav .has-menu-items').on('click', function () {
        $(this).toggleClass('active');
        $('.sub-menu', this).slideToggle();

    });


    /*==========================================================================
     // Mobile Menu
     =========================================================================*/
    $('.mainNav .menuBar').on('click', function () {
        $(this).toggleClass('active');
        $('.mainNav > ul').slideToggle();
    });
    if ($(window).width() < 900)
    {
        $(".mainNav > ul > li.has-menu-items > a").on('click', function () {
            $(this).parent().toggleClass('active');
            $(this).parent().children('.sub-menu').slideToggle('slow');
            $(this).parent().children('.megaitem').slideToggle('slow');
            
        });
    }

    //========================
    // Contact Submit
    //========================
    if ($("#contactForm").length > 0)
    {
        $("#contactForm").on('submit', function (e) {
            e.preventDefault();
            $("#con_submit").html('Processsing...');
            var con_name, con_lname, con_email, con_message, con_sub;

            if ($("#con_name").length > 0) {
                var con_name = $("#con_name").val();
            }
            if ($("#con_email").length > 0) {
                var con_email = $("#con_email").val();
            }
            if ($("#con_message").length > 0) {
                var con_message = $("#con_message").val();
            }
            if ($("#con_sub").length > 0) {
                var con_sub = $("#con_sub").val();
            }

            var required = 0;
            $(".required", this).each(function () {
                if ($(this).val() === '')
                {
                    $(this).addClass('reqError');
                    required += 1;
                } else
                {
                    if ($(this).hasClass('reqError'))
                    {
                        $(this).removeClass('reqError');
                        if (required > 0)
                        {
                            required -= 1;
                        }
                    }
                }
            });
            if (required === 0)
            {
                $.ajax({
                    type: "POST",
                    url: 'php/mail.php',
                    data: {con_name: con_name, con_email: con_email, con_message: con_message, con_sub: con_sub},
                    success: function (data)
                    {
                        $("#con_submit").html('Done!');
                        $("#contactForm input, #contactForm textarea").val('');
                    }
                });
            } else
            {
                $("#con_submit").html('Failed!');
            }

        });

        $(".required").on('keyup', function () {
            $(this).removeClass('reqError');
        });
    }

    $(".leftmenuScroll").mCustomScrollbar();

    //========================
    // Subscriptions 
    //========================
    if ($("#subscriptionsforms").length > 0)
    {
        $("#subscriptionsforms").on('submit', function (e) {
            e.preventDefault();
            var sub_email = $("#sub_email").val();
            $("#subs_submit").html('Processsing...');
            if (sub_email === '')
            {
                $("#sub_email").addClass('reqError');
                $("#subs_submit").html('Failed!');
            } else
            {
                $("#sub_email").removeClass('reqError');
                $.ajax({
                    type: "POST",
                    url: "php/subscribe.php",
                    data: {sub_email: sub_email},
                    success: function (data)
                    {
                        $("#subscriptionsforms input").val('');
                        $("#subs_submit").html('success');
                    }
                });
            }
        });
        $("#sub_email").on('keyup', function () {
            $(this).removeClass('reqError');
        });
    }


})(jQuery);
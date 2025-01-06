/*  ---------------------------------------------------
    Theme Name: Cake
    Description: Cake e-commerce tamplate
    Author: Colorib
    Author URI: https://www.colorib.com/
    Version: 1.0
    Created: Colorib
---------------------------------------------------------  */

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Search Switch
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    //Canvas Menu
    $(".canvas__open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("active");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".offcanvas-menu-overlay").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("active");
        $(".offcanvas-menu-overlay").removeClass("active");
    });


    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*-----------------------
        Hero Slider
    ------------------------*/
    $(".hero__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<i class='fa fa-angle-left'><i/>", "<i class='fa fa-angle-right'><i/>"],
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false
    });

    /*--------------------------
        Categories Slider
    ----------------------------*/
    $(".categories__slider").owlCarousel({
        loop: true,
        margin: 22,
        items: 5,
        dots: false,
        nav: true,
        navText: ["<span class='arrow_carrot-left'><span/>", "<span class='arrow_carrot-right'><span/>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false,
        responsive: {
            0: {
                items: 1,
                margin: 0
            },
            480: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            },
            1200: {
                items: 5
            }
        }
    });

    /*-----------------------------
        Testimonial Slider
    -------------------------------*/
    $(".testimonial__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 2,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            }
        }
    });

    /*---------------------------------
        Related Products Slider
    ----------------------------------*/
    $(".related__products__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 4,
        dots: false,
        nav: true,
        navText: ["<span class='arrow_carrot-left'><span/>", "<span class='arrow_carrot-right'><span/>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            },
        }
    });

    /*--------------------------
        Select
    ----------------------------*/
    $("select").niceSelect();

    /*------------------
		Magnific
	--------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe'
    });

    /*------------------
        Barfiller
    --------------------*/
    $('#bar1').barfiller({
        barColor: '#111111',
        duration: 2000
    });
    $('#bar2').barfiller({
        barColor: '#111111',
        duration: 2000
    });
    $('#bar3').barfiller({
        barColor: '#111111',
        duration: 2000
    });


    /*------------------
		Single Product
	--------------------*/
    $('.product__details__thumb img').on('click', function () {
        $('.product__details__thumb .pt__item').removeClass('active');
        $(this).addClass('active');
        var imgurl = $(this).data('imgbigurl');
        var bigImg = $('.big_img').attr('src');
        if (imgurl != bigImg) {
            $('.big_img').attr({
                src: imgurl
            });
        }
    });

    /*-------------------
		Quantity change
	--------------------- */

    // var proQty = $('.pro-qty');
    // const min_value_count = parseFloat($('#min_value_count').val());
    // proQty.prepend('<span class="dec qtybtn">-</span>');
    // proQty.append('<span class="inc qtybtn">+</span>');
    // proQty.on('click', '.qtybtn', function () {
    //     var $button = $(this);
    //     var oldValue = parseFloat($button.parent().find('input').val());
    //     var newVal;
    //     if ($button.hasClass('inc')) {
    //         newVal = oldValue + 1;
    //     } else {
    //         // Don't allow decrementing below the minimum value
    //         newVal = oldValue > min_value_count ? oldValue - 1 : min_value_count;
    //     }
    //     $button.parent().find('input').val(newVal);
    // });
    // $('.pro-qty').each(function () {
    //     var $this = $(this);
    //     var productId = $this.find('input').attr('id').split('_')[2];
    //     var min_value_count = parseFloat($('#min_value_count_' + productId).val());
    //
    //     $this.prepend('<span class="dec qtybtn">-</span>');
    //     $this.append('<span class="inc qtybtn">+</span>');
    //
    //     $this.on('click', '.qtybtn', function () {
    //         var $button = $(this);
    //         var oldValue = parseFloat($button.parent().find('input').val());
    //         var newVal;
    //         if ($button.hasClass('inc')) {
    //             newVal = oldValue + 1;
    //         } else {
    //             // Don't allow decrementing below the minimum value
    //             newVal = oldValue > min_value_count ? oldValue - 1 : min_value_count;
    //         }
    //         $button.parent().find('input').val(newVal);
    //     });
    // });


    $(".product__details__thumb").niceScroll({
        cursorborder: "",
        cursorcolor: "rgba(0, 0, 0, 0.5)",
        boxzoom: false
    });






})(jQuery);

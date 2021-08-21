/*
 Template Name: Marvil - Multi purpose HTML Template
 Template URI: http://elmanawy.info/demo/marvil
 Description: Multi purpose HTML Template
 Author: Marwa El-Manawy
 Author URI: https://elmanawy.info/
 Version: 1.0
 */
/*================================================
 [  Table of contents  ]
 ================================================
 :: Page loader
 :: Back to top
 :: Clients Reviews
 :: Owl corousel Team
 :: scrollIt Jquey Plugin
 :: Main Menu Fixed
 :: Wow Animation
 :: Isotope
 :: Masonry
 :: Portfolio
 :: Magnific Popup
 :: SUBSCRIBE
 :: CONTACT FORM
 :: Parallex
 :: Rotating Word
 :: Counter UP
 ======================================
 [ End table content ]
 ======================================*/


jQuery(document).ready(function () {
    "use strict";
    $('body').addClass('loaded');

    /**
     * =====================================
     * Owl corousel Clients Reviews
     * =====================================
     **/
    $(".all-reviews").owlCarousel({
        autoPlay: true,
        pagination: true,
        items: 3,
        itemsDesktop: [1024, 3],
        itemsDesktopSmall: [768, 2],
        itemsTablet: [650, 1],
        itemsMobile: 1
    });
    /**
     * =====================================
     * Owl corousel Team
     * =====================================
     */
    $(".all-team").owlCarousel({
        autoPlay: true,
        pagination: true,
        items: 4,
        itemsDesktop: [1024, 4],
        itemsDesktopSmall: [991, 2],
        itemsTablet: [650, 1],
        itemsMobile: 1
    }
    );

    /**
     /**
     * =====================================
     * scrollIt Jquey Plugin
     * =====================================
     */
    $.scrollIt({
        upKey: 60, // key code to navigate to the next section
        downKey: 40, // key code to navigate to the previous section
        easing: 'linear', // the easing function for animation
        scrollTime: 600, // how long (in ms) the animation takes
        activeClass: 'active', // class given to the active nav element
        onPageChange: null, // function(pageIndex) that is called when page is changed
        topOffset: -70 // offste (in px) for fixed top navigation
    }
    );

    /**
     * =====================================
     * Main Menu Fixed
     * =====================================
     */
    var $navberArea = $('.navber-area');
    var $bodyOverlay = $('.body-overlay');
    var $demoNavber = $('.demo-navber');
    $(".demo-button i").on('click', function () {
        $navberArea.addClass("show");
        $bodyOverlay.addClass('visible');
    }
    );
    $('.nav-menu ul li a, .nav-close-button i, .body-overlay').on('click', function () {
        $navberArea.removeClass("show");
        $bodyOverlay.removeClass('visible');
    }
    );
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 1) {
            $navberArea.addClass("main-menu-fix");
            $demoNavber.addClass("main-menu-fix");
        }
        else {
            $navberArea.removeClass("main-menu-fix");
            $demoNavber.removeClass("main-menu-fix");
        }
    });


    /**
     * =====================================
     * Wow Animation
     * =====================================
     **/
    var wow = new WOW({
        boxClass: 'wow', // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset: 0, // distance to the element when triggering the animation (default is 0)
        mobile: false, // trigger animations on mobile devices (default is true)
        live: true, // act on asynchronously loaded content (default is true)
        callback: function (box) {
        }
        , scrollContainer: true // optional scroll container selector, otherwise use window
    }
    );
    wow.init();

    /* SUBSCRIBE
     ======================================*/
    $("#subscriber_form").on("submit", function (e)
    {
        $('#show_subscriber_msg').html('<div class=gen>Submiting..</div>');
        var subscriberemail = $('#subscriberemail').val();
        var formURL = $(this).attr("action");
        var data = {
            subscriberemail: subscriberemail
        };
        $.ajax(
                {
                    url: formURL,
                    type: "POST",
                    data: data,
                    success: function (res) {
                        if (res === '1') {
                            $('#show_subscriber_msg').html('<div class=gen> <i class="fa fa-smile-o" aria-hidden="true"></i> شكرا لك، تم الاشتراك في القائمة البريدية بنجاح</div>');
                            $("#subscriber_form")[0].reset();
                        }

                        if (res === '5') {
                            $('#show_subscriber_msg').html('<div class=err><i class="fa fa-frown-o" aria-hidden="true"></i> من فضلك ادخل بريد الكتروني صحيح</div>');
                        }
                    }
                });
        e.preventDefault();
    });

    /* Initializing Particles */
    if ($("#particles-js").length) {
        window.onload = function () {
            Particles.init({
                selector: '#particles-js',
                color: '#ffffff',
                connectParticles: false,
                sizeVariations: 14,
                maxParticles: 140,
            });
        };
    }

    /*Counter*/
    $('.counterUp').counterUp({
        delay: 10,
        time: 1000
    });

    /*rotating words*/
    $("#js-rotating").Morphext({
        animation: "bounceIn",
        separator: ",",
        speed: 2000
    });
});


/**
 * =====================================
 * Back To Top
 * =====================================
 **/
function backtotop() {
    $('#back-to-top').fadeOut();
    $(window).scroll(function () {
        if ($(this).scrollTop() > 250) {
            $('#back-to-top').fadeIn(1500);
        } else {
            $('#back-to-top').fadeOut(500);
        }
    });
    // scroll body to 0px on click
    $('#top').on('click', function () {
        $('top').tooltip('hide');
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
}

/**
 * =====================================
 * Isotope
 * =====================================
 **/
function isotope() {
    var $isotope = $(".isotope"),
            $itemElement = '.mr-grid-item',
            $filters = $('.isotope-filters');
    if ($isotope) {
        $isotope.isotope({
            resizable: true,
            itemSelector: $itemElement,
            masonry: {
                gutterWidth: 10
            }
        });
        $filters.on('click', 'button', function () {
            var $val = $(this).attr('data-filter');
            $isotope.isotope({
                filter: $val
            });
            $filters.find('.active').removeClass('active');
            $(this).addClass('active');
        });
    }

}

/**
 * =====================================
 * Masonry
 * =====================================
 **/
function masonry() {
    var $masonry = $('.mr-masonry-block .mr-masonry'),
            $itemElement = '.mr-masonry-block .mr-masonry-item',
            $filters = $('.mr-masonry-block .isotope-filters');
    if ($masonry) {
        $masonry.isotope({
            percentPosition: true,
            resizable: true,
            itemSelector: $itemElement,
            masonry: {
                gutterWidth: 0
            }
        });
        $filters.on('click', 'button', function () {
            var filterValue = $(this).attr('data-filter');
            $masonry.isotope({
                filter: filterValue
            });
        });

        $filters.each(function (i, buttonGroup) {
            var $buttonGroup = $(buttonGroup);
            $buttonGroup.on('click', 'button', function () {
                $buttonGroup.find('.active').removeClass('active');
                $(this).addClass('active');
            });
        });
    }

}


/**
 * =====================================
 * Magnific Popup
 * =====================================
 **/

function popupgallery() {
    $('.popup-gallery').magnificPopup({
        delegate: 'a.popup-img',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
        },
    });

    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

}

/**
 * =====================================
 * Calling Functions
 * =====================================
 **/
$(window).on('load', function () {
    backtotop();
    isotope();
    masonry();
    popupgallery();
});
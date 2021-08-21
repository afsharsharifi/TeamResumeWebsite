window.console = window.console || (function() {
    var c = {};
    c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile = c.clear = c.exception = c.trace = c.assert = function() {};
    return c;
})();
jQuery(document).ready(function($) {
    $("#style-switcher .main").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/main.css");
        return false;
    });
    $("#style-switcher .blue").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/blue.css");
        return false;
    });
    $("#style-switcher .green").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/green.css");
        return false;
    });
    $("#style-switcher .orange").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/orange.css");
        return false;
    });
    $("#style-switcher .navy").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/navy.css");
        return false;
    });
    $("#style-switcher .yellow").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/yellow.css");
        return false;
    });
    $("#style-switcher .peach").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/peach.css");
        return false;
    });
    $("#style-switcher .beige").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/beige.css");
        return false;
    });
    $("#style-switcher .purple").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/purple.css");
        return false;
    });
    $("#style-switcher .red").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/red.css");
        return false;
    });
    $("#style-switcher .pink").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/pink.css");
        return false;
    });
    $("#style-switcher .celadon").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/celadon.css");
        return false;
    });
    $("#style-switcher .brown").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/brown.css");
        return false;
    });
    $("#style-switcher .cherry").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/cherry.css");
        return false;
    });
    $("#style-switcher .gray").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/gray.css");
        return false;
    });
    $("#style-switcher .darkcol").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/dark.css");
        return false;
    });
    $("#style-switcher .cyan").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/cyan.css");
        return false;
    });
    $("#style-switcher .olive").click(function() {
        $("#colors").attr("href", "/site_static/css/colors/olive.css");
        return false;
    });
    $("#style-switcher h2 a").click(function(e) {
        e.preventDefault();
        var div = $("#style-switcher");
        console.log(div.css("right"));
        if (div.css("right") === "-205px") {
            $("#style-switcher").animate({
                right: "0px"
            });
        } else {
            $("#style-switcher").animate({
                right: "-205px"
            });
        }
    });
    $("#layout-style").change(function(e) {
        if ($(this).val() == 1) {
            $("body").addClass("boxed");
            $("body").removeClass("fullwidth");
            $(window).resize();
        } else {
            $("body").removeClass("boxed");
            $("body").addClass("fullwidth");
            $(window).resize();
        }
    });
    $("#layout-switcher").on('change', function() {
        $('#layout').attr('href', $(this).val() + '.css');
    });
    $(".colors li a").click(function(e) {
        e.preventDefault();
        $(this).parent().parent().find("a").removeClass("active");
        $(this).addClass("active");
    });
    $('.bg li a').click(function() {
        var current = $('#style-switcher select[id=layout-style]').find('option:selected').val();
        if (current == '1') {
            var bg = $(this).css("backgroundImage");
            $("body").css("backgroundImage", bg);
        } else {
            alert('Please select boxed layout');
        }
    });
    $('.bgsolid li a').click(function() {
        var current = $('#style-switcher select[id=layout-style]').find('option:selected').val();
        if (current == '1') {
            var bg = $(this).css('backgroundColor');
            $('body').css('backgroundColor', bg).css('backgroundImage', 'none')
        } else {
            alert('Please select boxed layout');
        }
    });
    $("#reset a").click(function(e) {
        e.preventDefault();
        $("body").removeClass("boxed");
        $("header").removeClass("alternative");
        $("header").removeClass("full-width");
        $(".colors li a").removeClass("active");
        $("#colors").attr("href", "css/colors/main.css");
        $(window).resize();
    });
});
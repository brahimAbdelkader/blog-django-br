

$(document).ready(function () {
    $('form').parent().css('background-color', '#fff');
})


$(".see_more").click(function () {
    $(".see_more_blog").animate({
        height: "72px"
    }, 1500); // how long the animation should be
});
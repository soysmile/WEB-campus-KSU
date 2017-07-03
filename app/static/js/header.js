$(window).scroll(function() {
    
if ($(this).scrollTop() > 1){
$('.navbar.navbar-inverse.navbar-static-top.primaryNav').addClass("sticky");
}
else{
$('.navbar.navbar-inverse.navbar-static-top.primaryNav').removeClass("sticky");
}
});


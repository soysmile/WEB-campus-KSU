$(function(){
/* выбор города */
$(".cities_list").hide();
$('.delivery_list').click(function(){
    $(".cities_list").slideToggle('fast');
});
$('ul.cities_list li').click(function(){
    var tx = $(this).html();
    $(".cities_list").slideUp('fast');
    $(".delivery_list span").html(tx);
    });
})


$(function(){
$(".cities_list1").hide();
$('.delivery_list1').click(function(){
    $(".cities_list1").slideToggle('fast');
});
$('ul.cities_list1 li').click(function(){
    var tx = $(this).html();
    $(".cities_list1").slideUp('fast');
    $(".delivery_list1 span").html(tx);
    

	if (tx=="Комната №1"){
        $("#room1").css({'background-color':'rgba(0,255,30,0.25)'});
        $("#room2").css({'background-color':'rgba(0,255,30,0)'});
	}    
	else if(tx=="Комната №2"){
        $("#room2").css({'background-color':'rgba(255,0,00,0.25)'});
        $("#room1").css({'background-color':'rgba(0,255,30,0)'});
    }
    });
})

    $("#button").live("click", function() {
	if ($("#div").attr("display") == "none") {
		$("#div").attr("display","inline-block");
		$("#div").slideDown();
	}
	else {
		$("#div").slideUp();
		$("#div").attr("display","none");
	}	
});
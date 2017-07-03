$(document).ready(function() {

    $('#campus2').show('slow');
    $('#campus3').hide('slow');
    $('#campus4').hide('slow');

    $("#aMap").css({"color": "greenyellow"});
    $("#bMap").css({"color": "white"});
    $("#cMap").css({"color": "white"});


    $('#aMap').click(function() {

        //$('#a').hide();
        $('#campus2').animate({
            height: 'show'

        });
        $("#aMap").css({"color": "greenyellow"});
        $("#bMap").css({"color": "white"});
        $("#cMap").css({"color": "white"});


        $('#campus3').hide('slow');
        $('#campus4').hide('slow');


    });

    $('#bMap').click(function() {

        //$('#a').hide();
        $('#campus3').animate({
            height: 'show'

        });
        $("#aMap").css({"color": "white"});
        $("#bMap").css({"color": "greenyellow"});
        $("#cMap").css({"color": "white"});


        $('#campus2').hide('slow');
        $('#campus4').hide('slow');


    });

    $('#cMap').click(function() {

        //$('#a').hide();
        $('#campus4').animate({
            height: 'show'

        });

        $("#aMap").css({"color": "white"});
        $("#bMap").css({"color": "white"});
        $("#cMap").css({"color": "greenyellow"});


        $('#campus2').hide('slow');
        $('#campus3').hide('slow');


    });


});

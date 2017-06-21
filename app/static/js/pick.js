$(document).ready(function() {

    $('#campus2').show('slow');
    $('#campus3').hide('slow');
    $('#campus4').hide('slow');

    $("#aMap").css({"color": "green"});
    $("#bMap").css({"color": "black"});
    $("#cMap").css({"color": "black"});


    $('#aMap').click(function() {

        //$('#a').hide();
        $('#campus2').animate({
            height: 'show'

        });
        $("#aMap").css({"color": "green"});
        $("#bMap").css({"color": "black"});
        $("#cMap").css({"color": "black"});


        $('#campus3').hide('slow');
        $('#campus4').hide('slow');


    });

    $('#bMap').click(function() {

        //$('#a').hide();
        $('#campus3').animate({
            height: 'show'

        });
        $("#aMap").css({"color": "black"});
        $("#bMap").css({"color": "green"});
        $("#cMap").css({"color": "black"});


        $('#campus2').hide('slow');
        $('#campus4').hide('slow');


    });

    $('#cMap').click(function() {

        //$('#a').hide();
        $('#campus4').animate({
            height: 'show'

        });

        $("#aMap").css({"color": "black"});
        $("#bMap").css({"color": "black"});
        $("#cMap").css({"color": "green"});


        $('#campus2').hide('slow');
        $('#campus3').hide('slow');


    });


});

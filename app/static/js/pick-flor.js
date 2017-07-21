$(document).ready(function () {
    //2
    $('#flor-1').show('slow');
    $('#flor-2').hide('slow');
    $('#flor-3').hide('slow');
    $('#flor-4').hide('slow');
    $('#flor-5').hide('slow');
    //4
    $('#flor-4-1').show('slow');
    $('#flor-4-2').hide('slow');
    $('#flor-4-3').hide('slow');
    $('#flor-4-4').hide('slow');
    $('#flor-4-5').hide('slow');
    $('#flor-4-6').hide('slow');
    $('#flor-4-7').hide('slow');
    $('#flor-4-8').hide('slow');
    $('#flor-4-9').hide('slow');

    //2
    $("#first-flor").css({
        "color": "greenyellow"
    });
    $("#second-flor").css({
        "color": "white"
    });
    $("#third-flor").css({
        "color": "white"
    });
    $("#fourth-flor").css({
        "color": "white"
    });
    $("#fifth-flor ").css({
        "color": "white"
    });
    //3
    $("#first-flor-3").css({
        "color": "greenyellow"
    });
    $("#second-flor-3").css({
        "color": "white"
    });
    $("#third-flor-3").css({
        "color": "white"
    });
    $("#fourth-flor-3").css({
        "color": "white"
    });
    $("#fifth-flor-3").css({
        "color": "white"
    });
    $("#sixth-flor-3").css({
        "color": "white"
    });
    $("#seventh-flor-3").css({
        "color": "white"
    });
    $("#eighth-flor-3").css({
        "color": "white"
    });
    $("#nineth-flor-3").css({
        "color": "white"
    });
    //4
    $("#first-flor-4").css({
        "color": "greenyellow"
    });
    $("#second-flor-4").css({
        "color": "white"
    });
    $("#third-flor-4").css({
        "color": "white"
    });
    $("#fourth-flor-4").css({
        "color": "white"
    });
    $("#fifth-flor-4").css({
        "color": "white"
    });
    $("#sixth-flor-4").css({
        "color": "white"
    });
    $("#seventh-flor-4").css({
        "color": "white"
    });
    $("#eighth-flor-4").css({
        "color": "white"
    });
    $("#nineth-flor-4").css({
        "color": "white"
    });




    $('#first-flor').click(function () {

        //$('#a').hide();
        $('#flor-2').hide('slow');
        $('#flor-5').hide('slow');
        $('#flor-4').hide('slow');
        $('#flor-3').hide('slow', function () {
            $('#flor-1').animate({
                "height": "show"
            })
        });




        $("#first-flor").css({
            "color": "greenyellow"
        });
        $("#second-flor").css({
            "color": "white"
        });
        $("#third-flor").css({
            "color": "white"
        });
        $("#fourth-flor").css({
            "color": "white"
        });
        $("#fifth-flor").css({
            "color": "white"
        });

    });

    $('#second-flor').click(function () {


        $('#flor-1').hide('slow');
        $('#flor-5').hide('slow');
        $('#flor-4').hide('slow');
        $('#flor-3').hide('slow', function () {
            $('#flor-2').animate({
                "height": "show"
            })
        });


        $("#first-flor").css({
            "color": "white"
        });
        $("#second-flor").css({
            "color": "greenyellow"
        });
        $("#third-flor").css({
            "color": "white"
        });
        $("#fourth-flor").css({
            "color": "white"
        });
        $("#fifth-flor").css({
            "color": "white"
        });





    });

    $('#third-flor').click(function () {



        $('#flor-3').animate({
                height: 'show'
            },
            function () {
                $('#flor-5').hide('slow');
                $('#flor-4').hide('slow');
                $('#flor-2').hide('slow');
                $('#flor-1').hide('slow');

            });

        $("#first-flor").css({
            "color": "white"
        });
        $("#second-flor").css({
            "color": "white"
        });
        $("#third-flor").css({
            "color": "greenyellow"
        });
        $("#fourth-flor").css({
            "color": "white"
        });
        $("#fifth-flor").css({
            "color": "white"
        });

    });

    $('#fourth-flor').click(function () {



        $('#flor-4').animate({
                height: 'show'

            },
            function () {
                $('#flor-5').hide('slow');
                $('#flor-3').hide('slow');
                $('#flor-2').hide('slow');
                $('#flor-1').hide('slow');

            });
        $("#first-flor").css({
            "color": "white"
        });
        $("#second-flor").css({
            "color": "white"
        });
        $("#third-flor").css({
            "color": "white"
        });
        $("#fourth-flor").css({
            "color": "greenyellow"
        });
        $("#fifth-flor").css({
            "color": "white"
        });

    });

    $('#fifth-flor').click(function () {



        $('#flor-5').animate({
                height: 'show'

            },
            function () {
                $('#flor-3').hide('slow');
                $('#flor-4').hide('slow');
                $('#flor-2').hide('slow');
                $('#flor-1').hide('slow');
            });

        $("#first-flor").css({
            "color": "white"
        });
        $("#second-flor").css({
            "color": "white"
        });
        $("#third-flor").css({
            "color": "white"
        });
        $("#fourth-flor").css({
            "color": "white"
        });
        $("#fifth-flor").css({
            "color": "greenyellow"
        });

    });

    $('#first-flor-4').click(function () {

        //$('#a').hide();
        $('#flor-4-2').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-3').hide('slow', function () {
            $('#flor-4-1').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "greenyellow"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });


    });

    $('#second-flor-4').click(function () {


        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-3').hide('slow', function () {
            $('#flor-4-2').animate({
                "height": "show"
            })
        });


        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "greenyellow"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });





    });

    $('#third-flor-4').click(function () {



        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-3').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "greenyellow"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });

    });

    $('#fourth-flor-4').click(function () {

        $('#flor-4-1').hide('slow');
        $('#flor-4-3').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-4').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "greenyellow"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });

    });

    $('#fifth-flor-4').click(function () {



        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-3').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-5').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "greenyellow"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });

    });

    $('#sixth-flor-4').click(function () {



        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-3').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-6').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "greenyellow"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });

    });

    $('#seventh-flor-4').click(function () {



        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-3').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-7').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "greenyellow"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });

    });

    $('#eighth-flor-4').click(function () {



        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-3').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-8').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "greenyellow"
        });
        $("#nineth-flor-4").css({
            "color": "white"
        });

    });

    $('#nineth-flor-4').click(function () {



        $('#flor-4-1').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-3').hide('slow');

        $('#flor-4-2').hide('slow', function () {
            $('#flor-4-9').animate({
                "height": "show"
            })
        });

        $("#first-flor-4").css({
            "color": "white"
        });
        $("#second-flor-4").css({
            "color": "white"
        });
        $("#third-flor-4").css({
            "color": "white"
        });
        $("#fourth-flor-4").css({
            "color": "white"
        });
        $("#fifth-flor-4").css({
            "color": "white"
        });
        $("#sixth-flor-4").css({
            "color": "white"
        });
        $("#seventh-flor-4").css({
            "color": "white"
        });
        $("#eighth-flor-4").css({
            "color": "white"
        });
        $("#nineth-flor-4").css({
            "color": "greenyellow"
        });

    });
    $('#second-flor-3').click(function () {


        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-3').hide('slow', function () {
            $('#flor-3-2').animate({
                "height": "show"
            })
        });


        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "greenyellow"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });





    });

    $('#third-flor-3').click(function () {



        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-3').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "greenyellow"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });

    });

    $('#fourth-flor-3').click(function () {

        $('#flor-3-1').hide('slow');
        $('#flor-3-3').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-4').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "greenyellow"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });

    });

    $('#fifth-flor-3').click(function () {



        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-3').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-5').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "greenyellow"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });

    });

    $('#sixth-flor-3').click(function () {



        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-3').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-6').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "greenyellow"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });

    });

    $('#seventh-flor-3').click(function () {



        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-3').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-7').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "greenyellow"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });

    });

    $('#eighth-flor-3').click(function () {



        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-3').hide('slow');
        $('#flor-3-9').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-8').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "greenyellow"
        });
        $("#nineth-flor-3").css({
            "color": "white"
        });

    });

    $('#nineth-flor-3').click(function () {



        $('#flor-3-1').hide('slow');
        $('#flor-3-4').hide('slow');
        $('#flor-3-5').hide('slow');
        $('#flor-3-6').hide('slow');
        $('#flor-3-7').hide('slow');
        $('#flor-3-8').hide('slow');
        $('#flor-3-3').hide('slow');

        $('#flor-3-2').hide('slow', function () {
            $('#flor-3-9').animate({
                "height": "show"
            })
        });

        $("#first-flor-3").css({
            "color": "white"
        });
        $("#second-flor-3").css({
            "color": "white"
        });
        $("#third-flor-3").css({
            "color": "white"
        });
        $("#fourth-flor-3").css({
            "color": "white"
        });
        $("#fifth-flor-3").css({
            "color": "white"
        });
        $("#sixth-flor-3").css({
            "color": "white"
        });
        $("#seventh-flor-3").css({
            "color": "white"
        });
        $("#eighth-flor-3").css({
            "color": "white"
        });
        $("#nineth-flor-3").css({
            "color": "greenyellow"
        });

    });

});

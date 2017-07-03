    $(document).ready(function() {


        $('#tab1').show('slow');
        $('#tab2').hide('slow');
        $('#tab3').hide('slow');
        $('#tab4').hide('slow');
        $('#tab5').hide('slow');
        $('#tab6').hide('slow');

        $("#abtn").css({"color": "greenyellow"});
        $("#bbtn").css({"color": "white"});
        $("#cbtn").css({"color": "white"});
        $("#dbtn").css({"color": "white"});
        $("#wbtn").css({"color": "white"});
        $("#rbtn").css({"color": "white"});

        $('#abtn').click(function() {

            //$('#a').hide();
            $('#tab1').animate({
                height: 'show'

            });

            $("#abtn").css({"color": "greenyellow"});
            $("#bbtn").css({"color": "white"});
            $("#cbtn").css({"color": "white"});
            $("#dbtn").css({"color": "white"});
            $("#wbtn").css({"color": "white"});
            $("#rbtn").css({"color": "white"});

            $('#tab2').hide('slow');
            $('#tab3').hide('slow');
            $('#tab4').hide('slow');
            $('#tab5').hide('slow');
            $('#tab6').hide('slow');

        });

        $('#bbtn').click(function() {

            //$('#b').hide();
            $('#tab2').animate({
                height: 'show'
            });

            $("#abtn").css({"color": "white"});
            $("#bbtn").css({"color": "greenyellow"});
            $("#cbtn").css({"color": "white"});
            $("#dbtn").css({"color": "white"});
            $("#wbtn").css({"color": "white"});
            $("#rbtn").css({"color": "white"});

            $('#tab1').hide('slow');
            $('#tab3').hide('slow');
            $('#tab4').hide('slow');
            $('#tab5').hide('slow');
            $('#tab6').hide('slow');

        });

        $('#cbtn').click(function() {

            //$('#c').hide();
            $('#tab3').animate({
                width : 'show'
            });

            $("#abtn").css({"color": "white"});
            $("#bbtn").css({"color": "white"});
            $("#cbtn").css({"color": "greenyellow"});
            $("#dbtn").css({"color": "white"});
            $("#wbtn").css({"color": "white"});
            $("#rbtn").css({"color": "white"});

            $('#tab1').hide('slow');
            $('#tab2').hide('slow');
            $('#tab4').hide('slow');
            $('#tab5').hide('slow');
            $('#tab6').hide('slow');

        });

        $('#dbtn').click(function() {

            //$('#d').hide();
            $('#tab4').animate({
                width : 'show'
            });

            $("#abtn").css({"color": "white"});
            $("#bbtn").css({"color": "white"});
            $("#cbtn").css({"color": "white"});
            $("#dbtn").css({"color": "greenyellow"});
            $("#wbtn").css({"color": "white"});
            $("#rbtn").css({"color": "white"});

            $('#tab1').hide('slow');
            $('#tab2').hide('slow');
            $('#tab3').hide('slow');
            $('#tab5').hide('slow');
            $('#tab6').hide('slow');

        });

        $('#wbtn').click(function() {

            //$('#a').hide();
            $('#tab5').animate({
                height: 'show'

            });

            $("#abtn").css({"color": "white"});
            $("#bbtn").css({"color": "white"});
            $("#cbtn").css({"color": "white"});
            $("#dbtn").css({"color": "white"});
            $("#wbtn").css({"color": "greenyellow"});
            $("#rbtn").css({"color": "white"});

            $('#tab1').hide('slow');
            $('#tab2').hide('slow');
            $('#tab3').hide('slow');
            $('#tab4').hide('slow');
            $('#tab6').hide('slow');

        });

        $('#rbtn').click(function() {

            //$('#a').hide();
            $('#tab6').animate({
                height: 'show'

            });

            $("#abtn").css({"color": "white"});
            $("#bbtn").css({"color": "white"});
            $("#cbtn").css({"color": "white"});
            $("#dbtn").css({"color": "white"});
            $("#rbtn").css({"color": "greenyellow"});
            $("#wbtn").css({"color": "white"});

            $('#tab1').hide('slow');
            $('#tab2').hide('slow');
            $('#tab3').hide('slow');
            $('#tab4').hide('slow');
            $('#tab5').hide('slow');

        });

    });

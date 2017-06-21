    $(document).ready(function() {


        $('#tab1').show('slow');
        $('#tab2').hide('slow');
        $('#tab3').hide('slow');
        $('#tab4').hide('slow');
        $('#tab5').hide('slow');
        $('#tab6').hide('slow');

        $("#abtn").css({"color": "green"});
        $("#bbtn").css({"color": "black"});
        $("#cbtn").css({"color": "black"});
        $("#dbtn").css({"color": "black"});
        $("#wbtn").css({"color": "black"});
        $("#rbtn").css({"color": "black"});

        $('#abtn').click(function() {

            //$('#a').hide();
            $('#tab1').animate({
                height: 'show'

            });

            $("#abtn").css({"color": "green"});
            $("#bbtn").css({"color": "black"});
            $("#cbtn").css({"color": "black"});
            $("#dbtn").css({"color": "black"});
            $("#wbtn").css({"color": "black"});
            $("#rbtn").css({"color": "black"});

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

            $("#abtn").css({"color": "black"});
            $("#bbtn").css({"color": "green"});
            $("#cbtn").css({"color": "black"});
            $("#dbtn").css({"color": "black"});
            $("#wbtn").css({"color": "black"});
            $("#rbtn").css({"color": "black"});

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

            $("#abtn").css({"color": "black"});
            $("#bbtn").css({"color": "black"});
            $("#cbtn").css({"color": "green"});
            $("#dbtn").css({"color": "black"});
            $("#wbtn").css({"color": "black"});
            $("#rbtn").css({"color": "black"});

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

            $("#abtn").css({"color": "black"});
            $("#bbtn").css({"color": "black"});
            $("#cbtn").css({"color": "black"});
            $("#dbtn").css({"color": "green"});
            $("#wbtn").css({"color": "black"});
            $("#rbtn").css({"color": "black"});

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

            $("#abtn").css({"color": "black"});
            $("#bbtn").css({"color": "black"});
            $("#cbtn").css({"color": "black"});
            $("#dbtn").css({"color": "black"});
            $("#wbtn").css({"color": "green"});
            $("#rbtn").css({"color": "black"});

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

            $("#abtn").css({"color": "black"});
            $("#bbtn").css({"color": "black"});
            $("#cbtn").css({"color": "black"});
            $("#dbtn").css({"color": "black"});
            $("#rbtn").css({"color": "green"});
            $("#wbtn").css({"color": "black"});

            $('#tab1').hide('slow');
            $('#tab2').hide('slow');
            $('#tab3').hide('slow');
            $('#tab4').hide('slow');
            $('#tab5').hide('slow');

        });

    });

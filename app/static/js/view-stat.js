$(document).ready(function() {

    $('#stat1').show('slow');
    $('#stat2').hide('slow');
    $('#stat3').hide('slow');
    $('#stat4').hide('slow');
    $('#stat5').hide('slow');
    $('#stat6').hide('slow');
    $('#stat7').hide('slow');

    $("#aStat").css({"color": "green"});
    $("#bStat").css({"color": "black"});
    $("#cStat").css({"color": "black"});
    $("#dStat").css({"color": "black"});
    $("#eStat").css({"color": "black"});
    $("#fStat").css({"color": "black"});
    $("#gStat").css({"color": "black"});

    $('#aStat').click(function() {

        //$('#a').hide();
        $('#stat1').animate({
            height: 'show'

        });
        $("#aStat").css({"color": "green"});
        $("#bStat").css({"color": "black"});
        $("#cStat").css({"color": "black"});
        $("#dStat").css({"color": "black"});
        $("#eStat").css({"color": "black"});
        $("#fStat").css({"color": "black"});
        $("#gStat").css({"color": "black"});

        $('#stat2').hide('slow');
        $('#stat3').hide('slow');
        $('#stat4').hide('slow');
        $('#stat5').hide('slow');
        $('#stat6').hide('slow');
        $('#stat7').hide('slow');

    });

    $('#bStat').click(function() {

        //$('#a').hide();
        $('#stat2').animate({
            height: 'show'

        });
        $("#aStat").css({"color": "black"});
        $("#bStat").css({"color": "green"});
        $("#cStat").css({"color": "black"});
        $("#dStat").css({"color": "black"});
        $("#eStat").css({"color": "black"});
        $("#fStat").css({"color": "black"});
        $("#gStat").css({"color": "black"});

        $('#stat1').hide('slow');
        $('#stat3').hide('slow');
        $('#stat4').hide('slow');
        $('#stat5').hide('slow');
        $('#stat6').hide('slow');
        $('#stat7').hide('slow');

    });

    $('#cStat').click(function() {

        //$('#a').hide();
        $('#stat3').animate({
            height: 'show'

        });

        $("#aStat").css({"color": "black"});
        $("#bStat").css({"color": "black"});
        $("#cStat").css({"color": "green"});
        $("#dStat").css({"color": "black"});
        $("#eStat").css({"color": "black"});
        $("#fStat").css({"color": "black"});
        $("#gStat").css({"color": "black"});

        $('#stat1').hide('slow');
        $('#stat2').hide('slow');
        $('#stat4').hide('slow');
        $('#stat5').hide('slow');
        $('#stat6').hide('slow');
        $('#stat7').hide('slow');

    });

    $('#dStat').click(function() {

        //$('#a').hide();
        $('#stat4').animate({
            height: 'show'

        });

        $("#aStat").css({"color": "black"});
        $("#bStat").css({"color": "black"});
        $("#cStat").css({"color": "black"});
        $("#dStat").css({"color": "green"});
        $("#eStat").css({"color": "black"});
        $("#fStat").css({"color": "black"});
        $("#gStat").css({"color": "black"});

        $('#stat1').hide('slow');
        $('#stat2').hide('slow');
        $('#stat3').hide('slow');
        $('#stat5').hide('slow');
        $('#stat6').hide('slow');
        $('#stat7').hide('slow');

    });

    $('#eStat').click(function() {

        //$('#a').hide();
        $('#stat5').animate({
            height: 'show'

        });

        $("#aStat").css({"color": "black"});
        $("#bStat").css({"color": "black"});
        $("#cStat").css({"color": "black"});
        $("#dStat").css({"color": "black"});
        $("#eStat").css({"color": "green"});
        $("#fStat").css({"color": "black"});
        $("#gStat").css({"color": "black"});

        $('#stat1').hide('slow');
        $('#stat2').hide('slow');
        $('#stat3').hide('slow');
        $('#stat4').hide('slow');
        $('#stat6').hide('slow');
        $('#stat7').hide('slow');

    });

    $('#fStat').click(function() {

        //$('#a').hide();
        $('#stat6').animate({
            height: 'show'

        });

        $("#aStat").css({"color": "black"});
        $("#bStat").css({"color": "black"});
        $("#cStat").css({"color": "black"});
        $("#dStat").css({"color": "black"});
        $("#eStat").css({"color": "black"});
        $("#fStat").css({"color": "green"});
        $("#gStat").css({"color": "black"});

        $('#stat1').hide('slow');
        $('#stat2').hide('slow');
        $('#stat3').hide('slow');
        $('#stat4').hide('slow');
        $('#stat5').hide('slow');
        $('#stat7').hide('slow');

    });

    $('#gStat').click(function() {

        //$('#a').hide();
        $('#stat7').animate({
            height: 'show'

        });

        $("#aStat").css({"color": "black"});
        $("#bStat").css({"color": "black"});
        $("#cStat").css({"color": "black"});
        $("#dStat").css({"color": "black"});
        $("#eStat").css({"color": "black"});
        $("#fStat").css({"color": "black"});
        $("#gStat").css({"color": "green"});

        $('#stat1').hide('slow');
        $('#stat2').hide('slow');
        $('#stat3').hide('slow');
        $('#stat4').hide('slow');
        $('#stat5').hide('slow');
        $('#stat6').hide('slow');

    });

});

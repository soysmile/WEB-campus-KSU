$(document).ready(function() {
    //2
    $('#flor-2').show('slow');
    $('#flor-3').hide('slow');
    $('#flor-4').hide('slow');
    $('#flor-5').hide('slow');
    //4
    $('#flor-4-1').hide('slow');
    $('#flor-4-2').hide('slow');
    $('#flor-4-3').hide('slow');
    $('#flor-4-4').hide('slow');
    $('#flor-4-5').hide('slow');
    $('#flor-4-6').hide('slow');
    $('#flor-4-7').hide('slow');
    $('#flor-4-8').hide('slow');
    $('#flor-4-9').hide('slow');

    //2
    $("#first-flor").css({"color": "green"});
    $("#second-flor").css({"color": "darkgrey"});
    $("#third-flor").css({"color": "darkgrey"});
    $("#fourth-flor").css({"color": "darkgrey"});
    $("#fifth-flor ").css({"color": "darkgrey"});
    //3
    $("#first-flor-3").css({"color": "green"});
    $("#second-flor-3").css({"color": "darkgrey"});
    $("#third-flor-3").css({"color": "darkgrey"});
    $("#fourth-flor-3").css({"color": "darkgrey"});
    $("#fifth-flor-3").css({"color": "darkgrey"});
    $("#sixth-flor-3").css({"color": "darkgrey"});
    $("#seventh-flor-3").css({"color": "darkgrey"});
    $("#eighth-flor-3").css({"color": "darkgrey"});
    $("#nineth-flor-3").css({"color": "darkgrey"});
    //4
    $("#first-flor-4").css({"color": "green"});
    $("#second-flor-4").css({"color": "darkgrey"});
    $("#third-flor-4").css({"color": "darkgrey"});
    $("#fourth-flor-4").css({"color": "darkgrey"});
    $("#fifth-flor-4").css({"color": "darkgrey"});
    $("#sixth-flor-4").css({"color": "darkgrey"});
    $("#seventh-flor-4").css({"color": "darkgrey"});
    $("#eighth-flor-4").css({"color": "darkgrey"});
    $("#nineth-flor-4").css({"color": "darkgrey"});




    $('#first-flor').click(function() {

        //$('#a').hide();
        $('#flor-2').hide('slow');
        $('#flor-5').hide('slow');
        $('#flor-4').hide('slow');
        $('#flor-3').hide('slow',  function(){
          $('#flor-1').animate({"height":"show"})
        });




        $("#first-flor").css({"color": "green"});
        $("#second-flor").css({"color": "darkgrey"});
        $("#third-flor").css({"color": "darkgrey"});
        $("#fourth-flor").css({"color": "darkgrey"});
        $("#fifth-flor").css({"color": "darkgrey"});

    });

    $('#second-flor').click(function() {


        $('#flor-1').hide('slow');
        $('#flor-5').hide('slow');
        $('#flor-4').hide('slow');
        $('#flor-3').hide('slow',  function(){
          $('#flor-2').animate({"height":"show"})
        });


      $("#first-flor").css({"color": "darkgrey"});
      $("#second-flor").css({"color": "green"});
      $("#third-flor").css({"color": "darkgrey"});
      $("#fourth-flor").css({"color": "darkgrey"});
      $("#fifth-flor").css({"color": "darkgrey"});





    });

    $('#third-flor').click(function() {



      $('#flor-3').animate({
          height: 'show'
      },
      function(){
        $('#flor-5').hide('slow');
        $('#flor-4').hide('slow');
        $('#flor-2').hide('slow');
        $('#flor-1').hide('slow');

      });

      $("#first-flor").css({"color": "darkgrey"});
      $("#second-flor").css({"color": "darkgrey"});
      $("#third-flor").css({"color": "green"});
      $("#fourth-flor").css({"color": "darkgrey"});
      $("#fifth-flor").css({"color": "darkgrey"});

    });

    $('#fourth-flor').click(function() {



      $('#flor-4').animate({
          height: 'show'

      },
      function(){
        $('#flor-5').hide('slow');
        $('#flor-3').hide('slow');
        $('#flor-2').hide('slow');
        $('#flor-1').hide('slow');

      });
      $("#first-flor").css({"color": "darkgrey"});
      $("#second-flor").css({"color": "darkgrey"});
      $("#third-flor").css({"color": "darkgrey"});
      $("#fourth-flor").css({"color": "green"});
      $("#fifth-flor").css({"color": "darkgrey"});

    });

    $('#fifth-flor').click(function() {



      $('#flor-5').animate({
          height: 'show'

      },
      function(){
        $('#flor-3').hide('slow');
        $('#flor-4').hide('slow');
        $('#flor-2').hide('slow');
        $('#flor-1').hide('slow');
      });

      $("#first-flor").css({"color": "darkgrey"});
      $("#second-flor").css({"color": "darkgrey"});
      $("#third-flor").css({"color": "darkgrey"});
      $("#fourth-flor").css({"color": "darkgrey"});
      $("#fifth-flor").css({"color": "green"});

    });

    $('#first-flor-4').click(function() {

        //$('#a').hide();
        $('#flor-4-2').hide('slow');
        $('#flor-4-4').hide('slow');
        $('#flor-4-5').hide('slow');
        $('#flor-4-6').hide('slow');
        $('#flor-4-7').hide('slow');
        $('#flor-4-8').hide('slow');
        $('#flor-4-9').hide('slow');

        $('#flor-4-3').hide('slow',  function(){
          $('#flor-4-1').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "green"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});


    });

    $('#second-flor-4').click(function() {


      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-3').hide('slow',  function(){
          $('#flor-4-2').animate({"height":"show"})
        });


        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "green"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});





    });

    $('#third-flor-4').click(function() {



      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-3').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "green"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});

    });

    $('#fourth-flor-4').click(function() {

      $('#flor-4-1').hide('slow');
      $('#flor-4-3').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-4').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "green"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});

    });

    $('#fifth-flor-4').click(function() {



      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-3').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-5').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "green"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});

    });

    $('#sixth-flor-4').click(function() {



      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-3').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-6').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "green"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});

    });

    $('#seventh-flor-4').click(function() {



      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-3').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-7').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "green"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "darkgrey"});

    });

    $('#eighth-flor-4').click(function() {



      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-3').hide('slow');
      $('#flor-4-9').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-8').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "green"});
        $("#nineth-flor-4").css({"color": "darkgrey"});

    });

    $('#nineth-flor-4').click(function() {



      $('#flor-4-1').hide('slow');
      $('#flor-4-4').hide('slow');
      $('#flor-4-5').hide('slow');
      $('#flor-4-6').hide('slow');
      $('#flor-4-7').hide('slow');
      $('#flor-4-8').hide('slow');
      $('#flor-4-3').hide('slow');

        $('#flor-4-2').hide('slow',  function(){
          $('#flor-4-9').animate({"height":"show"})
        });

        $("#first-flor-4").css({"color": "darkgrey"});
        $("#second-flor-4").css({"color": "darkgrey"});
        $("#third-flor-4").css({"color": "darkgrey"});
        $("#fourth-flor-4").css({"color": "darkgrey"});
        $("#fifth-flor-4").css({"color": "darkgrey"});
        $("#sixth-flor-4").css({"color": "darkgrey"});
        $("#seventh-flor-4").css({"color": "darkgrey"});
        $("#eighth-flor-4").css({"color": "darkgrey"});
        $("#nineth-flor-4").css({"color": "green"});

    });

});

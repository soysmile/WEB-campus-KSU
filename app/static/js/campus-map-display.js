$(document).ready(function () {
    $('#campus-3, #myButton').click(function () {
        if (this.id == 'campus-3') {

            $('.campus-info-panel-in').fadeIn();
            
        } else if (this.id == 'myButton') {

            $('.campus-info-panel-in').fadeOut();
            
        }
    });
});
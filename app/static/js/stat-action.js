$(document).ready(function()
    {
    var flag=true;

    $(".stat-button").click(function()
        {
            if(flag==true)
        {
                $("#complete-stat").slideDown();
                flag=!flag;
            }
            else
            {
                $("#complete-stat").slideUp();
                flag=!flag;
            }
    });
});

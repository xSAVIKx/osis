/**
 * Created by Iurii Sergiichuk on 09.02.2015.
 */

$(document).ready(function ($) {
    var clickableRow = $(".clickable-row");
    clickableRow.on('click', function () {
        window.location.href = $(this).attr("href");
    });
});
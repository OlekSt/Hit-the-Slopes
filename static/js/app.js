$(document).ready(function(){
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.modal').modal();
    $('.datepicker').datepicker({
        selectMonths: true,
        selectYears: 3, 
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        firstDay: 1,
        format: 'yyyy.mm.dd'
    }); 

    /* Validate select fields so that a user cannot continue without filling them up */
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
    
    /* To make Date-To set for the same month as a chosen Date-From in add_trip.html */
    /* Same for search dates in trips.html */
    var today = new Date();
    setDate();
    function setDate(){
        /* Dates choice for a new trip */
        $('#from').datepicker({
        format: 'yyyy.mm.dd', 
        minDate: today,/* Block dates before today for a new trip */
        onSelect: function(dateFrom){
            $("#to").datepicker({ minDate: dateFrom, format: 'yyyy.mm.dd' }).datepicker('setDate', new Date (dateFrom));
            }
        });    
        $('#to').datepicker({
        format: 'yyyy.mm.dd',
        minDate: today,
        onSelect: function(dateTo){ 
            $("#from").datepicker({ minDate: today, maxDate: dateTo, format: 'yyyy.mm.dd' }).datepicker('setDate', new Date (dateTo));
            }
        });        
        /* Dates choice for search in trips */
        $('#query_from').datepicker({
        format: 'yyyy.mm.dd',
        onSelect: function(dateFrom){
            $("#query_to").datepicker({ minDate: dateFrom, format: 'yyyy.mm.dd' }).datepicker('setDate', new Date (dateFrom));
            }
        });    
        $('#query_to').datepicker({
        format: 'yyyy.mm.dd',
        onSelect: function(dateTo){ 
            $("#query_from").datepicker({ maxDate: dateTo, format: 'yyyy.mm.dd' }).datepicker('setDate', new Date (dateTo));
            }
        });        
    }
});

$(document).ready(function() {
  var scriptInterpreter;
  $( function() {
    $(".column" ).sortable({
      connectWith: ".column",
      handle: ".card-header",
      cancel: ".card-toggle",
      placeholder: "card-placeholder ui-corner-all"
    });

    $(".card" )
      .addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
      .find( ".card-header" )
        .addClass( "ui-widget-header ui-corner-all" )
        .prepend( "<span class='ui-icon ui-icon-minusthick card-toggle'></span>");

        $( ".card-toggle" ).on( "click", function() {
        var icon = $( this );
        icon.toggleClass( "ui-icon-minusthick ui-icon-plusthick" );
        icon.closest( ".card" ).find( ".card-content" ).toggle();
      });
  });
  $( function() {
    $( ".sortable" ).sortable();
    $( ".sortable" ).disableSelection();
  });
});

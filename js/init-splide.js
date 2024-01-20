document.addEventListener( 'DOMContentLoaded', function() {
  var housesSlider = new Splide( '#houses-slider', {
    autoWidth: true,
    autoHeight: true,
    gap: '50px',
    pagination: false
  });

  housesSlider.mount();

  var actionsSlider = new Splide( '#actions-slider', {
    autoWidth: true,
    autoHeight: true,
    gap: '50px',
    pagination: false
  });

  actionsSlider.mount();
} );
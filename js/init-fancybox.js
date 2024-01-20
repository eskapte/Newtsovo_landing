const slidePhotos = document.querySelectorAll(".slide__photos");

slidePhotos.forEach(carousel => {
  new Carousel(carousel, {
    'slidesPerPage' : 1,
    'preload' : '1'
  });
})

const offersSliders = document.querySelectorAll(".offers-slider");

offersSliders.forEach(carousel => {
  new Carousel(carousel, {
    'slidesPerPage' : 4,
    'preload' : '1'
  });
})

Fancybox.bind("[data-fancybox]", {
  // Your custom options
});

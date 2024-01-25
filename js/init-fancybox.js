const slidePhotos = document.querySelectorAll(".slide__photos");

slidePhotos.forEach(carousel => {
  new Carousel(carousel, {
    'slidesPerPage' : 1,
    'preload' : 0
  });
})

const ourProductsCarousel = document.querySelector(".our-products__carousel");
new Carousel(ourProductsCarousel, {
  'slidesPerPage': 1,
  'preload': 0
});

Fancybox.bind("[data-fancybox]", {
  // Your custom options
});

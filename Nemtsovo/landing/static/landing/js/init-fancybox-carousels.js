const slidePhotos = document.querySelectorAll(".slide__photos");

slidePhotos.forEach(carousel => {
  new Carousel(carousel, {
    'slidesPerPage' : 1,
    'center': false
  })
})
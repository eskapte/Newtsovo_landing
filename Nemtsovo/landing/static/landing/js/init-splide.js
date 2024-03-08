document.addEventListener('DOMContentLoaded', function () {
    const housesSlider = new Splide('#houses-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: false
    });

    housesSlider.mount();

    const wellnesTreatmentSlider = new Splide('#wellness-treatments-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: false
    });

    wellnesTreatmentSlider.mount();

    const actionsSlider = new Splide('#actions-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: false
    });

    actionsSlider.mount();

    const ourPetsSlider = new Splide('#our-pets-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: false
    });

    ourPetsSlider.mount();
});
document.addEventListener('DOMContentLoaded', function () {
    const housesSlider = new Splide('#houses-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: true,
        arrows: false,
        classes: {
            page: 'splide__pagination__page custom-pagination-page'
        }
    });

    housesSlider.mount();

    const wellnesTreatmentSlider = new Splide('#wellness-treatments-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: true,
        arrows: false,
        classes: {
            page: 'splide__pagination__page custom-pagination-page'
        }
    });

    wellnesTreatmentSlider.mount();

    const actionsSlider = new Splide('#actions-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: true,
        arrows: false,
        classes: {
            page: 'splide__pagination__page custom-pagination-page'
        }
    });

    actionsSlider.mount();

    const ourPetsSlider = new Splide('#our-pets-slider', {
        autoWidth: true,
        autoHeight: true,
        gap: '50px',
        pagination: true,
        arrows: false,
        classes: {
            page: 'splide__pagination__page custom-pagination-page'
        }
    });

    ourPetsSlider.mount();
});
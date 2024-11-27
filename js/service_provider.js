// Initialize the service provider slider
const slides = document.querySelectorAll('.slider .slide');
let currentSlide = 0;

function changeSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    const slider = document.querySelector('.slider');
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Change slides every 3 seconds
setInterval(changeSlide, 3000);

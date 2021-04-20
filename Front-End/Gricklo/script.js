let images = document.querySelectorAll('.properties-card');
let start = 0;

images[start].style.display = 'block';

document.querySelector('.next').addEventListener('click', () => {
    if (start == images.length - 1) {
        start = -1;
    }
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none'
    }
    images[++start].style.display = 'block'

});

document.querySelector('.prev').addEventListener('click', () => {
    start -= 1;
    if (start < 0) {
        start = images.length - 1
    }
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none'
    }
    images[start].style.display = 'block'

});

const moveSlider = () => {
    if (start == images.length - 1) {
        start = -1;
    }
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none'
    }
    images[++start].style.display = 'block'

}


setInterval(() => {
    moveSlider();
}, 3000);
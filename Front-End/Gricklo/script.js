let images = document.querySelectorAll('.properties-card');
let start = 4;

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

let slider2 = document.querySelectorAll('.video-about');
let begin = 1
slider2[1].style.display = 'none'
slider2[2].style.display = 'none'
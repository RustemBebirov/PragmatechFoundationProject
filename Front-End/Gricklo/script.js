let move = 0;
let sliderLine = document.querySelector('.slider-line');

document.querySelector('.next').addEventListener('click', () => {
    move += 480;
    if (move >= 1900) {
        move = 0

    }
    sliderLine.style.left = -move + 'px';
})

document.querySelector('.prev').addEventListener('click', () => {
    move -= 480;
    if (move < 0) {
        move = 1920
    }

    sliderLine.style.left = -move + 'px'

})


function autoplay(params) {
    let sliderLine2 = document.querySelector('.slider-line-2');
    sliderLine2.style.left = -575 + 'px'



}

setTimeout(() => {
    autoplay()
}, 1000);

window.addEventListener('scroll', () => {
    if (window.scrollY > window.innerHeight / 4 - document.querySelector('header').clientHeight) {
        document.querySelector('.main-header').classList.add('sticky-bar')
    } else {
        document.querySelector('.main-header').classList.remove('sticky-bar')
    }

})
let move = 0;
let sliderLine = document.querySelector('.slider-line');

document.querySelector('.next').addEventListener('click', () => {
    move += 480;
    if (move >= 1920) {
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

setInterval(() => {
    autoplay()
}, 1000);


window.addEventListener('scroll', () => {
    if (window.scrollY > window.innerHeight / 4 - document.querySelector('header').clientHeight) {
        document.querySelector('.main-header').classList.add('sticky-bar')
    } else {
        document.querySelector('.main-header').classList.remove('sticky-bar')
    }

})


let div = document.createElement('div');
div.setAttribute('id', 'back-top');
div.style.display = 'none'


let a = document.createElement('a');

a.setAttribute('title', 'Go to Tap')
a.setAttribute('href', '#')
a.classList.add('smooth')
a.style.color = 'white'
a.innerHTML = '<i class="fas fa-level-up-alt"></i>'
div.appendChild(a)

document.querySelector('body').appendChild(div);

window.addEventListener('scroll', () => {
    if (window.scrollY > window.innerHeight - document.querySelector('header').clientHeight) {
        div.style.display = 'block'

    } else {
        div.style.display = 'none'
    }
})

document.querySelector('.smooth').addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelector('header').scrollIntoView({
        behavior: 'smooth'
    });
})
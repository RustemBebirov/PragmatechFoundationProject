let move = 0;
let move1 = 0;
let sliderLine = document.querySelector('.slider-line');

document.querySelector('.next').addEventListener('click', () => {
    move += 474;
    if (move >= 1930) {
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

function auto(e) {
    move += 474;
    if (move >= 1930) {
        move = 0

    }

    sliderLine.style.left = -move + 'px';

}

setInterval(() => {

    auto()
}, 2000);


function autoplay(params) {
    let sliderLine2 = document.querySelector('.slider-line-2');
    move1 += 480;
    if (move1 > 1240) {
        move1 = 0
    }

    sliderLine2.style.left = -move1 + 'px'

}

setInterval(() => {
    autoplay()
}, 2000);


window.addEventListener('scroll', () => {
    if (window.scrollY > window.innerHeight / 4 - document.querySelector('header').clientHeight) {
        document.querySelector('.main-header').classList.add('sticky-bar')
        document.querySelector('nav').style.background = 'rgba(26, 33, 61, 0.8)'
    } else {
        document.querySelector('.main-header').classList.remove('sticky-bar')
        document.querySelector('nav').style.background = ''

    }

})




// back to top scroll
let div = document.createElement('div');
div.setAttribute('id', 'back-top');
div.style.display = 'none'
div.style.zIndex = 1;


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

//resposive nav

document.querySelector('.burger').addEventListener('click', () => {
    let nav = document.querySelector('nav')
    if (nav.style.display == 'none') {
        nav.style.display = 'block'
    } else {
        nav.style.display = 'none'
    }


})
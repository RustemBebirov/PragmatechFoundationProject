let block = document.createElement('div');

block.setAttribute('id', 'box')

block.setAttribute('style', 'width:500px;height:500px;background-color:red;display:flex;flex-wrap:wrap;')

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}



function setRandomColor() {
    $(".box1").css("background-color", getRandomColor());
}



for (let i = 0; i < 35; i++) {
    let miniblock = document.createElement('div');
    miniblock.setAttribute('style', 'width:50px;height:50px;margin-right:10px;margin-left:10px;margin-top:10px;background-color:blue')
    block.appendChild(miniblock);

    miniblock.addEventListener('click', (event) => {
        event.target.classList.add('box1');
        event.target = setRandomColor();
    })



}




document.querySelector('.container').appendChild(block);
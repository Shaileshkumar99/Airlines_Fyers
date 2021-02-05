const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
ctx.globalCompositeOperation = 'destination-over';

let number = 0;
let scale = 10;
let color = 0;

function drawFlower(){

    let angle = number * -1;
    let radius = scale * Math.sqrt(number);
    let positionX = radius * Math.sin(angle) + canvas.width/2;
    let positionY = radius * Math.cos(angle) + canvas.height/2;

    ctx.fillStyle = 'hsl(' + color + ', 100%, 50%';
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 3;
    ctx.beginPath()
    ctx.arc(positionX, positionY, 20,0, Math.PI * 2);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    number += 1;
    color += 1;
}

function animate(){


    drawFlower();
    if (number > 500){
        return ;
    }
    requestAnimationFrame(animate);
}
animate();
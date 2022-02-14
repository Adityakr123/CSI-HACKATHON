const slideImage = document.querySelectorAll('.slide-image');
const slider = document.querySelector('.slider');
const next = document.querySelector('.nextBtn');
const prev = document.querySelector('.prevBtn');
const navigation = document.querySelector('.navigation-dots');

function init(){
    slideImage.forEach((img,i) =>{
        img.style.left = i*100 + '%';
    });
    // slideImage[0].classList.add('active');
}
init();
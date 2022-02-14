var a = document.getElementsByClassName('image')
var counter =0;
var myImages=['Diabetes1.jpg','Heart1.jpg','Diabetes2.jpg','Heart2.jpg'];
setInterval(function next(){
    counter++;
    a.className = 'fideinimg';
    if(counter>4){
        counter=0;
        a.src=myImages[counter];
    }
    else{
        a.src=myImages[counter];
    }
},5000);
function next(){
    counter++;
    if(counter>4){
        counter=0;
        a.className='fideinimg';
        a.src=myImages[counter];
    }
    else{
        a.className='fideinimg';
        a.src=myImages[counter];
    }
}
function prev(){
    counter--;
    if(counter>4){
        counter=0;
        a.src=myImages[counter];
    }
    else if(counter<0){
        counter=4;
        a.src=myImages[counter];
    }
    else{
        a.src=myImages[counter];
    }
}

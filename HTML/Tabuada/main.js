const myform = document.querySelector('#my-form')
myform.addEventListener("submit", onSubmit)

function onSubmit(e){
   e.preventDefault();

var num = parseInt(document.getElementById('num').value);
while (i<=10){
    tabuada = num * i
    console.log(tabuada); 
}

document.getElementById('tabuada').innerHTML = tabuada;
}
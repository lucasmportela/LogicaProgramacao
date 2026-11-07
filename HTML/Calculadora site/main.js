
const myform = document.querySelector('#my-form')
myform.addEventListener("submit", onSubmit)

function onSubmit(e){
   e.preventDefault();

var operator = parseInt(document.getElementById('operator').value);
var first = parseFloat(document.getElementById('first').value);
var second = parseFloat(document.getElementById('second').value);
var result = parseFloat(document.getElementById('result').value);
 
if (operator == 1) 
{
       result =  first + second;
       console.log(result);  
}
else if (operator == 2) 
{
      result =  first - second;-
      console.log(result);  
}

else if (operator == 3) 
{
      result =  first * second;
      console.log(result);  
}

else if (operator == 4) 
{
       result =  first / second;
       console.log(result);  
}

document.getElementById('result').innerHTML = result;
}
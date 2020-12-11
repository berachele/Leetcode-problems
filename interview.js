//variables
var myDiv = document.getElementsByTagName('div')
var myButton = document.querySelector('button')

//eventListeners
myButton.addEventListener("click", function(){
    const currentColor = myDiv[0].style.backgroundColor
    myDiv[0].style.backgroundColor = currentColor === "red" ? "green" : "red"
})
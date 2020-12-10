var heading = document.getElementById('heading')
var paragraph = document.getElementsByTagName('p')
var par = Array.from(paragraph)

par.forEach(p => {p.addEventListener("click", function(){
    p.style.background = "purple"
})})

heading.addEventListener("mouseover", function(){heading.style.color = "yellow"})
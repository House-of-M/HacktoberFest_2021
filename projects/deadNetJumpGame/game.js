var character = document.getElementById("character");
var block= document.getElementById("block");
let jump =()=>{
character.classList.toggle("animate");
setTimeout(()=>{
character.classList.toggle("animate");
},1000)
}
document.addEventListener("click",jump);

var checkdead= setInterval(()=>{
    var charTop=parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    var blockLeft=parseInt(window.getComputedStyle(block).getPropertyValue("left"));
if(blockLeft<20 && blockLeft >0 && charTop>=150){
    alert("you loose");
    block.style.animation="none";
    block.style.display="none";

}
},10)
document.addEventListener('DOMContentLoaded', ()=>{
    const button = document.getElementById('button1')
    if(button) button.addEventListener('click', clickButton)
})

const clickButton = ()=>{
    alert("You pressed the button!");
}
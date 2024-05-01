function changeMessage() {
    let message = document.getElementById('js-content');
    
    //empting the message ...
    message.innerHTML = "";
    message.innerHTML = "I came from a JS file!"; //... so it can be resetted
}
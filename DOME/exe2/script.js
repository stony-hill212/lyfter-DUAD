let count= 0;

const counter= document.getElementById("counter");
const increaseButton= document.getElementById("increaseButton");
const decreaseButton= document.getElementById("decreaseButton");

increaseButton.addEventListener("click", function () {
    count++;
    counter.textContent= count;
    decreaseButton.disabled= false;
});
decreaseButton.addEventListener("click", function () {
    if (count>0) {
        count--;
        counter.textContent= count;
    }
    if (count===0) {decreaseButton.disabled= true;}
});
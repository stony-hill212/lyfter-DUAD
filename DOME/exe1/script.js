const enochText= document.getElementById("enochText");
const colorButton= document.getElementById("colorButton");

colorButton.addEventListener("click", function () {
    enochText.classList.toggle("revealed");
});
const colors= [
    "#7b1113",
    "#1f4ef5",
    "#55ea3b",
    "#e57711",
    "#3b6e4f"
]

const colorButton= document.getElementById("colorButton");
const enochText= document.getElementById("enochText");

colorButton.addEventListener("click", function () {
    const randomColor= colors[Math.floor(Math.random()*colors.length)];
    enochText.style.color= randomColor;
});

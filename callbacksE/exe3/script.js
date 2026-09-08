const colorBox= document.getElementById("colorBox");
const colorName= document.getElementById("colorName");
const colorButton= document.getElementById("colorButton");

const colors= [
    "red",
    "blue",
    "green",
    "yellow",
    "cyan",
    "pink"
];

function generateColor(callback) {
    const randomIndex= Math.floor(Math.random()*colors.length);
    const selectedColor= colors[randomIndex];
    callback(selectedColor);
}
function displayColor(color) {
    colorBox.style.backgroundColor= color;
    colorName.textContent= `Color: ${color}`;
}
colorButton.addEventListener("click", function () {
    generateColor(displayColor);
});
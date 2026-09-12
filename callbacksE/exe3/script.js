const colorBox= document.getElementById("colorBox");
const colorName= document.getElementById("colorName");
const colorButton= document.getElementById("colorButton");

const colors= [
    "#FF5733",
    "#33FF57",
    "#3357FF",
    "#F5FF33",
    "#FF33F6",
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

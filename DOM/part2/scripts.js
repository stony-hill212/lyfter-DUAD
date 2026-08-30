const userInput= document.getElementById("userInput");
const processButton= document.getElementById("processButton");
const displayText= document.getElementById("displayText");

let hasInformation= false;

processButton.addEventListener("click", function () {
    if (userInput.value.trim()!== "") {
        displayText.textContent= userInput.value;
        hasInformation= true;
    } else if (hasInformation) {
        userInput.value= "";
        displayText.textContent= "";
        hasInformation= false;
    }
});
const userInput= document.getElementById("userInput");
const processButton= document.getElementById("processButton");
const displayText= document.getElementById("displayText");

let hasInformation= false;

processButton.addEventListener("click", function () {
    if (userInput.value.trim()!== "") {
        displayText.textContent= userInput.value;
        userInput.value= "";
    } else if (displayText.textContent!== "") {
        displayText.textContent= "";
    }
});

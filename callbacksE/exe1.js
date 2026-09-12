function validateInput(number, successCallback, errorCallback) {
    if (number > 0) {
        successCallback(number);
    } else {errorCallback(number);}
}

function showSuccess(number) {
    console.log(`Valid number: ${number}`);
}
function showError(number) {
    console.log(`Invalid number: ${number}`);
}

validateInput(-10, showSuccess, showError);
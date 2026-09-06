function checkNumber(number, evenCallback, oddCallback) {
    if (number %2===0) {evenCallback();}
    else {oddCallback();}
}
function shownEven() {
    console.log("The number is even!");
}
function showOdd() {
    console.log("The number is odd!");
}
checkNumber(9, shownEven, showOdd);
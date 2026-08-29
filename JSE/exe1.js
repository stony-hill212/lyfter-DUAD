function reversedWord(word) {
    let reversed= "";
    for (let i=word.length-1; i>=0; i--) {
        reversed+= word[i];
    }
    return reversed
}
const result= reversedWord("JavaScript");
console.log(result);

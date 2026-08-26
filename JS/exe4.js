const sentence= "Ground and pound";
const words= [];
let currentWord= "";

for (const character of sentence) {
    if (character===" ") {
        words.push(currentWord);
        currentWord= "";
    } else {currentWord+=character;}
}
words.push(currentWord);
console.log(words);
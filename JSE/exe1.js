const word= "JavaScript";
let reversed= "";
for (let i= word.length-1; i>=0; i--) {
    console.log(i, word[i])
    reversed+= word[i];
}
console.log(reversed);
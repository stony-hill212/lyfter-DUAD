function countWords(sentence) {
    const normalizedSentence= sentence.toLowerCase();
    const cleanedSentence= normalizedSentence.replace(/[^\w\s]/g, "");
    const words= cleanedSentence.split(" ");
    const wordCount= {};
    for (const word of words) {
        if (wordCount[word]) {wordCount[word]++;}
        else {wordCount[word]= 1;}
    }
    return wordCount;
}
const sentence= "This is the Zodiac speaking. Read this letter...";
const result= countWords(sentence);

console.log(result);
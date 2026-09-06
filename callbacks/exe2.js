const fs= require("fs");

function compareLists(list1, list2, callback) {
    const repeatedWords= list1.filter(word => list2.includes(word));
    callback(repeatedWords);
}
fs.readFile("list1.txt", "utf-8", (error, data1)=> {
    if (error) {
        console.log("Error reading list1.txt");
        return;
    }
    fs.readFile("list2.txt", "utf-8", (error, data2)=> {
        if (error) {
            console.log("Error reading list2.txt");
            return;
        }
        const list1= data1.split(/\r?\n/).map(word=>word.trim());
        const list2= data2.split(/\r?\n/).map(word=>word.trim());
        compareLists(list1, list2, (repeatedWords)=> {
            console.log("Repeated words:");
            repeatedWords.forEach(word=> {console.log(word);});
            console.log("Hidden message:", repeatedWords.join(" "));
        });
    });
});
const word1= new Promise(resolve=> {
    setTimeout(()=> {
        resolve("very");
    }, 300);
});

const word2= new Promise(resolve=> {
    setTimeout(()=> {
        resolve("dogs");
    }, 100);
});

const word3= new Promise(resolve=> {
    setTimeout(()=> {
        resolve("cute");
    }, 400);
});

const word4= new Promise(resolve=> {
    setTimeout(()=> {
        resolve("are");
    }, 200);
});

Promise.all([word1, word2, word3, word4]).then(words=> {
    console.log(`${words[1]} ${words[3]} ${words[0]} ${words[2]}`);
});
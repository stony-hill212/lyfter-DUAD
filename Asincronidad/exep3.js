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
    const sentence= `${words[1][0].toUpperCase()}${words[1].slice(1)} ${words[3]} ${words[0]} ${words[2]}`;
    console.log(sentence);
});

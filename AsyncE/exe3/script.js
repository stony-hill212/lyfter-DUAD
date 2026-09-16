const messages= document.getElementById("messages");

function wait(seconds) {
    return new Promise((resolve)=> {
        setTimeout(()=> {
            resolve(`It's been ${seconds} seconds`);
        }, seconds *1000);
    });
}

async function runWaits() {
    const message1= await wait(2);
    console.log(message1);
    messages.innerHTML+= `<p>${message1}</p>`;

    const message2= await wait(3);
    console.log(message2);
    messages.innerHTML+= `<p>${message2}</p>`;

    const message3= await wait(1);
    console.log(message3);
    messages.innerHTML+= `<p>${message3}</p>`;
}

runWaits();
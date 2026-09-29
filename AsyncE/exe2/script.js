const loadButton= document.getElementById("loadButton");
const status= document.getElementById("status");
const resources= document.getElementById("resources");

function loadResource(resourceName, time) {
    return new Promise((resolve)=> {
        setTimeout(()=> {
            resolve(`${resourceName} loaded successfully`);
        }, time);
    });
}

function displayResource(message) {
    const resource= document.createElement("div");
    resource.classList.add("resource");
    resource.textContent= message;
    resources.appendChild(resource);
}

async function LoadWebsite() {
    resources.innerHTML= "";
    status.textContent= "Starting website loading...";
    try {
        status.textContent= "loading images...";
        const images= await Promise.all([
            loadResource("Image1", 2000),
            loadResource("Image2", 1000),
            loadResource("Image3", 1500)
        ]);
        images.forEach(displayResource);
        status.textContent= "Loading scripts...";
        const script1= await loadResource("Script 1", 2000);
        displayResource(script1);
        const script2= await loadResource("Script 2", 1500);
        displayResource(script2);
        const script3= await loadResource("Script 3", 1000);
        displayResource(script3);
        status.textContent= "The website has fully loaded.";
    } catch (error) {
        status.textContent= "Something went wrong.";
        console.log(error);
    }
}

loadButton.addEventListener("click", LoadWebsite);
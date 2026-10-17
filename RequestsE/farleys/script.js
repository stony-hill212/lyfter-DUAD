const productsContainer= document.getElementById("products");
const previousButton= document.getElementById("previousButton");
const nextButton= document.getElementById("nextButton");
const pageNumber= document.getElementById("pageNumber");

let products= [];
let currentPage= 1;

const productsPerPage= 5;

async function getProducts() {
    try{
        const response= await axios.get("https://api.restful-api.dev/objects");
        products= response.data;
        displayProducts();
    } catch(error) {
        productsContainer.innerHTML= "<p>Sorry, we couldn't load the products. Please try again.</p>";
        console.error(error);
    }
}

function displayProducts() {
    productsContainer.innerHTML= "";
    if (products.length===0) {
        productsContainer.textContent= "No products found.";
        pageNumber.textContent= "Page 0";
        updateButtons();
        return;
    }
    const startIndex= (currentPage- 1)* productsPerPage;
    const endIndex= startIndex+productsPerPage;
    const productsToDisplay= products.slice(startIndex, endIndex);
    productsToDisplay.forEach((product)=> {
        const productCard= document.createElement("div");
        productCard.classList.add("product-card");
        const productName= document.createElement("h2");
        productName.textContent= product.name ?? "Unnamed product";
        const productId= document.createElement("p");
        const idLabel= document.createElement("strong");
        idLabel.textContent= "ID: ";
        productId.appendChild(idLabel);
        productId.appendChild(document.createTextNode(product.id ?? "No ID available"));
        productCard.appendChild(productName);
        productCard.appendChild(productId);
        if (product.data!= null) {
            const detailsLabel= document.createElement("p");
            detailsLabel.textContent= "Details:";
            const details= document.createElement("pre");
            details.textContent= JSON.stringify(product.data, null, 2);
            productCard.appendChild(detailsLabel);
            productCard.appendChild(details);
        }
        productsContainer.appendChild(productCard);
    });
    pageNumber.textContent= `Page ${currentPage}`;
    updateButtons();
}

function updateButtons() {
    previousButton.disabled= currentPage===1;
    const totalPages= Math.ceil(products.length/productsPerPage);
    nextButton.disabled= currentPage=== totalPages;
}

previousButton.addEventListener("click", ()=> {
    if (currentPage>1) {
        currentPage--;
        displayProducts();
    }
});

nextButton.addEventListener("click", ()=> {
    const totalPages= Math.ceil(products.length/productsPerPage);
    if (currentPage<totalPages) {
        currentPage++;
        displayProducts();
    }
});

getProducts();
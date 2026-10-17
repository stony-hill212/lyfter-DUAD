const loadProductsButton= document.getElementById("loadProducts");
const productsContainer= document.getElementById("products");
const message= document.getElementById("message");
const addProductButton= document.getElementById("addProduct");
const addMessage= document.getElementById("addMessage");
const productIdInput= document.getElementById("productId");
const findProductButton= document.getElementById("findProduct");
const foundProduct= document.getElementById("foundProduct");
const findMessage= document.getElementById("findMessage");
const updateProductId= document.getElementById("updateProductId");
const updateProductName= document.getElementById("updateProductName");
const updateProductColor= document.getElementById("updateProductColor");
const updateProductButton= document.getElementById("updateProduct");
const updateMessage= document.getElementById("updateMessage");

function createProductCard(product) {
    const productElement= document.createElement("div");
    productElement.classList.add("product");
    const title= document.createElement("h2");
    title.textContent= product.name;
    const idParagraph= document.createElement("p");
    const idLabel= document.createElement("strong");
    idLabel.textContent= "ID: ";
    idParagraph.appendChild(idLabel);
    idParagraph.appendChild(document.createTextNode(product.id));
    const dataParagraph= document.createElement("p");
    const dataLabel= document.createElement("strong");
    dataLabel.textContent= "Data: ";
    dataParagraph.appendChild(dataLabel);
    dataParagraph.appendChild(document.createTextNode(JSON.stringify(product.data ?? {})));
    productElement.appendChild(title);
    productElement.appendChild(idParagraph);
    productElement.appendChild(dataParagraph);
    return productElement;
}

async function getProducts() {
    try {
        const response= await fetch("https://api.restful-api.dev/objects");
        if (!response.ok) {
            throw new Error("Could not load the products.");
        }
        const products= await response.json();
        const productsWithData= products.filter(product=> product.data);
        productsContainer.innerHTML= "";
        productsWithData.forEach(product=> {
            const productElement= createProductCard(product);
            productsContainer.appendChild(productElement);
        });
        if (productsWithData.length=== 0) {
            message.textContent= "No products with available data were found.";
        } else {
            message.textContent= "";
        }
    } catch (error) {
        message.textContent= "Something went wrong while loading the products.";
        console.log(error);
    }
}

async function createProduct(product) {
    const response= await fetch("https://api.restful-api.dev/objects", {
        method:"POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(product)
    });
    if (!response.ok) {throw new Error("Could not create the product.");}
    const createdProduct= await response.json();
    return createdProduct;
}

const boxingGloves= {
    name: "Heavyweight Boxing Gloves",
    data: {
        brand: "ONX",
        size: "16 oz/XL",
        color: "Black",
        material: "Leather",
        weight: "16 oz"
    }
};

async function getProductById(id) {
    const response= await fetch(`https://api.restful-api.dev/objects/${id}`);
    if (!response.ok) {
        throw new Error("Product not found.");
    }
    const product= await response.json();
    return product;
}

async function updateProduct(id, updatedInfo) {
    const response= await fetch(
        `https://api.restful-api.dev/objects/${id}`,
        {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(updatedInfo)
        }
    );
    if (!response.ok) {
        throw new Error("Could not update the product.");
    }
    const updatedProduct= await response.json();
    return updatedProduct;
}


loadProductsButton.addEventListener("click", getProducts);

addProductButton.addEventListener("click", async()=> {
    try {
        const createdProduct= await createProduct(boxingGloves);
        addMessage.textContent= `Product "${createdProduct.name}" was created successfully.`;
        console.log(createdProduct);
    } catch (error) {
        addMessage.textContent= "Something went wrong while creating the product.";
        console.error(error);
    }
});

findProductButton.addEventListener("click", async()=> {
    const id=productIdInput.value.trim();
    if (!id) {
        findMessage.textContent= "Please enter a product ID.";
        return;
    }
    try {
        const product= await getProductById(id); 
        foundProduct.replaceChildren(createProductCard(product));
        findMessage.textContent= "";
    } catch (error) {
        foundProduct.replaceChildren();
        findMessage.textContent= "Product not found.";
        console.log(error)
    }
});

updateProductButton.addEventListener("click", async()=> {
    const id= updateProductId.value.trim();
    const newName= updateProductName.value.trim();
    const newColor= updateProductColor.value.trim();

    if (!id || !newName || !newColor) {
        updateMessage.textContent= "Please complete all the fields.";
        return;
    }
    try {
        const product= await getProductById(id);
        const updatedInfo= {
            ...product,
            name: newName,
            data: {
                ...product.data,
                color: newColor
            }
        };
        const updatedProduct= await updateProduct(id, updatedInfo);
        updateMessage.textContent= `Product "${updatedProduct.name}" was updated successfully`;
        console.log(updatedProduct);
    } catch (error) {
        updateMessage.textContent= "Something went wrong while updating the product.";
        console.error(error);
    }
});

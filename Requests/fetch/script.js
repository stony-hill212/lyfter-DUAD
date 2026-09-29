const LoadProductsButton= document.getElementById("loadProducts");
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
            const productElement= document.createElement("div");
            productElement.classList.add("product");
            productElement.innerHTML= `
                <h2>${product.name}</h2>
                <p><strong>ID:</strong> ${product.id}</p>
                <p><strong>Data:</strong> ${JSON.stringify(product.data)}</p>
            `;
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
    try {
        const response= await fetch("https://api.restful-api.dev/objects", {
            method:"POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(product)
        });
        if (!response.ok) {throw new Error("Could not create the product.");}
        const createdProduct= await response.json();
        addMessage.textContent= `Product "${createdProduct.name}" was created successfully`;
        console.log(createdProduct);
    } catch (error) {
        addMessage.textContent= "Something went wrong while creating the product.";
        console.error(error);
    }
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



LoadProductsButton.addEventListener("click", getProducts);
addProductButton.addEventListener("click", ()=> {
    createProduct(boxingGloves);
});

findProductButton.addEventListener("click", async()=> {
    const id=productIdInput.value.trim();
    if (!id) {
        findMessage.textContent= "Please enter a product ID.";
        return;
    }
    try {
        const product= await getProductById(id); 
        foundProduct.innerHTML= `
            <div class="product">
                <h2>${product.name}</h2>
                <p><strong>ID:</strong> ${product.id}</p>
                <p><strong>Data:</strong> ${JSON.stringify(product.data)}</p>
            </div>
        `;
        findMessage.textContent= "";
    } catch (error) {
        foundProduct.innerHTML= "";
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
    const updatedInfo= {
        name: newName,
        data: {
            brand: "ONX",
            size: "XL/16 oz",
            color: newColor,
            material: "Leather",
            weight: "16 oz"
        }
    };
    try {
        const updatedProduct= await updateProduct(id, updatedInfo);
        updateMessage.textContent= `Product "${updatedProduct.name}" was updated successfully`;
        console.log(updatedProduct);
    } catch (error) {
        updateMessage.textContent= "Something went wrong while updating the product.";
        console.error(error);
    }
});
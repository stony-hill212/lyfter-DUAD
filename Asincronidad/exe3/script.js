const userIdInput= document.getElementById("userId");
const searchButton= document.getElementById("searchButton");
const result= document.getElementById("result");

async function getUser() {
    console.log("Button works");
    const userId= userIdInput.value;
    if (!userId) {
        result.innerHTML= '<p class="error">Please enter a user ID.</p>';
        return;
    }
    try {
        result.textContent= "Searching...";
        const response= await fetch(`https://reqres.in/api/users/${userId}`);
        if (!response.ok) {throw new Error("User not found");}
        const user= await response.json();
        result.innerHTML= `
            <div class="user-card">
                <img src="${user.data.avatar}" alt="User avatar">
                <h2>${user.data.first_name} ${user.data.last_name}</h2>
                <p>${user.data.email}</p>
            </div>
        `;
    } catch (error) {
        result.innerHTML= `<p class="error">The user was not found.</p>`;
    }
}
searchButton.addEventListener("click", getUser);
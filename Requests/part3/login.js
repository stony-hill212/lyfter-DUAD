const loginForm= document.getElementById("loginForm");
const userIdInput= document.getElementById("userId");
const passwordInput= document.getElementById("password");
const loginMessage= document.getElementById("loginMessage");

async function loginUser(id, password) {
    const response= await axios.get(
        `https://api.restful-api.dev/objects/${id}`
    );
    const user= response.data;
    if (user.data?.password !==password) {
        throw new Error("Invalid ID or password.");
    }
    return user;
}

loginForm.addEventListener("submit", async(event)=> {
    event.preventDefault();
    const id= userIdInput.value.trim();
    const password= passwordInput.value;
    if (!id || !password) {
        loginMessage.textContent= "Please enter your ID and password.";
        return;
    }
    try {
        const user= await loginUser(id, password);
        localStorage.setItem("currentUser", JSON.stringify(user));
        window.location.href= "profile.html";
    } catch(error) {
        loginMessage.textContent= "Login failed. Please check your ID and password.";
        console.error(error);
    }
});
const savedUser= localStorage.getItem("currentUser");
if (savedUser) {window.location.href= "profile.html";}
const registerForm= document.getElementById("registerForm");
const nameInput= document.getElementById("name");
const emailInput= document.getElementById("email");
const passwordInput= document.getElementById("password");
const registerMessage= document.getElementById("registerMessage");

async function registerUser(userInfo) {
    const response= await axios.post(
        "https://api.restful-api.dev/objects", userInfo
    );
    return response.data;
}
registerForm.addEventListener("submit", async(event)=> {
    event.preventDefault();
    const userInfo= {
        name: nameInput.value.trim(),
        data: {
            email: emailInput.value.trim(),
            password: passwordInput.value
        }
    };
    try {
        const registeredUser= await registerUser(userInfo);
        localStorage.setItem("currentUser", JSON.stringify({id: registeredUser.id}));
        alert(`User created successfully! Your ID is <${registeredUser.id}>.`);
        window.location.href= "profile.html";
        console.log(registeredUser);
    } catch (error) {
        registerMessage.textContent= "Registration failed. Please try again.";
        console.error(error);
    }
});

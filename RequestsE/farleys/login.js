const API_URL= "https://api.restful-api.dev/objects";

const loginForm= document.getElementById("loginForm");
const profileIdInput= document.getElementById("profileIdInput");
const loginButton= document.getElementById("loginButton");
const loginMessage= document.getElementById("loginMessage");

function showLoginMessage(text, type) {
    loginMessage.textContent= text;
    loginMessage.className= type;
}

function getLoginErrorMessage(error) {
    if (error.response?.status===404) {
        return "Profile not found. Please check your profile ID.";
    }
    if (error.response?.data?.message) {
        return error.response.data.message;
    }
    if (error.response) {
        return `Login failed. Server returned status ${error.response.status}.`;
    }
    return "Unable to connect to the API. Please try again.";
}

const savedMessage= sessionStorage.getItem("sessionMessage");
if (savedMessage) {
    showLoginMessage(savedMessage, "error");
    sessionStorage.removeItem("sessionMessage");
}
loginForm.addEventListener("submit", async(event)=> {
    event.preventDefault();
    const userId= profileIdInput.value.trim();
    if (!userId) {
        showLoginMessage("Please enter your profile ID.", "error");
        return;
    }
    loginButton.disabled= true;
    showLoginMessage("Checking profile...", "");
    try {
        const response= await axios.get(`${API_URL}/${userId}`);
        createSession(response.data.id);
        window.location.href= "profile.html";
    } catch (error) {
        showLoginMessage(getLogin)
    }
})
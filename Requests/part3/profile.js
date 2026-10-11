const profileInfo= document.getElementById("profileInfo");
const logoutButton= document.getElementById("logoutButton");
const profileMessage= document.getElementById("profileMessage");

async function getUserById(id) {
    const response= await axios.get(`https://api.restful-api.dev/objects/${id}`);
    return response.data;
}

async function loadProfile() {
    const savedUser= localStorage.getItem("currentUser");
    if (!savedUser) {
        window.location.href= "login.html";
        return;
    }
    try {
        const session= JSON.parse(savedUser);
        if (!session.id) {
            localStorage.removeItem("currentUser");
            window.location.href= "login.html"
            return;
        }
        const user= await getUserById(session.id);
        const profileCard= document.createElement("div");
        profileCard.classList.add("profile-info");
        const nameHeading= document.createElement("h3");
        nameHeading.textContent= user.name;
        const idParagraph= document.createElement("p");
        const idLabel= document.createElement("strong");
        idLabel.textContent= "User ID: ";
        idParagraph.appendChild(idLabel);
        idParagraph.appendChild(document.createTextNode(user.id));
        const emailParagraph= document.createElement("p");
        const emailLabel= document.createElement("strong");
        emailLabel.textContent= "Email: ";
        emailParagraph.appendChild(emailLabel);
        emailParagraph.appendChild(document.createTextNode(user.data?.email ?? "Not provided"));
        profileCard.appendChild(nameHeading);
        profileCard.appendChild(idParagraph);
        profileCard.appendChild(emailParagraph);
        profileInfo.replaceChildren(profileCard);
    } catch (error) {
        profileMessage.textContent= "Could not load your profile.";
        console.error(error);
    }
}
loadProfile();

logoutButton.addEventListener("click", ()=> {
    localStorage.removeItem("currentUser");
    window.location.href= "login.html";
});

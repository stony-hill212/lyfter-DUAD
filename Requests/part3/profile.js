const profileInfo= document.getElementById("profileInfo");
const logoutButton= document.getElementById("logoutButton");
const profileMessage= document.getElementById("profileMessage");

const savedUser= localStorage.getItem("currentUser");
if (!savedUser) {window.location.href= "login.html";}
else {
    const user= JSON.parse(savedUser);
    profileInfo.innerHTML= `
        <div class="profile-info">
            <h3>${user.name}</h3>
            <p><strong>User ID:</strong> ${user.id}</p>
            <p><strong>Email:</strong> ${user.data.email}</p>
        </div>
    `;
}

logoutButton.addEventListener("click", ()=> {
    localStorage.removeItem("currentUser");
    window.location.href= "login.html";
});
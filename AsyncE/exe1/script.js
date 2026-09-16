const startButton= document.getElementById("startButton");
const userContainer= document.getElementById("userContainer");
const status= document.getElementById("status");

async function getUser(userId) {
    const response= await fetch(`https://reqres.in/api/users/${userId}`);
    if (!response.ok) {
        throw new Error(`Request for user ${userId} failed.`);
    }
    const data= await response.json();
    return data.data;
}

function displayUser(user) {
    const userCard= document.createElement("div");
    userCard.classList.add("user-card");
    userCard.innerHTML= `
        <img src="${user.avatar}" alt="${user.first_name}">
        <div class="user-info"> 
            <h2>${user.first_name} ${user.last_name}</h2>
            <p>${user.email}</p>
        </div>
    `;
    usersContainer.appendChild(userCard);
}

async function getUsersSequentially() {
    usersContainer.innerHTML= "";
    status.textContent= "Starting requests...";
    try {
        status.textContent= "Requesting user 2...";
        const user2= await getUser(2);
        displayUser(user2);
        status.textContent= "User 2 completed. Requesting user 3...";
        const user3= await getUser(3);
        displayUser(user3);
        status.textContent= "User 3 completed. Requesting user 4...";
        const user4= await getUser(4);
        displayUser(user4);
        status.textContent= "All users retrieved";
    } catch (error) {
        status.textContent= error.message;
        console.error(error);
    }
}

startButton.addEventListener("click", getUsersSequentially);
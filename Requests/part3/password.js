const passwordForm= document.getElementById("passwordForm");
const userIdInput= document.getElementById("userId");
const currentPasswordInput= document.getElementById("currentPassword");
const newPasswordInput= document.getElementById("newPassword");
const confirmPasswordInput= document.getElementById("confirmPassword");
const passwordMessage= document.getElementById("passwordMessage");

async function getUserById(id) {
    const response= await axios.get(`https://api.restful-api.dev/objects/${id}`);
    return response.data;
}

async function updatePassword(id, updatedInfo) {
    const response= await axios.put(
        `https://api.restful-api.dev/objects/${id}`,
        updatedInfo
    );
    return response.data;
}

passwordForm.addEventListener("submit", async(event)=> {
    event.preventDefault();
    const id= userIdInput.value.trim();
    const currentPassword= currentPasswordInput.value;
    const newPassword= newPasswordInput.value;
    const confirmPassword= confirmPasswordInput.value;    
    passwordMessage.textContent= "";
    if (!id || !currentPassword || !newPassword || !confirmPassword) {
        passwordMessage.textContent= "Please complete all the fields.";
        return;
    }
    const savedUser= localStorage.getItem("currentUser");
    if (!savedUser) {
        window.location.href= "login.html";
        return;
    }
    const session= JSON.parse(savedUser);
    if (session.id!== id) {
        passwordMessage.textContent= "You can only change your own password.";
        return;
    }
    if (newPassword!== confirmPassword) {
        passwordMessage.textContent= "The new passwords do not match.";
        return;
    }
    if (newPassword=== currentPassword) {
        passwordMessage.textContent= "Your new password must be different from the current password.";
        return;
    }
    try {
        const user= await getUserById(id);
        if (user.data?.password!== currentPassword) {
            passwordMessage.textContent= "Incorrect current password.";
            return;
        }
        const updatedInfo= {
            ...user,
            data: {
                ...user.data,
                password: newPassword
            }
        };
        const updatedUser= await updatePassword(id, updatedInfo);
        console.log("Updated user:", updatedUser);
        const verifiedUser= await getUserById(id);
        console.log("Verified user:", verifiedUser);
        console.log("User data:", verifiedUser.data);
        console.log("Email:", verifiedUser.data?.email);
        if (verifiedUser.data?.password!== newPassword) {
            passwordMessage.textContent= "The API did not confirm the password update.";
            return;
        }
        passwordMessage.textContent= "Password changed successfully.";
    } catch (error) {
        if (error.response?.status===404) {
            passwordMessage.textContent= "No user was found with that ID.";
        } else {
            passwordMessage.textContent= "Could not change the password. Please try again later.";
        }
        console.error(error);
    }
});

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

async function updatePassword(id, newPassword) {
    const response= axios.patch(
        `https://api.restful-api.dev/objects/${id}`,
        {
            data: {password: newPassword}
        }
    );
    return response.data;
}

passwordForm.addEventListener("submit", async(event)=> {
    event.preventDefault();
    const id= userIdInput.value.trim();
    const currentPassword= currentPasswordInput.value;
    const newPassword= newPasswordInput.value;
    const confirmPassword= confirmPasswordInput.value;
    try {
        const user= await getUserById(id);
        if (user.data?.password!== currentPassword) {
            passwordMessage.textContent= "Incorrect password.";
            return;
        }
        if (newPassword!== confirmPassword) {
            passwordMessage.textContent= "The new passwords do not match.";
            return;
        }
        const updatedUser= await updatePassword(id, newPassword);
        localStorage.setItem("currentUser", JSON.stringify(updatedUser));
        passwordMessage.textContent= "Password changed successfully";
        console.log(updatedUser);
    } catch(error) {
        passwordMessage.textContent= "Could not change the password. Check user ID and try again.";
        console.error(error);
    }
});
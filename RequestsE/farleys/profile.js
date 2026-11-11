const session= requireValidSession();

if (session) {
    const API_URL= "https://api.restful-api.dev/objects";
    const profileId= session.id;
    const profileName= document.getElementById("profileName");
    const profileAddress= document.getElementById("profileAddress");
    const editButton= document.getElementById("editButton");
    const editForm= document.getElementById("editForm");
    const nameInput= document.getElementById("nameInput");
    const addressInput= document.getElementById("addressInput");
    const cancelButton= document.getElementById("cancelButton");
    const saveButton= document.getElementById("saveButton");
    const message= document.getElementById("message");

    let profile= null;

    function showMessage(text, type) {
        message.textContent= text;
        message.className= type;
    }
    function getErrorMessage(error) {
        if (error.response?.data?.message) {
            return error.response.data.message;
        }
        if (error.response?.status===404) {
            return "Profile not found. Please check the profile ID.";
        }
        if (error.response) {
            return `Request failed with status ${error.response.status}.`;
        }
        return "Unable to connect to the API. Please try again.";
    }
    function displayProfile() {
        profileName.textContent= profile.name ?? "Not provided";
        profileAddress.textContent= profile.data.address ?? "Not provided";
    }
    async function getProfile() {
        try {
            const response= await axios.get(`${API_URL}/${profileId}`);
            profile= response.data;
            displayProfile();
            editButton.disabled= false;
        } catch (error) {
            showMessage(getErrorMessage(error), "error");
            console.error(error);
        }
    }

    editButton.addEventListener("click", ()=> {
        nameInput.value= profile.name ?? "";
        addressInput.value= profile.data?.address ?? "";
        editForm.hidden= false;
        showMessage("", "");
    });

    cancelButton.addEventListener("click", ()=> {
        editForm.hidden= true;
        editForm.reset();
        showMessage("", "");
    });

    editForm.addEventListener("submit", async(event)=> {
        event.preventDefault();
        const updatedName= nameInput.value.trim();
        const updatedAddress= addressInput.value.trim();
        if (!updatedName || !updatedAddress) {
            showMessage("Name and address are required.", "error");
            return;
        }
        saveButton.disabled= true;
        try {
            const updatedData= {
                ...(profile.data ?? {}),
                address: updatedAddress
            };
            const response= await axios.patch(
                `${API_URL}/${profileId}`,
                {
                    name: updatedName,
                    data: updatedData
                }
            );
            profile= response.data;
            displayProfile();
            editForm.hidden= true;
            showMessage("Profile updated successfully.", "success");
        } catch (error) {
            showMessage(getErrorMessage(error), "error");
            console.error(error);
        } finally {saveButton.disabled= false;}
    });

    getProfile();
}
async function getUser() {
    try {
        const response= await fetch("https://reqres.in/api/users/23");
        if (!response.ok) {
            throw new Error("User was not found");
        }
        const user= await response.json();
        console.log(user);
    } catch (error) {
        console.log("The user was not found");
    }
}
getUser();
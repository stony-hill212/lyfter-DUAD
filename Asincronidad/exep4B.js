fetch("https://reqres.in/api/users/23").then(response=> {
    if (!response.ok) {throw new Error("User not found");}
    return response.json();
}).then(user=> {
    console.log(user);
}).catch(error=> {
    console.log("Something went wrong:", error)
}).finally(()=> {
    console.log("Request finished.");
});
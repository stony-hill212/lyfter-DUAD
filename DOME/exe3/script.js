const taskInput= document.getElementById("taskInput");
const addButton= document.getElementById("addButton");
const taskList= document.getElementById("taskList");

addButton.addEventListener("click", function () {
    const taskText= taskInput.value.trim();
    if (taskText=== "") {return;}
    const listItem= document.createElement("li");
    listItem.textContent= taskText;
    const deleteButton= document.createElement("button");
    deleteButton.textContent= "Delete";
    deleteButton.addEventListener("click", function() {listItem.remove();});
    listItem.appendChild(deleteButton);
    taskList.appendChild(listItem);
    taskInput.value= "";
});
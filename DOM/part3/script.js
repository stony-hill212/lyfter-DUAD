const employeeOptions= document.querySelectorAll('input[name="employee"]');
const employeeField= document.getElementById("employeeField");

employeeOptions.forEach(function (option) {
    option.addEventListener("change", function () {
        if (option.value=== "yes") {
            employeeField.classList.remove("hidden");
        } else {employeeField.classList.add("hidden");}
    });
});
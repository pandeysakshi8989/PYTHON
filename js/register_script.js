// Function to show the registration form and update the role
function showForm(role) {
    // Set the role name in the form header
    const roleName = {
        student: "Student",
        serviceProvider: "Service Provider",
        infoProvider: "Information Provider",
        admin: "Admin"
    };

    // Change the displayed role
    document.getElementById("role-name").innerText = roleName[role];

    // Show the registration form
    document.getElementById("registration-form").style.display = "block";
}

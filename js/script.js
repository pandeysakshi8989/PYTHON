document.getElementById('register-button').onclick = function() {
    document.getElementById('register-modal').style.display = 'block';
}

document.querySelector('.close').onclick = function() {
    document.getElementById('register-modal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target === document.getElementById('register-modal')) {
        document.getElementById('register-modal').style.display = 'none';
    }
}

// Handle form submissions (you can add your own logic here)
document.getElementById('login-form').onsubmit = function(event) {
    event.preventDefault();
    // Add your login logic here
    alert('Login submitted');
}

document.getElementById('register-form').onsubmit = function(event) {
    event.preventDefault();
    // Add your registration logic here
    alert('Registration submitted');
}

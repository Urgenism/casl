document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');
    const errorMessage = document.getElementById('errorMessage');

    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Event listener for login button
    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();  // Prevent form submission

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (!emailRegex.test(email)) {
            errorMessage.textContent = 'Please enter a valid email.';
            return;
        }

        if (password.length < 6) {
            errorMessage.textContent = 'Password must be at least 6 characters long.';
            return;
        }

        // Clear error message
        errorMessage.textContent = '';

        // Simulate redirection to the dashboard upon valid login
        window.location.href = '/dashboard';  // Adjust as necessary
    });

    // Event listener for register button
    registerBtn.addEventListener('click', () => {
        window.location.href = '/register';  // Redirect to register page
    });
});

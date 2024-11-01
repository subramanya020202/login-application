function submitLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        const message = document.getElementById('message');
        if (data.message === "Login successful!") {
            message.style.color = 'green';
        } else {
            message.style.color = 'red';
        }
        message.textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
}


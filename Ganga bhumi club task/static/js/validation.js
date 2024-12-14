const API_BASE_URL = "https://flask-app.onrender.com"; // Replace with your Flask URL

fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email_or_mobile, password })
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        alert("Login successful!");
    } else {
        alert("Login failed!");
    }
})
.catch(error => console.error("Error:", error));

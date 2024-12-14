# Ganga bhumi club task
 a simple signup/login page with error handling and valiations.

# Flask Web App - Local Setup Guide

This guide explains how to set up and run the Flask web application locally on your machine.(As i am not able to deploy this webapp)

## Prerequisites
Before running the application, ensure you have the following installed on your system:

1. **Python 3.7+**
2. **pip** (Python package manager)
3. **SQLite** (usually included with Python)

## Steps to Run Locally

### 1. Clone the Repository
Download the project files by cloning the repository or downloading it as a ZIP file:
```bash
git clone <repository-url>
cd <repository-folder>
```


### 2. Install Dependencies
Install the required Python libraries using `pip`:
```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not available, manually install the libraries:
```bash
pip install flask werkzeug flask-cors
```


### 3. Run the Application
Start the Flask development server:
```bash
python app.py
```
The application will start running on `http://127.0.0.1:5000` by default.

### 4. Access the Application
Open a browser and navigate to:
```
http://127.0.0.1:5000
```

### 5. Stopping the Application
Press `Ctrl+C` in the terminal to stop the Flask server.

## Project Structure
```
├── app.py                 # Main Flask application
├── templates/             # HTML files
│   ├── signup.html
│   ├── login.html
│   └── welcome.html
├── static/                # Static assets
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── validation.js
├── users.db               # SQLite database (auto-created after init_db)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

## Features
- **User Registration:** Allows users to sign up with email/mobile and password.
- **User Login:** Validates credentials and redirects to the welcome page.
- **Validation:** Frontend and backend validation for email, mobile number, and password.
- **Error Handling:** Flash messages for invalid inputs or errors.

## Troubleshooting

### Common Issues
1. **Error:** `ModuleNotFoundError: No module named '<module>'`
   - Install the missing module using `pip install <module>`.

2. **Database Not Found:**
   - Ensure you initialized the database using the `init_db()` function.


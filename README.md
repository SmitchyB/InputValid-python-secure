InputValid-dotnet-secure - Python Flask Secure Build
Purpose
This repository contains the Secure Build of the Python Flask application, developed as part of a comparative study on secure coding practices across different development stacks. This build demonstrates the implementation of recommended secure coding techniques to mitigate common web application vulnerabilities.

Vulnerability Focus
This application specifically addresses the mitigation of three critical and pervasive web application vulnerabilities:

Improper Input Validation: Ensuring all user input is thoroughly checked and sanitized on the server-side to prevent malicious data from entering the system.
Insecure Secrets Management: Securely handling sensitive information like API keys and credentials, avoiding hardcoded values.
Insecure Error Handling: Preventing the exposure of sensitive internal information through verbose error messages.
Key Secure Coding Practices Implemented
Input Validation: All user inputs submitted to the /signup endpoint are subjected to comprehensive explicit server-side validation. Dedicated helper functions (validate_username, validate_email, validate_phone_number, validate_password) ensure:
Required Fields: Inputs must not be empty.
Length Constraints: Fields adhere to specified minimum and maximum lengths (e.g., username 3-20 chars, password min 8 chars, email max 255 chars).
Character Set/Format: Regular expressions (re.match, re.search) enforce valid character sets (e.g., alphanumeric for username, email format, phone number format, password complexity rules for uppercase, lowercase, numbers, and special characters).
Whitespace Stripping: Inputs are stripped of leading/trailing whitespace (.strip()).
Password Confirmation: The confirmPassword field is explicitly checked to match the password field. This approach ensures data integrity, guards against injection attacks (e.g., SQL Injection, XSS), and prevents malformed data from affecting application logic.
Secrets Management: (Placeholder - In a production Flask application, sensitive information like API keys or database credentials would be loaded from environment variables (os.environ), a .env file (using python-dotenv), or a dedicated secrets management service, rather than being hardcoded in server.py.)
Error Handling: (Placeholder - In a production Flask application, generic error handlers (@app.errorhandler) would catch exceptions and return non-descriptive, user-friendly error messages (e.g., "An internal server error occurred"), logging full details only internally for debugging. debug=True in app.run is used only for development and would be disabled in production.)
Setup and Running the Application
Prerequisites
Python 3.x
pip (Python package installer)
Flask and Flask-CORS Python packages.
Steps
Clone the repository:
Bash

git clone <your-repo-url>
cd InputValid-dotnet-secure/python # Assuming your Python project is here
Create and activate a virtual environment (recommended):
    python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. **Install dependencies:**bash
pip install Flask Flask-Cors # Add any other specific packages like python-dotenv if used for secrets
4. **Run the application:**bash
python server.py
```
The application will typically start on http://127.0.0.1:5003.

API Endpoints
POST /signup
Purpose: Handles user registration requests with robust server-side input validation.
Method: POST
Content-Type: application/json
Request Body Example (JSON):
JSON

{
  "username": "MyValidUser",
  "email": "user@example.com",
  "phoneNumber": "123-456-7890",
  "password": "SecureP@ssw0rd!",
  "confirmPassword": "SecureP@ssw0rd!"
}
Expected Behavior:
Valid Inputs: Returns 200 OK with a success message. Check the backend console for --- VALIDATION SUCCESS ---.
Invalid Inputs (e.g., empty fields, too long username, invalid email format, non-matching passwords): Returns 400 Bad Request with a JSON payload detailing the specific validation errors. Check the backend console for --- VALIDATION FAILED --- and specific error messages.
Static Analysis Tooling
This project is designed to be analyzed by Static Analysis Security Testing (SAST) tools such as Semgrep and Python's Bandit to measure their detection capabilities for the implemented security controls and to verify compliance with secure coding standards.

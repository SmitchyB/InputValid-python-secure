# InputValid-python-secure - Python Flask Secure Build (Input Validation)

This repository houses a specific application build that is part of a larger comparative study, "Evaluating the Effectiveness of Secure Coding Practices Across Python, MERN, and .NET 8." The experiment systematically assesses how secure coding techniques mitigate critical web application vulnerabilities—specifically improper input validation, insecure secrets management, and insecure error handling—across these three diverse development stacks. Through the development of paired vulnerable and secure application versions, this study aims to provide empirical evidence on the practical effectiveness of various security controls and the impact of architectural differences on developer effort and overall security posture.

## Purpose
This particular build contains the **Secure Build** of the Python Flask application, specifically designed to demonstrate secure coding practices for **Input Validation**.

## Vulnerability Focus
This application build specifically addresses the mitigation of:
* **Improper Input Validation:** Ensuring all user input is thoroughly checked and sanitized on the server-side to prevent malicious data from entering the system.

## Key Secure Coding Practices Implemented
* **Explicit Server-Side Input Validation:** All user inputs submitted to the `/signup` endpoint are subjected to comprehensive, explicit server-side validation. Dedicated helper functions (`validate_username`, `validate_email`, `validate_phone_number`, `validate_password`) ensure:
    * **Required Fields:** Inputs must not be empty.
    * **Length Constraints:** Fields adhere to specified minimum and maximum lengths (e.g., username 3-20 chars, password min 8 chars, email max 255 chars).
    * **Character Set/Format:** Regular expressions (`re.match`, `re.search`) enforce valid character sets (e.g., alphanumeric for username, email format, phone number format, password complexity rules for uppercase, lowercase, numbers, and special characters).
    * **Whitespace Stripping:** Inputs are stripped of leading/trailing whitespace (`.strip()`).
    * **Password Confirmation:** The `confirmPassword` field is explicitly checked to match the `password` field.
    This robust approach ensures data integrity, guards against common injection attacks (e.g., SQL Injection, XSS), and prevents malformed data from affecting application logic.

## Setup and Running the Application

### Prerequisites
* Python 3.x
* `pip` (Python package installer)
* `Flask` and `Flask-CORS` Python packages.

### Steps
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Navigate to the specific build folder, e.g.:
    cd InputValid-dotnet-secure/python/secure-input-validation
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install Flask Flask-Cors
    ```
4.  **Run the application:**
    ```bash
    python server.py
    ```
    The application will typically start on `http://127.0.0.1:5003`.

## API Endpoints

### `POST /signup`
* **Purpose:** Handles user registration requests with robust server-side input validation.
* **Method:** `POST`
* **Content-Type:** `application/json`
* **Request Body Example (JSON):**
    ```json
    {
      "username": "MyValidUser",
      "email": "user@example.com",
      "phoneNumber": "123-456-7890",
      "password": "SecureP@ssw0rd!",
      "confirmPassword": "SecureP@ssw0rd!"
    }
    ```
* **Expected Behavior:**
    * **Valid Inputs:** Returns `200 OK` with a success message. Check the backend console for `--- VALIDATION SUCCESS ---`.
    * **Invalid Inputs (e.g., empty fields, too long username, invalid email format, non-matching passwords):** Returns `400 Bad Request` with a JSON payload detailing the specific validation errors. Check the backend console for `--- VALIDATION FAILED ---` and specific error messages.

## Static Analysis Tooling
This specific build is designed to be analyzed by Static Analysis Security Testing (SAST) tools such as Semgrep and Python's Bandit to measure their detection capabilities for the implemented **input validation** security controls and to verify compliance with secure coding standards.

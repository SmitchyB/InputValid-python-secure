from flask import Flask, request, jsonify
from flask_cors import CORS
import re # Import the regular expression module

app = Flask(__name__)
CORS(app) # Enable CORS for all origins

# ===================Change 1============================
# =======================================================
# Helper Functions for Input Validation
# =======================================================

def validate_username(username):
    errors = []
    if not username:
        errors.append("Username is required.")
    else:
        username = username.strip() # Sanitize: Remove leading/trailing whitespace
        if not (3 <= len(username) <= 20):
            errors.append("Username must be between 3 and 20 characters.")
        # Only alphanumeric, underscores, and hyphens allowed
        if not re.match(r"^[a-zA-Z0-9_-]+$", username):
            errors.append("Username contains invalid characters (only alphanumeric, _, - allowed).")
    return errors

def validate_email(email):
    errors = []
    if not email:
        errors.append("Email is required.")
    else:
        email = email.strip()
        # A comprehensive regex for email validation (can be more complex for strictness)
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            errors.append("Please enter a valid email address.")
        if len(email) > 255: # Max length for practical reasons
            errors.append("Email address is too long.")
    return errors

def validate_phone_number(phone_number):
    errors = []
    if not phone_number:
        errors.append("Phone number is required.")
    else:
        phone_number = phone_number.strip()
        # Basic US phone number format: allows digits, optional +, -, (, ), spaces
        if not re.match(r"^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$", phone_number):
            errors.append("Please enter a valid phone number format (e.g., 123-456-7890).")
        # Stripping non-digits to check effective length
        digits_only = re.sub(r'\D', '', phone_number)
        if not (10 <= len(digits_only) <= 15): # Assuming 10-digit US number + optional country code
            errors.append("Phone number length is invalid.")
    return errors

def validate_password(password):
    errors = []
    if not password:
        errors.append("Password is required.")
    else:
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            errors.append("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            errors.append("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            errors.append("Password must contain at least one number.")
        if not re.search(r"[^A-Za-z0-9]", password): # Any character that is not alphanumeric
            errors.append("Password must contain at least one special character.")
        if len(password) > 128: # Practical max length to prevent DOS
            errors.append("Password is too long.")
    return errors

# =======================================================
# SECURE Sign-Up Endpoint with Input Validation
# =======================================================
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    all_errors = {}

    if not data:
        return jsonify({"message": "No data provided"}), 400

    username = data.get('username', '') # Use .get with default empty string
    email = data.get('email', '')
    phoneNumber = data.get('phoneNumber', '')
    password = data.get('password', '')
    confirmPassword = data.get('confirmPassword', '')

    # Log the RAW, UNVALIDATED data received (for demonstration purposes)
    print('--- RECEIVED UNVALIDATED SIGN-UP DATA ---')
    print(f'Username: "{username}"')
    print(f'Email: "{email}"')
    print(f'Phone Number: "{phoneNumber}"')
    print(f'Password: "{password}"') # Still logging raw here for demo, but never do this in production
    print(f'Confirm Password: "{confirmPassword}"')
    print('-----------------------------------------')

    #======================Change 2===========================
    # Perform validation for each field
    username_errors = validate_username(username)
    if username_errors:
        all_errors['username'] = username_errors

    email_errors = validate_email(email)
    if email_errors:
        all_errors['email'] = email_errors

    phone_errors = validate_phone_number(phoneNumber)
    if phone_errors:
        all_errors['phoneNumber'] = phone_errors

    password_errors = validate_password(password)
    if password_errors:
        all_errors['password'] = password_errors
    
    # Confirm password check (only if initial password validation passed and both exist)
    if not password_errors and password and confirmPassword and password != confirmPassword:
        if 'confirmPassword' not in all_errors:
            all_errors['confirmPassword'] = []
        all_errors['confirmPassword'].append("Passwords do not match.")
    elif not confirmPassword: # Check if confirm password is just empty
        if 'confirmPassword' not in all_errors:
            all_errors['confirmPassword'] = []
        all_errors['confirmPassword'].append("Confirm Password is required.")


    # If any errors were found, send them back to the client
    if all_errors:
        print('--- VALIDATION FAILED ---')
        # Print each error for server-side log clarity
        for field, errors in all_errors.items():
            print(f'{field}: {errors}')
        print('-------------------------')
        return jsonify({"errors": all_errors}), 400

    # If validation passes
    print('--- VALIDATION SUCCESS ---')
    print('Received data is VALID.')
    print('--------------------------')

    # In a real application, you would now hash the password and save to a database.
    return jsonify({"message": "Sign-up data successfully validated and received!"}), 200

# Run the Flask app
# Use a different port (e.g., 5003) to distinguish from other backends
if __name__ == '__main__':
    print("Python Flask SECURE Backend listening at http://127.0.0.1:5003")
    print("Ready to receive sign-up data with input validation.")
    app.run(debug=True, port=5003) # debug=True for development, turn off in production!
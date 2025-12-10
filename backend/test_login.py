import urllib.request
import urllib.error
import json
import time

BASE_URL_SIGNUP = "http://127.0.0.1:8000/api/v1/auth/signup"
BASE_URL_LOGIN = "http://127.0.0.1:8000/api/v1/auth/login"

def test_login():
    timestamp = int(time.time())
    email = f"testuser_{timestamp}@example.com"
    password = "securepassword123"

    # 1. Signup first to ensure user exists
    print(f"Creating user {email}...")
    signup_payload = {
        "email": email,
        "password": password
    }
    
    data = json.dumps(signup_payload).encode('utf-8')
    req = urllib.request.Request(
        BASE_URL_SIGNUP, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() != 201:
                print("Failed to create user for login test.")
                return
            print("User created successfully.")
    except urllib.error.HTTPError as e:
        print(f"Failed to create user. Status: {e.code}")
        print(e.read().decode())
        return
    except urllib.error.URLError as e:
        print(f"Connection failed: {e.reason}")
        print("Make sure the server is running.")
        return

    # 2. Successful Login
    print("\nAttempting successful login...")
    login_payload = {
        "email": email,
        "password": password
    }
    
    data = json.dumps(login_payload).encode('utf-8')
    req = urllib.request.Request(
        BASE_URL_LOGIN, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Success! Status: {status}")
            print(f"Response: {body}")
            response_json = json.loads(body)
            assert "access_token" in response_json
            assert response_json["token_type"] == "bearer"
            print("Token verification successful.")
    except urllib.error.HTTPError as e:
        print(f"Failed to login. Status: {e.code}")
        print(e.read().decode())
        return

    # 3. Invalid Password
    print("\nAttempting login with invalid password...")
    invalid_payload = {
        "email": email,
        "password": "wrongpassword"
    }
    
    data = json.dumps(invalid_payload).encode('utf-8')
    req = urllib.request.Request(
        BASE_URL_LOGIN, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            print("Unexpected success on invalid password!")
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(f"Caught expected error: {e.code} - {e.reason}")
            # print(e.read().decode())
        else:
            print(f"Unexpected error: {e.code}")
            print(e.read().decode())

    # 4. Non-existent User
    print("\nAttempting login with non-existent user...")
    non_existent_payload = {
        "email": f"fake_{timestamp}@example.com",
        "password": "somepassword"
    }
    
    data = json.dumps(non_existent_payload).encode('utf-8')
    req = urllib.request.Request(
        BASE_URL_LOGIN, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
             print("Unexpected success on non-existent user!")
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(f"Caught expected error: {e.code} - {e.reason}")
        else:
            print(f"Unexpected error: {e.code}")
            print(e.read().decode())

if __name__ == "__main__":
    test_login()
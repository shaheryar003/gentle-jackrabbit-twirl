import urllib.request
import urllib.error
import json
import time
import sys

def test_auth_flow(port=8000):
    BASE_URL_SIGNUP = f"http://127.0.0.1:{port}/api/v1/auth/signup"
    BASE_URL_LOGIN = f"http://127.0.0.1:{port}/api/v1/auth/login"
    BASE_URL_ME = f"http://127.0.0.1:{port}/api/v1/users/me"

    timestamp = int(time.time())
    email = f"testuser_{timestamp}@example.com"
    password = "securepassword123"

    # 1. Signup first to ensure user exists
    print(f"Creating user {email} on port {port}...")
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
                print("Failed to create user for auth test.")
                return False
            print("User created successfully.")
    except urllib.error.HTTPError as e:
        print(f"Failed to create user. Status: {e.code}")
        print(e.read().decode())
        return False
    except urllib.error.URLError as e:
        print(f"Connection failed: {e.reason}")
        print("Make sure the server is running.")
        return False

    # 2. Login to get token
    print("\nLogging in to get token...")
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
    
    access_token = None
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode()
            response_json = json.loads(body)
            access_token = response_json["access_token"]
            print("Token retrieved successfully.")
    except Exception as e:
        print(f"Login failed: {e}")
        return False

    # 3. Access Protected Route with Token
    print("\nAccessing protected route WITH token...")
    req = urllib.request.Request(
        BASE_URL_ME,
        headers={'Authorization': f'Bearer {access_token}'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Success! Status: {status}")
            print(f"Response: {body}")
            user_data = json.loads(body)
            if user_data["email"] != email:
                print(f"Error: Email mismatch. Expected {email}, got {user_data['email']}")
                return False
            print("Protected data verified.")
    except urllib.error.HTTPError as e:
        print(f"Failed to access protected route. Status: {e.code}")
        print(e.read().decode())
        return False

    # 4. Access Protected Route without Token
    print("\nAccessing protected route WITHOUT token...")
    req = urllib.request.Request(
        BASE_URL_ME
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            print("Error: Unexpected success without token!")
            return False
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(f"Caught expected error: {e.code} - {e.reason}")
        else:
            print(f"Unexpected error: {e.code}")
            print(e.read().decode())
            return False

    return True

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    success = test_auth_flow(port)
    if not success:
        sys.exit(1)
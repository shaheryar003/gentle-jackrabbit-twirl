import urllib.request
import urllib.error
import json
import time

BASE_URL = "http://127.0.0.1:8000/api/v1/auth/signup"

def test_signup():
    # 1. Successful Signup
    timestamp = int(time.time())
    email = f"testuser_{timestamp}@example.com"
    password = "securepassword123"
    
    payload = {
        "email": email,
        "password": password
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        BASE_URL, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"Attempting signup with {email}...")
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Success! Status: {status}")
            print(f"Response: {body}")
            response_json = json.loads(body)
            assert response_json["email"] == email
            assert "id" in response_json
    except urllib.error.HTTPError as e:
        print(f"Failed to signup. Status: {e.code}")
        print(e.read().decode())
        return
    except urllib.error.URLError as e:
        print(f"Connection failed: {e.reason}")
        print("Make sure the server is running at", BASE_URL)
        return

    # 2. Duplicate Signup
    print("\nAttempting duplicate signup...")
    try:
        with urllib.request.urlopen(req) as response:
            print("Unexpected success on duplicate signup!")
    except urllib.error.HTTPError as e:
        if e.code == 400:
            print(f"Caught expected error: {e.code} - {e.reason}")
            # print(e.read().decode())
        else:
            print(f"Unexpected error: {e.code}")
            print(e.read().decode())

if __name__ == "__main__":
    test_signup()
import urllib.request
import urllib.error
import json
import time

BASE_URL = "http://127.0.0.1:8000/api/v1/themes"

def test_themes():
    print("Testing Themes API...")

    # 1. Test GET /api/v1/themes
    print("\n1. Fetching all themes...")
    try:
        with urllib.request.urlopen(BASE_URL) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Status: {status}")
            data = json.loads(body)
            print(f"Themes found: {len(data)}")
            
            if len(data) > 0:
                print("First theme sample:")
                print(json.dumps(data[0], indent=2))
                
                # Check for required fields
                theme = data[0]
                assert "id" in theme
                assert "name" in theme
                assert "description" in theme
                assert "image" in theme
                print("Field validation passed.")
            else:
                print("No themes found. Did you run seed.py?")
                return
            
            # Keep an ID for the next test
            test_id = data[0]["id"]

    except urllib.error.HTTPError as e:
        print(f"Failed to fetch themes. Status: {e.code}")
        print(e.read().decode())
        return
    except urllib.error.URLError as e:
        print(f"Connection failed: {e.reason}")
        print("Make sure the server is running.")
        return

    # 2. Test GET /api/v1/themes/{id}
    print(f"\n2. Fetching specific theme ({test_id})...")
    url = f"{BASE_URL}/{test_id}"
    try:
        with urllib.request.urlopen(url) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Status: {status}")
            theme = json.loads(body)
            print(json.dumps(theme, indent=2))
            
            assert theme["id"] == test_id
            print("Theme ID match confirmed.")
            
    except urllib.error.HTTPError as e:
        print(f"Failed to fetch theme. Status: {e.code}")
        print(e.read().decode())
    
    # 3. Test GET /api/v1/themes/{id} Not Found
    print("\n3. Fetching non-existent theme...")
    url = f"{BASE_URL}/non-existent-id-12345"
    try:
        with urllib.request.urlopen(url) as response:
            print("Unexpected success on non-existent theme!")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Caught expected error: {e.code} - {e.reason}")
        else:
            print(f"Unexpected error: {e.code}")
            print(e.read().decode())

if __name__ == "__main__":
    test_themes()
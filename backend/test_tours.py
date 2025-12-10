import urllib.request
import urllib.error
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"

def test_tours_and_objects():
    print("Testing Tours and Objects API...")

    # 1. Test GET /api/v1/objects/{id}
    print("\n1. Fetching specific object (obj-01)...")
    url = f"{BASE_URL}/objects/obj-01"
    try:
        with urllib.request.urlopen(url) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Status: {status}")
            obj = json.loads(body)
            # print(json.dumps(obj, indent=2))
            
            assert obj["id"] == "obj-01"
            assert "title" in obj
            assert "mapPosition" in obj
            print("Object 'obj-01' fetched and validated.")
            
    except urllib.error.HTTPError as e:
        print(f"Failed to fetch object. Status: {e.code}")
        print(e.read().decode())
        return

    # 2. Test GET /api/v1/tours/{theme_id}/{size}
    print("\n2. Fetching tour (roman-empire, Small)...")
    theme_id = "roman-empire"
    size = "Small"
    url = f"{BASE_URL}/tours/{theme_id}/{size}"
    
    try:
        with urllib.request.urlopen(url) as response:
            status = response.getcode()
            body = response.read().decode()
            print(f"Status: {status}")
            objects = json.loads(body)
            print(f"Objects in tour: {len(objects)}")
            # print(json.dumps(objects, indent=2))
            
            # Verify we got the expected objects
            expected_ids = ["obj-01", "obj-02"]
            received_ids = [obj["id"] for obj in objects]
            
            print(f"Expected IDs: {expected_ids}")
            print(f"Received IDs: {received_ids}")
            
            assert received_ids == expected_ids
            print("Tour objects match expected list and order.")

    except urllib.error.HTTPError as e:
        print(f"Failed to fetch tour. Status: {e.code}")
        print(e.read().decode())
        return

    # 3. Test Invalid Object
    print("\n3. Fetching non-existent object...")
    try:
        urllib.request.urlopen(f"{BASE_URL}/objects/non-existent")
        print("Error: Should have failed")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Caught expected 404 for object.")
        else:
            print(f"Unexpected error: {e.code}")

    # 4. Test Invalid Tour
    print("\n4. Fetching non-existent tour configuration...")
    try:
        urllib.request.urlopen(f"{BASE_URL}/tours/roman-empire/ExtraLarge")
        print("Error: Should have failed")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Caught expected 404 for tour.")
        else:
            print(f"Unexpected error: {e.code}")

if __name__ == "__main__":
    test_tours_and_objects()
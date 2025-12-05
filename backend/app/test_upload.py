import requests

def test_upload():
    base_url = "http://localhost:5000/api/v1"
    
    # 1. Login
    print("Logging in...")
    login_resp = requests.post(f"{base_url}/auth/login", data={
        "username": "admin@example.com",
        "password": "admin123"
    })
    
    if login_resp.status_code != 200:
        print(f"Login failed: {login_resp.text}")
        return
        
    token = login_resp.json()["access_token"]
    print("Login successful.")
    
    # 2. Upload
    print("Uploading file...")
    import time
    unique_content = f"This is a unique document content generated at {time.time()}. The AI should summarize this specific timestamp."
    files = {'file': ('test_dynamic.txt', unique_content)}
    headers = {'Authorization': f'Bearer {token}'}
    
    upload_resp = requests.post(f"{base_url}/documents/upload", files=files, headers=headers)
    
    if upload_resp.status_code == 200:
        print(f"Upload successful: {upload_resp.json()}")
        
        # 3. Search
        print("Testing Search...")
        time.sleep(1) # Wait for DB commit just in case
        search_resp = requests.get(f"{base_url}/documents/search?q=unique", headers=headers)
        if search_resp.status_code == 200:
            results = search_resp.json()
            print(f"Search Results: {len(results)} found.")
            print(results)
        else:
            print(f"Search failed: {search_resp.text}")
            
    else:
        print(f"Upload failed: {upload_resp.text}")

if __name__ == "__main__":
    test_upload()

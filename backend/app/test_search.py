import requests

def test_search():
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
    
    # 2. Search
    print("Testing search...")
    headers = {'Authorization': f'Bearer {token}'}
    search_resp = requests.get(f"{base_url}/documents/search?q=unique", headers=headers)
    
    if search_resp.status_code == 200:
        results = search_resp.json()
        print(f"Search successful: Found {len(results)} documents")
        for doc in results:
            print(f"  - {doc['label']}: {doc['summary'][:50]}...")
    else:
        print(f"Search failed: {search_resp.status_code} - {search_resp.text}")

if __name__ == "__main__":
    test_search()

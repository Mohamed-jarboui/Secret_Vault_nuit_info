import httpx
import asyncio

async def test_ai():
    url = "http://ollama:11434/api/generate"
    print(f"Testing connection to {url}...")
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(url, json={
                "model": "llama3",
                "prompt": "Hello",
                "stream": False
            })
            print(f"Status: {resp.status_code}")
            print(f"Response: {resp.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_ai())

import requests

BASE = "http://localhost:5000"

print(requests.get(f"{BASE}/ping").json())
print(requests.get(f"{BASE}/hello/Sunlyn").json())
print(requests.post(f"{BASE}/echo", json={"note": "learn by doing"}).json())

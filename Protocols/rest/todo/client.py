import requests

BASE = "http://localhost:5001"

print('Create:', requests.post(f"{BASE}/todos", json={"title": "Read docs", "done": False}).json())
print('List:', requests.get(f"{BASE}/todos").json())
print('Update:', requests.put(f"{BASE}/todos/1", json={"done": True}).json())
print('Get:', requests.get(f"{BASE}/todos/1").json())
print('Delete:', requests.delete(f"{BASE}/todos/1").json())

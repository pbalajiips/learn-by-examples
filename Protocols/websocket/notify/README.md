# WebSocket Notify Example

This example opens a WebSocket server and pushes a notification event every 3 seconds to all connected clients.

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Connect from browser or WebSocket client:
```js
const ws = new WebSocket('ws://localhost:5005');
ws.onmessage = e => console.log('Notification', JSON.parse(e.data));
```

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-websocket-notify:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-websocket-notify:local`
   - or `minikube image load protocols-websocket-notify:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/websocket-notify 8085:80`
5. Connect to `ws://localhost:8085`

# WebSocket Chat Example

This example runs a simple WebSocket server that broadcasts every received message to all connected clients.

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Use a WebSocket client to connect:
   - `ws://localhost:5004`

Example JavaScript browser console:
```js
const ws = new WebSocket('ws://localhost:5004');
ws.onmessage = e => console.log(e.data);
ws.onopen = () => ws.send('Hi from browser');
```

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-websocket-chat:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-websocket-chat:local`
   - or `minikube image load protocols-websocket-chat:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/websocket-chat 8084:80`
5. Connect to `ws://localhost:8084`

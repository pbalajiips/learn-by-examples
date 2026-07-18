# REST Simple Example

This example demonstrates a small REST API using Flask.

Endpoints:
- `GET /ping` returns `{ "status": "pong" }`
- `GET /hello/<name>` returns a greeting
- `POST /echo` returns back the JSON payload

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Call endpoints directly or run `python client.py`

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-rest-simple:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-rest-simple:local`
   - or `minikube image load protocols-rest-simple:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/rest-simple 8080:80`
5. Call the service at `http://localhost:8080`

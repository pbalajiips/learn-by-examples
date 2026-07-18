# gRPC Streaming Example

This example shows a server-side streaming gRPC service:
- `StreamHello` returns 5 streamed messages for one request

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python server.py`
3. Run client:
   - `python client.py`

## Deploy to Kubernetes

1. Build the image:
   - `docker build -t protocols-grpc-stream:local .`
2. Load image into local cluster:
   - `kind load docker-image protocols-grpc-stream:local`
   - or `minikube image load protocols-grpc-stream:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/grpc-stream 50052:50052`
5. Run client locally against `localhost:50052`

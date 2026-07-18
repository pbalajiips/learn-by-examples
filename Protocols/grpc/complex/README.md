# gRPC Complex Example

This example demonstrates a more complete gRPC service with:
- unary RPC: `CreateOrder` and `GetOrder`
- server streaming RPC: `TrackOrder`
- client streaming RPC: `SubmitRatings`
- bidirectional streaming RPC: `OrderChat`

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Generate Python code from proto:
   - `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. order.proto`
3. Start server:
   - `python server.py`
4. Run client:
   - `python client.py`

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-grpc-complex:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-grpc-complex:local`
   - or `minikube image load protocols-grpc-complex:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/grpc-complex 50053:50053`
5. Run client locally against `localhost:50053`

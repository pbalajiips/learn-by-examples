# gRPC Hello Example

This example shows a simple unary gRPC service:
- `SayHello` takes a name and returns a greeting

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python server.py`
3. Run client:
   - `python client.py`

## Deploy to Kubernetes

1. Build the Docker image:
   - `docker build -t protocols-grpc-hello:local .`
2. Load into local cluster:
   - `kind load docker-image protocols-grpc-hello:local`
   - or `minikube image load protocols-grpc-hello:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/grpc-hello 50051:50051`
5. Run client locally against `localhost:50051`

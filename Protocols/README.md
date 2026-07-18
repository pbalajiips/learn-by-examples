# Protocol Examples for Local Kubernetes

This workspace contains hands-on example apps for different API styles and protocols.
Each protocol folder has two example projects and Kubernetes manifests for local deployment.

## Protocol folders

- `grpc/hello` – simple unary gRPC example
- `grpc/stream` – gRPC server-side streaming example
- `rest/simple` – basic REST CRUD example
- `rest/todo` – REST API with create/read/update/delete operations
- `graphql/basic` – GraphQL query and mutation example
- `graphql/books` – GraphQL schema for books with nested types
- `websocket/chat` – WebSocket chat-style updates
- `websocket/notify` – WebSocket push notifications example
- `soap/simple` – SOAP service with a hello operation
- `soap/calc` – SOAP calculator service

## Run locally with Kubernetes

Use a local cluster like `minikube`, `kind`, or Docker Desktop Kubernetes.

Typical flow:

1. Build the image locally:
   - `docker build -t protocols-grpc-hello ./grpc/hello`
2. Load the image into the cluster:
   - `kind load docker-image protocols-grpc-hello`
   - or `minikube image load protocols-grpc-hello`
3. Deploy with kubectl:
   - `kubectl apply -f grpc/hello/k8s.yaml`
4. Check services:
   - `kubectl get pods,svc`
5. Port-forward when needed:
   - `kubectl port-forward svc/grpc-hello 50051:50051`

Each example contains a `README.md` describing how to start the server, test it, and deploy it to Kubernetes.

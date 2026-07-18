# GraphQL Basic Example

This example uses a minimal GraphQL schema with a query and mutation.

GraphQL endpoint:
- `POST /graphql`
- `GET /graphql` opens GraphiQL UI

Example query:
```
query {
  hello(name: "Sunlyn")
}
```

Example mutation:
```
mutation {
  addNumbers(a: 4, b: 5) {
    result
  }
}
```

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Open `http://localhost:5002/graphql` in a browser

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-graphql-basic:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-graphql-basic:local`
   - or `minikube image load protocols-graphql-basic:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/graphql-basic 8082:80`
5. Open `http://localhost:8082/graphql`

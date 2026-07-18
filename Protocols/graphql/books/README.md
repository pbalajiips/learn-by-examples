# GraphQL Books Example

This GraphQL example exposes a `Book` type with query and mutation.

Example query:
```
query {
  books {
    id
    title
    author
    year
  }
}
```

Example query by ID:
```
query {
  book(id: "1") {
    title
    author
  }
}
```

Example mutation:
```
mutation {
  addBook(title: "New Book", author: "Author", year: 2026) {
    book {
      id
      title
    }
  }
}
```

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Open `http://localhost:5003/graphql`

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-graphql-books:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-graphql-books:local`
   - or `minikube image load protocols-graphql-books:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/graphql-books 8083:80`
5. Open `http://localhost:8083/graphql`

# REST Todo Example

This REST example demonstrates a small CRUD service using Flask.

Endpoints:
- `GET /todos` list all todos
- `GET /todos/<id>` get one todo
- `POST /todos` create a todo
- `PUT /todos/<id>` update a todo
- `DELETE /todos/<id>` remove a todo

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Run sample client:
   - `python client.py`

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-rest-todo:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-rest-todo:local`
   - or `minikube image load protocols-rest-todo:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/rest-todo 8081:80`
5. Call the service at `http://localhost:8081`

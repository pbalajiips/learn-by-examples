# SOAP Calculator Example

This SOAP example exposes four operations:
- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`

Example request XML:
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.example.soap.calc">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:add>
         <a>5</a>
         <b>3</b>
      </spy:add>
   </soapenv:Body>
</soapenv:Envelope>
```

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-soap-calc:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-soap-calc:local`
   - or `minikube image load protocols-soap-calc:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/soap-calc 8087:80`
5. Call `http://localhost:8087`

# SOAP Simple Example

This example exposes a SOAP endpoint with one operation:
- `sayHello(name)` returns a greeting.

## Run locally

1. Install dependencies:
   - `python -m pip install -r requirements.txt`
2. Start server:
   - `python app.py`
3. Call the SOAP endpoint with a SOAP client or raw XML.

Example request XML:
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.example.soap">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:sayHello>
         <name>Sunlyn</name>
      </spy:sayHello>
   </soapenv:Body>
</soapenv:Envelope>
```

## Deploy to Kubernetes

1. Build image:
   - `docker build -t protocols-soap-simple:local .`
2. Load image into cluster:
   - `kind load docker-image protocols-soap-simple:local`
   - or `minikube image load protocols-soap-simple:local`
3. Apply manifest:
   - `kubectl apply -f k8s.yaml`
4. Port-forward:
   - `kubectl port-forward svc/soap-simple 8086:80`
5. Call `http://localhost:8086`

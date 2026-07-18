from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class HelloService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name} from SOAP!"

application = Application(
    [HelloService],
    tns='spyne.example.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 5006, wsgi_app)
    print('SOAP simple server running on http://0.0.0.0:5006')
    server.serve_forever()

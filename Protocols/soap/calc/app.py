from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class CalcService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, a, b):
        return a * b

    @rpc(Integer, Integer, _returns=Integer)
    def divide(ctx, a, b):
        return int(a / b)

application = Application(
    [CalcService],
    tns='spyne.example.soap.calc',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 5007, wsgi_app)
    print('SOAP calculator server running on http://0.0.0.0:5007')
    server.serve_forever()

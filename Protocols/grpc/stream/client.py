import grpc
import greet_pb2
import greet_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = greet_pb2_grpc.StreamServiceStub(channel)
        responses = stub.StreamHello(greet_pb2.HelloRequest(name="Sunlyn"))
        for reply in responses:
            print(reply.message)

if __name__ == "__main__":
    run()

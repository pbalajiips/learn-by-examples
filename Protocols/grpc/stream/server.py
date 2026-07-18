import time
from concurrent import futures
import grpc
import greet_pb2
import greet_pb2_grpc

class StreamServiceServicer(greet_pb2_grpc.StreamServiceServicer):
    def StreamHello(self, request, context):
        for i in range(1, 6):
            yield greet_pb2.HelloReply(message=f"{i}: Hello, {request.name} (streamed)")
            time.sleep(0.5)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    greet_pb2_grpc.add_StreamServiceServicer_to_server(StreamServiceServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("gRPC stream server started on :50052")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

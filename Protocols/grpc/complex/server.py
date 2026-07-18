from concurrent import futures
import time
import grpc
import order_pb2
import order_pb2_grpc

ORDERS = {}
NEXT_ID = 1

class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        global NEXT_ID
        order_id = NEXT_ID
        NEXT_ID += 1
        ORDERS[order_id] = {
            "order_id": order_id,
            "customer": request.customer,
            "items": list(request.items),
            "status": "RECEIVED",
        }
        return order_pb2.OrderResponse(
            order_id=order_id,
            customer=request.customer,
            items=request.items,
            status="RECEIVED",
        )

    def GetOrder(self, request, context):
        order = ORDERS.get(request.order_id)
        if order is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")
        return order_pb2.OrderResponse(
            order_id=order["order_id"],
            customer=order["customer"],
            items=order["items"],
            status=order["status"],
        )

    def TrackOrder(self, request, context):
        if request.order_id not in ORDERS:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")

        statuses = ["RECEIVED", "PACKED", "SHIPPED", "OUT_FOR_DELIVERY", "DELIVERED"]
        for status in statuses:
            time.sleep(0.5)
            yield order_pb2.OrderStatus(order_id=request.order_id, status=status)

    def SubmitRatings(self, request_iterator, context):
        count = 0
        total = 0
        for rating in request_iterator:
            total += rating.stars
            count += 1
        average = float(total) / count if count else 0.0
        return order_pb2.RatingSummary(count=count, average=average)

    def OrderChat(self, request_iterator, context):
        for msg in request_iterator:
            response = order_pb2.ChatMessage(
                user="server",
                message=f"Hello {msg.user}, I received: {msg.message}",
            )
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("gRPC complex server started on :50053")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

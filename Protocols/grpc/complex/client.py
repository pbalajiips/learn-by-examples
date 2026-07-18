import grpc
import order_pb2
import order_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50053") as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)

        print("--- CreateOrder ---")
        create_resp = stub.CreateOrder(
            order_pb2.OrderRequest(customer="Sunlyn", items=["item-1", "item-2"])
        )
        print(create_resp)

        print("--- GetOrder ---")
        get_resp = stub.GetOrder(order_pb2.GetOrderRequest(order_id=create_resp.order_id))
        print(get_resp)

        print("--- TrackOrder ---")
        for status in stub.TrackOrder(order_pb2.TrackRequest(order_id=create_resp.order_id)):
            print(status)

        print("--- SubmitRatings ---")
        def rating_stream():
            for stars, comment in [(5, "Great"), (4, "Nice"), (3, "Okay")]:
                yield order_pb2.Rating(stars=stars, comment=comment)
        rating_summary = stub.SubmitRatings(rating_stream())
        print(rating_summary)

        print("--- OrderChat ---")
        def chat_messages():
            for text in ["Hello server", "How is my order?", "Thanks"]:
                yield order_pb2.ChatMessage(user="client", message=text)
        for response in stub.OrderChat(chat_messages()):
            print(response)


if __name__ == "__main__":
    run()

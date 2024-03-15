import grpc
import example_pb2
import example_pb2_grpc

def run_client():
    # channel_creds = grpc.alts_channel_credentials()
    # with grpc.secure_channel("127.0.0.1:8000",channel_creds) as channel:
    with grpc.insecure_channel("127.0.0.1:8000") as channel:
        stub = example_pb2_grpc.ExampleServiceStub(channel)
        response = stub.SendMessage(example_pb2.Request(message="Hello gRPC!",num=2))
        print(f"Response from server: {response.reply}")
        print(f"answer from server: {response.re_num} ")

if __name__ == "__main__":
    run_client()


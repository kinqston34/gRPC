import grpc
from concurrent import futures
import example_pb2
import example_pb2_grpc

class ExampleServicer(example_pb2_grpc.ExampleServiceServicer):
    def SendMessage(self, request, context):
        ans = request.num + 5 
        return example_pb2.Response(reply=f"Received: {request.message}，我是server!",re_num=ans)
    
def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServicer(),server) 
    # server_creds = grpc.alts_server_credentials()
    # server.add_secure_port("127.0.0.1:8000",server_creds)
    server.add_insecure_port("127.0.0.1:8000")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    run_server()

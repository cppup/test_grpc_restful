import grpc

import sys
sys.path.insert(0, '.')
sys.path.insert(0, './proto/gen/python')

from proto.gen.python.your.service.v1 import your_service_pb2
from proto.gen.python.your.service.v1 import your_service_pb2_grpc

def run():
    port = 9090
    channel = grpc.insecure_channel('localhost:{}'.format(port))
    stub = your_service_pb2_grpc.YourServiceStub(channel)
    response = stub.Echo(your_service_pb2.StringMessage(value="world"))
    print("GreeterService client received: " + response.value)

if __name__ == '__main__':
    run()

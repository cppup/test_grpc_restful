from concurrent import futures
import time

import grpc

import sys
sys.path.insert(0, '.')
sys.path.insert(0, './proto/gen/python')

from proto.gen.python.your.service.v1 import your_service_pb2
from proto.gen.python.your.service.v1 import your_service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyServer(your_service_pb2_grpc.YourServiceServicer):
    def Echo(self, request, context):
        print("Receive request, request.value: {0}".format(request.value))
        return your_service_pb2.StringMessage(
            value='Hello, {0}'.format(request.value))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    your_service_pb2_grpc.add_YourServiceServicer_to_server(MyServer(), server)
    port = 9090
    server.add_insecure_port('[::]:{}'.format(port))
    print("GreeterServicer start at port {}...".format(port))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

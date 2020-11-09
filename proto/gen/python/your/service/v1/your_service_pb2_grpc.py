# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from your.service.v1 import your_service_pb2 as your_dot_service_dot_v1_dot_your__service__pb2


class YourServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Echo = channel.unary_unary(
                '/your.service.v1.YourService/Echo',
                request_serializer=your_dot_service_dot_v1_dot_your__service__pb2.StringMessage.SerializeToString,
                response_deserializer=your_dot_service_dot_v1_dot_your__service__pb2.StringMessage.FromString,
                )


class YourServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Echo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YourServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=your_dot_service_dot_v1_dot_your__service__pb2.StringMessage.FromString,
                    response_serializer=your_dot_service_dot_v1_dot_your__service__pb2.StringMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'your.service.v1.YourService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YourService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/your.service.v1.YourService/Echo',
            your_dot_service_dot_v1_dot_your__service__pb2.StringMessage.SerializeToString,
            your_dot_service_dot_v1_dot_your__service__pb2.StringMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
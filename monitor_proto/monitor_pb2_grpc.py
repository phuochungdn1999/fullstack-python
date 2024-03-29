# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from monitor_proto import monitor_pb2 as monitor__proto_dot_monitor__pb2


class MonitorControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/monitor.MonitorController/List',
                request_serializer=monitor__proto_dot_monitor__pb2.MonitorListRequest.SerializeToString,
                response_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                )
        self.Create = channel.unary_unary(
                '/monitor.MonitorController/Create',
                request_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
                response_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/monitor.MonitorController/Retrieve',
                request_serializer=monitor__proto_dot_monitor__pb2.MonitorRetrieveRequest.SerializeToString,
                response_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                )
        self.Update = channel.unary_unary(
                '/monitor.MonitorController/Update',
                request_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
                response_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/monitor.MonitorController/Destroy',
                request_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class MonitorControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=monitor__proto_dot_monitor__pb2.MonitorListRequest.FromString,
                    response_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                    response_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=monitor__proto_dot_monitor__pb2.MonitorRetrieveRequest.FromString,
                    response_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                    response_serializer=monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=monitor__proto_dot_monitor__pb2.Monitor.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'monitor.MonitorController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MonitorController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/monitor.MonitorController/List',
            monitor__proto_dot_monitor__pb2.MonitorListRequest.SerializeToString,
            monitor__proto_dot_monitor__pb2.Monitor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/monitor.MonitorController/Create',
            monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            monitor__proto_dot_monitor__pb2.Monitor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/monitor.MonitorController/Retrieve',
            monitor__proto_dot_monitor__pb2.MonitorRetrieveRequest.SerializeToString,
            monitor__proto_dot_monitor__pb2.Monitor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/monitor.MonitorController/Update',
            monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            monitor__proto_dot_monitor__pb2.Monitor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/monitor.MonitorController/Destroy',
            monitor__proto_dot_monitor__pb2.Monitor.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

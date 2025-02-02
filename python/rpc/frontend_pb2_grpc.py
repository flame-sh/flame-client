# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import frontend_pb2 as frontend__pb2
import types_pb2 as types__pb2


class FrontendStub(object):
    """
    The frontend service of Flame, which is used to communicate with client sdk,
    e.g. create connection/session/task and so on.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSession = channel.unary_unary(
                '/flame.Frontend/CreateSession',
                request_serializer=frontend__pb2.CreateSessionRequest.SerializeToString,
                response_deserializer=types__pb2.Session.FromString,
                )
        self.DeleteSession = channel.unary_unary(
                '/flame.Frontend/DeleteSession',
                request_serializer=frontend__pb2.DeleteSessionRequest.SerializeToString,
                response_deserializer=types__pb2.Result.FromString,
                )
        self.OpenSession = channel.unary_unary(
                '/flame.Frontend/OpenSession',
                request_serializer=frontend__pb2.OpenSessionRequest.SerializeToString,
                response_deserializer=types__pb2.Result.FromString,
                )
        self.CloseSession = channel.unary_unary(
                '/flame.Frontend/CloseSession',
                request_serializer=frontend__pb2.CloseSessionRequest.SerializeToString,
                response_deserializer=types__pb2.Result.FromString,
                )
        self.GetSession = channel.unary_unary(
                '/flame.Frontend/GetSession',
                request_serializer=frontend__pb2.GetSessionRequest.SerializeToString,
                response_deserializer=types__pb2.Session.FromString,
                )
        self.ListSession = channel.unary_unary(
                '/flame.Frontend/ListSession',
                request_serializer=frontend__pb2.ListSessionRequest.SerializeToString,
                response_deserializer=types__pb2.SessionList.FromString,
                )
        self.CreateTask = channel.unary_unary(
                '/flame.Frontend/CreateTask',
                request_serializer=frontend__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=types__pb2.Task.FromString,
                )
        self.DeleteTask = channel.unary_unary(
                '/flame.Frontend/DeleteTask',
                request_serializer=frontend__pb2.DeleteTaskRequest.SerializeToString,
                response_deserializer=types__pb2.Result.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/flame.Frontend/GetTask',
                request_serializer=frontend__pb2.GetTaskRequest.SerializeToString,
                response_deserializer=types__pb2.Task.FromString,
                )
        self.WatchTask = channel.unary_stream(
                '/flame.Frontend/WatchTask',
                request_serializer=frontend__pb2.WatchTaskRequest.SerializeToString,
                response_deserializer=types__pb2.Task.FromString,
                )


class FrontendServicer(object):
    """
    The frontend service of Flame, which is used to communicate with client sdk,
    e.g. create connection/session/task and so on.
    """

    def CreateSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FrontendServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=frontend__pb2.CreateSessionRequest.FromString,
                    response_serializer=types__pb2.Session.SerializeToString,
            ),
            'DeleteSession': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSession,
                    request_deserializer=frontend__pb2.DeleteSessionRequest.FromString,
                    response_serializer=types__pb2.Result.SerializeToString,
            ),
            'OpenSession': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenSession,
                    request_deserializer=frontend__pb2.OpenSessionRequest.FromString,
                    response_serializer=types__pb2.Result.SerializeToString,
            ),
            'CloseSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseSession,
                    request_deserializer=frontend__pb2.CloseSessionRequest.FromString,
                    response_serializer=types__pb2.Result.SerializeToString,
            ),
            'GetSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSession,
                    request_deserializer=frontend__pb2.GetSessionRequest.FromString,
                    response_serializer=types__pb2.Session.SerializeToString,
            ),
            'ListSession': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSession,
                    request_deserializer=frontend__pb2.ListSessionRequest.FromString,
                    response_serializer=types__pb2.SessionList.SerializeToString,
            ),
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=frontend__pb2.CreateTaskRequest.FromString,
                    response_serializer=types__pb2.Task.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=frontend__pb2.DeleteTaskRequest.FromString,
                    response_serializer=types__pb2.Result.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=frontend__pb2.GetTaskRequest.FromString,
                    response_serializer=types__pb2.Task.SerializeToString,
            ),
            'WatchTask': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchTask,
                    request_deserializer=frontend__pb2.WatchTaskRequest.FromString,
                    response_serializer=types__pb2.Task.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flame.Frontend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Frontend(object):
    """
    The frontend service of Flame, which is used to communicate with client sdk,
    e.g. create connection/session/task and so on.
    """

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/CreateSession',
            frontend__pb2.CreateSessionRequest.SerializeToString,
            types__pb2.Session.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/DeleteSession',
            frontend__pb2.DeleteSessionRequest.SerializeToString,
            types__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/OpenSession',
            frontend__pb2.OpenSessionRequest.SerializeToString,
            types__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/CloseSession',
            frontend__pb2.CloseSessionRequest.SerializeToString,
            types__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/GetSession',
            frontend__pb2.GetSessionRequest.SerializeToString,
            types__pb2.Session.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/ListSession',
            frontend__pb2.ListSessionRequest.SerializeToString,
            types__pb2.SessionList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/CreateTask',
            frontend__pb2.CreateTaskRequest.SerializeToString,
            types__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/DeleteTask',
            frontend__pb2.DeleteTaskRequest.SerializeToString,
            types__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flame.Frontend/GetTask',
            frontend__pb2.GetTaskRequest.SerializeToString,
            types__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/flame.Frontend/WatchTask',
            frontend__pb2.WatchTaskRequest.SerializeToString,
            types__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

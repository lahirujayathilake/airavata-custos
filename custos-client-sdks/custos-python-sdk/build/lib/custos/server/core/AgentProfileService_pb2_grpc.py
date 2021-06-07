#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements. See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership. The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing,
#   software distributed under the License is distributed on an
#   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied. See the License for the
#   specific language governing permissions and limitations
#   under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import custos.server.core.AgentProfileService_pb2 as AgentProfileService__pb2


class AgentProfileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createAgent = channel.unary_unary(
                '/org.apache.custos.agent.profile.service.AgentProfileService/createAgent',
                request_serializer=AgentProfileService__pb2.AgentRequest.SerializeToString,
                response_deserializer=AgentProfileService__pb2.Agent.FromString,
                )
        self.updateAgent = channel.unary_unary(
                '/org.apache.custos.agent.profile.service.AgentProfileService/updateAgent',
                request_serializer=AgentProfileService__pb2.AgentRequest.SerializeToString,
                response_deserializer=AgentProfileService__pb2.Agent.FromString,
                )
        self.deleteAgent = channel.unary_unary(
                '/org.apache.custos.agent.profile.service.AgentProfileService/deleteAgent',
                request_serializer=AgentProfileService__pb2.AgentRequest.SerializeToString,
                response_deserializer=AgentProfileService__pb2.OperationStatus.FromString,
                )
        self.getAgent = channel.unary_unary(
                '/org.apache.custos.agent.profile.service.AgentProfileService/getAgent',
                request_serializer=AgentProfileService__pb2.AgentRequest.SerializeToString,
                response_deserializer=AgentProfileService__pb2.Agent.FromString,
                )


class AgentProfileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.createAgent,
                    request_deserializer=AgentProfileService__pb2.AgentRequest.FromString,
                    response_serializer=AgentProfileService__pb2.Agent.SerializeToString,
            ),
            'updateAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.updateAgent,
                    request_deserializer=AgentProfileService__pb2.AgentRequest.FromString,
                    response_serializer=AgentProfileService__pb2.Agent.SerializeToString,
            ),
            'deleteAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteAgent,
                    request_deserializer=AgentProfileService__pb2.AgentRequest.FromString,
                    response_serializer=AgentProfileService__pb2.OperationStatus.SerializeToString,
            ),
            'getAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.getAgent,
                    request_deserializer=AgentProfileService__pb2.AgentRequest.FromString,
                    response_serializer=AgentProfileService__pb2.Agent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.custos.agent.profile.service.AgentProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgentProfileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.agent.profile.service.AgentProfileService/createAgent',
            AgentProfileService__pb2.AgentRequest.SerializeToString,
            AgentProfileService__pb2.Agent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.agent.profile.service.AgentProfileService/updateAgent',
            AgentProfileService__pb2.AgentRequest.SerializeToString,
            AgentProfileService__pb2.Agent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.agent.profile.service.AgentProfileService/deleteAgent',
            AgentProfileService__pb2.AgentRequest.SerializeToString,
            AgentProfileService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.agent.profile.service.AgentProfileService/getAgent',
            AgentProfileService__pb2.AgentRequest.SerializeToString,
            AgentProfileService__pb2.Agent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
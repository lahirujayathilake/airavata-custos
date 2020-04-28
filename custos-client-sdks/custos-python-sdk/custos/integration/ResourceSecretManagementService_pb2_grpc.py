# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import custos.core.IdentityService_pb2 as IdentityService__pb2
import custos.core.ResourceSecretService_pb2 as ResourceSecretService__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


class ResourceSecretManagementServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getSecret = channel.unary_unary(
        '/org.apache.custos.resource.secret.management.service.ResourceSecretManagementService/getSecret',
        request_serializer=ResourceSecretService__pb2.GetSecretRequest.SerializeToString,
        response_deserializer=ResourceSecretService__pb2.SecretMetadata.FromString,
        )
    self.getJWKS = channel.unary_unary(
        '/org.apache.custos.resource.secret.management.service.ResourceSecretManagementService/getJWKS',
        request_serializer=IdentityService__pb2.GetJWKSRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
        )


class ResourceSecretManagementServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getSecret(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getJWKS(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ResourceSecretManagementServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getSecret': grpc.unary_unary_rpc_method_handler(
          servicer.getSecret,
          request_deserializer=ResourceSecretService__pb2.GetSecretRequest.FromString,
          response_serializer=ResourceSecretService__pb2.SecretMetadata.SerializeToString,
      ),
      'getJWKS': grpc.unary_unary_rpc_method_handler(
          servicer.getJWKS,
          request_deserializer=IdentityService__pb2.GetJWKSRequest.FromString,
          response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.apache.custos.resource.secret.management.service.ResourceSecretManagementService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
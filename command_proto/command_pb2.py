# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_proto/command.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63ommand_proto/command.proto\x12\x07monitor\"\'\n\x0fPredictResponse\x12\x14\n\x0clucky_number\x18\x01 \x01(\x05\"\x1a\n\x0bLogResponse\x12\x0b\n\x03log\x18\x01 \x01(\t\"\x10\n\x0ePredictRequest\"\x18\n\nLogRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\x88\x01\n\x11\x43ommandController\x12>\n\x07Predict\x12\x17.monitor.PredictRequest\x1a\x18.monitor.PredictResponse\"\x00\x12\x33\n\x04Logs\x12\x13.monitor.LogRequest\x1a\x14.monitor.LogResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_proto.command_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREDICTRESPONSE._serialized_start=40
  _PREDICTRESPONSE._serialized_end=79
  _LOGRESPONSE._serialized_start=81
  _LOGRESPONSE._serialized_end=107
  _PREDICTREQUEST._serialized_start=109
  _PREDICTREQUEST._serialized_end=125
  _LOGREQUEST._serialized_start=127
  _LOGREQUEST._serialized_end=151
  _COMMANDCONTROLLER._serialized_start=154
  _COMMANDCONTROLLER._serialized_end=290
# @@protoc_insertion_point(module_scope)
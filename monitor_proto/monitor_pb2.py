# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: monitor_proto/monitor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmonitor_proto/monitor.proto\x12\x07monitor\x1a\x1bgoogle/protobuf/empty.proto\"|\n\x07Monitor\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x17\n\x0f\x63pu_utilization\x18\x04 \x01(\x02\x12\x18\n\x10training_process\x18\x05 \x01(\x02\x12\x11\n\terror_log\x18\x06 \x01(\t\"\x14\n\x12MonitorListRequest\"$\n\x16MonitorRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xa6\x02\n\x11MonitorController\x12\x39\n\x04List\x12\x1b.monitor.MonitorListRequest\x1a\x10.monitor.Monitor\"\x00\x30\x01\x12.\n\x06\x43reate\x12\x10.monitor.Monitor\x1a\x10.monitor.Monitor\"\x00\x12?\n\x08Retrieve\x12\x1f.monitor.MonitorRetrieveRequest\x1a\x10.monitor.Monitor\"\x00\x12.\n\x06Update\x12\x10.monitor.Monitor\x1a\x10.monitor.Monitor\"\x00\x12\x35\n\x07\x44\x65stroy\x12\x10.monitor.Monitor\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'monitor_proto.monitor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MONITOR._serialized_start=69
  _MONITOR._serialized_end=193
  _MONITORLISTREQUEST._serialized_start=195
  _MONITORLISTREQUEST._serialized_end=215
  _MONITORRETRIEVEREQUEST._serialized_start=217
  _MONITORRETRIEVEREQUEST._serialized_end=253
  _MONITORCONTROLLER._serialized_start=256
  _MONITORCONTROLLER._serialized_end=550
# @@protoc_insertion_point(module_scope)

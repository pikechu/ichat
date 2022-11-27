# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc_header.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10rpc_header.proto\x12\x04irpc\"=\n\x05MHead\x12\x11\n\tfrom_addr\x18\x01 \x01(\t\x12\x11\n\tfrom_port\x18\x02 \x01(\x07\x12\x0e\n\x06\x64\x65vice\x18\x03 \x01(\x07*@\n\x06\x44\x65vice\x12\x0e\n\nOS_WINDOWS\x10\x01\x12\x0e\n\nOS_ANDROID\x10\x02\x12\n\n\x06OS_MAC\x10\x03\x12\n\n\x06OS_IOS\x10\x04\x42\x06\x80\x01\x01\x90\x01\x01')

_DEVICE = DESCRIPTOR.enum_types_by_name['Device']
Device = enum_type_wrapper.EnumTypeWrapper(_DEVICE)
OS_WINDOWS = 1
OS_ANDROID = 2
OS_MAC = 3
OS_IOS = 4


_MHEAD = DESCRIPTOR.message_types_by_name['MHead']
MHead = _reflection.GeneratedProtocolMessageType('MHead', (_message.Message,), {
  'DESCRIPTOR' : _MHEAD,
  '__module__' : 'rpc_header_pb2'
  # @@protoc_insertion_point(class_scope:irpc.MHead)
  })
_sym_db.RegisterMessage(MHead)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001\220\001\001'
  _DEVICE._serialized_start=89
  _DEVICE._serialized_end=153
  _MHEAD._serialized_start=26
  _MHEAD._serialized_end=87
# @@protoc_insertion_point(module_scope)

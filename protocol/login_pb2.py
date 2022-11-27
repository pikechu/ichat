# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blogin.proto\x12\x05login\"*\n\x08LoginReq\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"1\n\x08LoginRsp\x12\x12\n\nerror_code\x18\x01 \x01(\x0f\x12\x11\n\terror_msg\x18\x02 \x01(\t\"+\n\tRegistReq\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"2\n\tRegistRsp\x12\x12\n\nerror_code\x18\x01 \x01(\x0f\x12\x11\n\terror_msg\x18\x02 \x01(\tB\x06\x80\x01\x01\x90\x01\x01')



_LOGINREQ = DESCRIPTOR.message_types_by_name['LoginReq']
_LOGINRSP = DESCRIPTOR.message_types_by_name['LoginRsp']
_REGISTREQ = DESCRIPTOR.message_types_by_name['RegistReq']
_REGISTRSP = DESCRIPTOR.message_types_by_name['RegistRsp']
LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQ,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:login.LoginReq)
  })
_sym_db.RegisterMessage(LoginReq)

LoginRsp = _reflection.GeneratedProtocolMessageType('LoginRsp', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRSP,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:login.LoginRsp)
  })
_sym_db.RegisterMessage(LoginRsp)

RegistReq = _reflection.GeneratedProtocolMessageType('RegistReq', (_message.Message,), {
  'DESCRIPTOR' : _REGISTREQ,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:login.RegistReq)
  })
_sym_db.RegisterMessage(RegistReq)

RegistRsp = _reflection.GeneratedProtocolMessageType('RegistRsp', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRSP,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:login.RegistRsp)
  })
_sym_db.RegisterMessage(RegistRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001\220\001\001'
  _LOGINREQ._serialized_start=22
  _LOGINREQ._serialized_end=64
  _LOGINRSP._serialized_start=66
  _LOGINRSP._serialized_end=115
  _REGISTREQ._serialized_start=117
  _REGISTREQ._serialized_end=160
  _REGISTRSP._serialized_start=162
  _REGISTRSP._serialized_end=212
# @@protoc_insertion_point(module_scope)

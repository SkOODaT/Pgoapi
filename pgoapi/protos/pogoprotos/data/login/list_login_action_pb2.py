# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/login/list_login_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.login import login_detail_pb2 as pogoprotos_dot_data_dot_login_dot_login__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/login/list_login_action.proto',
  package='pogoprotos.data.login',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/data/login/list_login_action.proto\x12\x15pogoprotos.data.login\x1a(pogoprotos/data/login/login_detail.proto\"d\n\x17ListLoginActionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x38\n\x0clogin_detail\x18\x02 \x03(\x0b\x32\".pogoprotos.data.login.LoginDetailb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_login_dot_login__detail__pb2.DESCRIPTOR,])




_LISTLOGINACTIONRESPONSE = _descriptor.Descriptor(
  name='ListLoginActionResponse',
  full_name='pogoprotos.data.login.ListLoginActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.data.login.ListLoginActionResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_detail', full_name='pogoprotos.data.login.ListLoginActionResponse.login_detail', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=214,
)

_LISTLOGINACTIONRESPONSE.fields_by_name['login_detail'].message_type = pogoprotos_dot_data_dot_login_dot_login__detail__pb2._LOGINDETAIL
DESCRIPTOR.message_types_by_name['ListLoginActionResponse'] = _LISTLOGINACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListLoginActionResponse = _reflection.GeneratedProtocolMessageType('ListLoginActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTLOGINACTIONRESPONSE,
  __module__ = 'pogoprotos.data.login.list_login_action_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.login.ListLoginActionResponse)
  ))
_sym_db.RegisterMessage(ListLoginActionResponse)


# @@protoc_insertion_point(module_scope)

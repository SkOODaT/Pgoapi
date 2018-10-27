# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/friends/incoming_friend_invite.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/friends/incoming_friend_invite.proto',
  package='pogoprotos.data.friends',
  syntax='proto3',
  serialized_pb=_b('\n4pogoprotos/data/friends/incoming_friend_invite.proto\x12\x17pogoprotos.data.friends\"\xc2\x01\n\x14IncomingFriendInvite\x12\x44\n\x06status\x18\x01 \x01(\x0e\x32\x34.pogoprotos.data.friends.IncomingFriendInvite.Status\x12\x11\n\tplayer_id\x18\x02 \x01(\t\x12\x12\n\ncreated_ms\x18\x03 \x01(\x03\"=\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08\x44\x45\x43LINED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x62\x06proto3')
)



_INCOMINGFRIENDINVITE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.data.friends.IncomingFriendInvite.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLINED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=215,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_INCOMINGFRIENDINVITE_STATUS)


_INCOMINGFRIENDINVITE = _descriptor.Descriptor(
  name='IncomingFriendInvite',
  full_name='pogoprotos.data.friends.IncomingFriendInvite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.data.friends.IncomingFriendInvite.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.data.friends.IncomingFriendInvite.player_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created_ms', full_name='pogoprotos.data.friends.IncomingFriendInvite.created_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INCOMINGFRIENDINVITE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=276,
)

_INCOMINGFRIENDINVITE.fields_by_name['status'].enum_type = _INCOMINGFRIENDINVITE_STATUS
_INCOMINGFRIENDINVITE_STATUS.containing_type = _INCOMINGFRIENDINVITE
DESCRIPTOR.message_types_by_name['IncomingFriendInvite'] = _INCOMINGFRIENDINVITE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncomingFriendInvite = _reflection.GeneratedProtocolMessageType('IncomingFriendInvite', (_message.Message,), dict(
  DESCRIPTOR = _INCOMINGFRIENDINVITE,
  __module__ = 'pogoprotos.data.friends.incoming_friend_invite_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.friends.IncomingFriendInvite)
  ))
_sym_db.RegisterMessage(IncomingFriendInvite)


# @@protoc_insertion_point(module_scope)

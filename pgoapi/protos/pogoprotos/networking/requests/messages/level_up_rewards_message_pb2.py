# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/level_up_rewards_message.proto

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
  name='pogoprotos/networking/requests/messages/level_up_rewards_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/requests/messages/level_up_rewards_message.proto\x12\'pogoprotos.networking.requests.messages\"&\n\x15LevelUpRewardsMessage\x12\r\n\x05level\x18\x01 \x01(\x05\x62\x06proto3')
)




_LEVELUPREWARDSMESSAGE = _descriptor.Descriptor(
  name='LevelUpRewardsMessage',
  full_name='pogoprotos.networking.requests.messages.LevelUpRewardsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.networking.requests.messages.LevelUpRewardsMessage.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=115,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['LevelUpRewardsMessage'] = _LEVELUPREWARDSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LevelUpRewardsMessage = _reflection.GeneratedProtocolMessageType('LevelUpRewardsMessage', (_message.Message,), dict(
  DESCRIPTOR = _LEVELUPREWARDSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.level_up_rewards_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.LevelUpRewardsMessage)
  ))
_sym_db.RegisterMessage(LevelUpRewardsMessage)


# @@protoc_insertion_point(module_scope)

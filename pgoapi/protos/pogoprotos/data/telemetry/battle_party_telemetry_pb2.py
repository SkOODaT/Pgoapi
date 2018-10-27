# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/battle_party_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/battle_party_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n6pogoprotos/data/telemetry/battle_party_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\x99\x01\n\x14\x42\x61ttlePartyTelemetry\x12H\n\x15\x62\x61ttle_party_click_id\x18\x01 \x01(\x0e\x32).pogoprotos.enums.BattlePartyTelemetryIds\x12\x1a\n\x12\x62\x61ttle_party_count\x18\x02 \x01(\x05\x12\x1b\n\x13\x62\x61ttle_party_number\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_BATTLEPARTYTELEMETRY = _descriptor.Descriptor(
  name='BattlePartyTelemetry',
  full_name='pogoprotos.data.telemetry.BattlePartyTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='battle_party_click_id', full_name='pogoprotos.data.telemetry.BattlePartyTelemetry.battle_party_click_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_party_count', full_name='pogoprotos.data.telemetry.BattlePartyTelemetry.battle_party_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_party_number', full_name='pogoprotos.data.telemetry.BattlePartyTelemetry.battle_party_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=124,
  serialized_end=277,
)

_BATTLEPARTYTELEMETRY.fields_by_name['battle_party_click_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._BATTLEPARTYTELEMETRYIDS
DESCRIPTOR.message_types_by_name['BattlePartyTelemetry'] = _BATTLEPARTYTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BattlePartyTelemetry = _reflection.GeneratedProtocolMessageType('BattlePartyTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEPARTYTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.battle_party_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.BattlePartyTelemetry)
  ))
_sym_db.RegisterMessage(BattlePartyTelemetry)


# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/delete_gift_from_inventory_response.proto

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
  name='pogoprotos/networking/responses/social/delete_gift_from_inventory_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_pb=_b('\nPpogoprotos/networking/responses/social/delete_gift_from_inventory_response.proto\x12&pogoprotos.networking.responses.social\"\xd5\x01\n\x1f\x44\x65leteGiftFromInventoryResponse\x12^\n\x06result\x18\x01 \x01(\x0e\x32N.pogoprotos.networking.responses.social.DeleteGiftFromInventoryResponse.Result\"R\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1d\n\x19\x45RROR_GIFT_DOES_NOT_EXIST\x10\x03\x62\x06proto3')
)



_DELETEGIFTFROMINVENTORYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.DeleteGiftFromInventoryResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GIFT_DOES_NOT_EXIST', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=256,
  serialized_end=338,
)
_sym_db.RegisterEnumDescriptor(_DELETEGIFTFROMINVENTORYRESPONSE_RESULT)


_DELETEGIFTFROMINVENTORYRESPONSE = _descriptor.Descriptor(
  name='DeleteGiftFromInventoryResponse',
  full_name='pogoprotos.networking.responses.social.DeleteGiftFromInventoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.DeleteGiftFromInventoryResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DELETEGIFTFROMINVENTORYRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=338,
)

_DELETEGIFTFROMINVENTORYRESPONSE.fields_by_name['result'].enum_type = _DELETEGIFTFROMINVENTORYRESPONSE_RESULT
_DELETEGIFTFROMINVENTORYRESPONSE_RESULT.containing_type = _DELETEGIFTFROMINVENTORYRESPONSE
DESCRIPTOR.message_types_by_name['DeleteGiftFromInventoryResponse'] = _DELETEGIFTFROMINVENTORYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteGiftFromInventoryResponse = _reflection.GeneratedProtocolMessageType('DeleteGiftFromInventoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEGIFTFROMINVENTORYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.delete_gift_from_inventory_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.DeleteGiftFromInventoryResponse)
  ))
_sym_db.RegisterMessage(DeleteGiftFromInventoryResponse)


# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/uncomment_annotation_test.proto

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
  name='pogoprotos/data/uncomment_annotation_test.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n/pogoprotos/data/uncomment_annotation_test.proto\x12\x0fpogoprotos.data\"I\n\x17UncommentAnnotationTest\x12\x17\n\x0fstring_property\x18\x01 \x01(\t\x12\x15\n\rlong_property\x18\x02 \x01(\x03\x62\x06proto3')
)




_UNCOMMENTANNOTATIONTEST = _descriptor.Descriptor(
  name='UncommentAnnotationTest',
  full_name='pogoprotos.data.UncommentAnnotationTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_property', full_name='pogoprotos.data.UncommentAnnotationTest.string_property', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long_property', full_name='pogoprotos.data.UncommentAnnotationTest.long_property', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=68,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['UncommentAnnotationTest'] = _UNCOMMENTANNOTATIONTEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UncommentAnnotationTest = _reflection.GeneratedProtocolMessageType('UncommentAnnotationTest', (_message.Message,), dict(
  DESCRIPTOR = _UNCOMMENTANNOTATIONTEST,
  __module__ = 'pogoprotos.data.uncomment_annotation_test_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.UncommentAnnotationTest)
  ))
_sym_db.RegisterMessage(UncommentAnnotationTest)


# @@protoc_insertion_point(module_scope)
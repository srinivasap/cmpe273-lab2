# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

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
  name='calculator.proto',
  package='calculator',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\x12\ncalculator\"(\n\nAddRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1c\n\nAddReponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32L\n\nCalculator\x12>\n\nAddNumbers\x12\x16.calculator.AddRequest\x1a\x16.calculator.AddReponse\"\x00\x42\x38\n\x1c\x65\x64u.sjsu.cmpe273.fall18.lab2B\x0f\x43\x61lculatorProtoP\x01\xa2\x02\x04\x43\x41LCb\x06proto3')
)




_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='calculator.AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num1', full_name='calculator.AddRequest.num1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num2', full_name='calculator.AddRequest.num2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=72,
)


_ADDREPONSE = _descriptor.Descriptor(
  name='AddReponse',
  full_name='calculator.AddReponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='calculator.AddReponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=74,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddReponse'] = _ADDREPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDREQUEST,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.AddRequest)
  ))
_sym_db.RegisterMessage(AddRequest)

AddReponse = _reflection.GeneratedProtocolMessageType('AddReponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDREPONSE,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.AddReponse)
  ))
_sym_db.RegisterMessage(AddReponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034edu.sjsu.cmpe273.fall18.lab2B\017CalculatorProtoP\001\242\002\004CALC'))

_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='calculator.Calculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=104,
  serialized_end=180,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddNumbers',
    full_name='calculator.Calculator.AddNumbers',
    index=0,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDREPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\tcoherence\",\n\x0c\x43learRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\"`\n\x14\x43ontainsEntryRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\r\n\x05value\x18\x05 \x01(\x0c\"O\n\x12\x43ontainsKeyRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\"S\n\x14\x43ontainsValueRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x0c\".\n\x0e\x44\x65stroyRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\".\n\x0eIsEmptyRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\"+\n\x0bSizeRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\"G\n\nGetRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\"J\n\rGetAllRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x03(\x0c\"c\n\nPutRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\r\n\x05value\x18\x05 \x01(\x0c\x12\x0b\n\x03ttl\x18\x06 \x01(\x03\"^\n\rPutAllRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x1f\n\x05\x65ntry\x18\x04 \x03(\x0b\x32\x10.coherence.Entry\"k\n\x12PutIfAbsentRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\r\n\x05value\x18\x05 \x01(\x0c\x12\x0b\n\x03ttl\x18\x06 \x01(\x03\"J\n\rRemoveRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\"`\n\x14RemoveMappingRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\r\n\x05value\x18\x05 \x01(\x0c\"Z\n\x0eReplaceRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\r\n\x05value\x18\x05 \x01(\x0c\"{\n\x15ReplaceMappingRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\x0c\x12\x15\n\rpreviousValue\x18\x05 \x01(\x0c\x12\x10\n\x08newValue\x18\x06 \x01(\x0c\"K\n\x0bPageRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0e\n\x06\x63ookie\x18\x04 \x01(\x0c\"9\n\x0b\x45ntryResult\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0e\n\x06\x63ookie\x18\x03 \x01(\x0c\"#\n\x05\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"/\n\x0fTruncateRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\"v\n\x0f\x41\x64\x64IndexRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x11\n\textractor\x18\x04 \x01(\x0c\x12\x0e\n\x06sorted\x18\x05 \x01(\x08\x12\x12\n\ncomparator\x18\x06 \x01(\x0c\"U\n\x12RemoveIndexRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x11\n\textractor\x18\x04 \x01(\x0c\"r\n\x10\x41ggregateRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x12\n\naggregator\x18\x04 \x01(\x0c\x12\x0c\n\x04keys\x18\x05 \x03(\x0c\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\x0c\"]\n\rInvokeRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x11\n\tprocessor\x18\x04 \x01(\x0c\x12\x0b\n\x03key\x18\x05 \x01(\x0c\"q\n\x10InvokeAllRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x11\n\tprocessor\x18\x04 \x01(\x0c\x12\x0c\n\x04keys\x18\x05 \x03(\x0c\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\x0c\"c\n\x0f\x45ntrySetRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\x0c\x12\x12\n\ncomparator\x18\x05 \x01(\x0c\"M\n\rKeySetRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\x0c\"a\n\rValuesRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\x0c\x12\x12\n\ncomparator\x18\x05 \x01(\x0c\"/\n\rOptionalValue\x12\x0f\n\x07present\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xa8\x02\n\x12MapListenerRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\r\n\x05\x63\x61\x63he\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x37\n\x04type\x18\x05 \x01(\x0e\x32).coherence.MapListenerRequest.RequestType\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\x0c\x12\x0b\n\x03key\x18\x07 \x01(\x0c\x12\x0c\n\x04lite\x18\x08 \x01(\x08\x12\x11\n\tsubscribe\x18\t \x01(\x08\x12\x0f\n\x07priming\x18\n \x01(\x08\x12\x0f\n\x07trigger\x18\x0b \x01(\x0c\x12\x10\n\x08\x66ilterId\x18\x0c \x01(\x03\",\n\x0bRequestType\x12\x08\n\x04INIT\x10\x00\x12\x07\n\x03KEY\x10\x01\x12\n\n\x06\x46ILTER\x10\x02\"\xfe\x02\n\x13MapListenerResponse\x12>\n\nsubscribed\x18\x01 \x01(\x0b\x32(.coherence.MapListenerSubscribedResponseH\x00\x12\x42\n\x0cunsubscribed\x18\x02 \x01(\x0b\x32*.coherence.MapListenerUnsubscribedResponseH\x00\x12,\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x1b.coherence.MapEventResponseH\x00\x12\x34\n\x05\x65rror\x18\x04 \x01(\x0b\x32#.coherence.MapListenerErrorResponseH\x00\x12\x36\n\tdestroyed\x18\x05 \x01(\x0b\x32!.coherence.CacheDestroyedResponseH\x00\x12\x36\n\ttruncated\x18\x06 \x01(\x0b\x32!.coherence.CacheTruncatedResponseH\x00\x42\x0f\n\rresponse_type\",\n\x1dMapListenerSubscribedResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\".\n\x1fMapListenerUnsubscribedResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\"\'\n\x16\x43\x61\x63heDestroyedResponse\x12\r\n\x05\x63\x61\x63he\x18\x01 \x01(\t\"\'\n\x16\x43\x61\x63heTruncatedResponse\x12\r\n\x05\x63\x61\x63he\x18\x01 \x01(\t\"U\n\x18MapListenerErrorResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12\r\n\x05stack\x18\x04 \x03(\t\"\xa6\x02\n\x10MapEventResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x10\n\x08newValue\x18\x03 \x01(\x0c\x12\x10\n\x08oldValue\x18\x04 \x01(\x0c\x12L\n\x13transformationState\x18\x05 \x01(\x0e\x32/.coherence.MapEventResponse.TransformationState\x12\x11\n\tfilterIds\x18\x06 \x03(\x03\x12\x11\n\tsynthetic\x18\x07 \x01(\x08\x12\x0f\n\x07priming\x18\x08 \x01(\x08\"P\n\x13TransformationState\x12\x15\n\x11NON_TRANSFORMABLE\x10\x00\x12\x11\n\rTRANSFORMABLE\x10\x01\x12\x0f\n\x0bTRANSFORMED\x10\x02\x42\x1d\n\x19\x63om.oracle.coherence.grpcP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.oracle.coherence.grpcP\001'
  _CLEARREQUEST._serialized_start=29
  _CLEARREQUEST._serialized_end=73
  _CONTAINSENTRYREQUEST._serialized_start=75
  _CONTAINSENTRYREQUEST._serialized_end=171
  _CONTAINSKEYREQUEST._serialized_start=173
  _CONTAINSKEYREQUEST._serialized_end=252
  _CONTAINSVALUEREQUEST._serialized_start=254
  _CONTAINSVALUEREQUEST._serialized_end=337
  _DESTROYREQUEST._serialized_start=339
  _DESTROYREQUEST._serialized_end=385
  _ISEMPTYREQUEST._serialized_start=387
  _ISEMPTYREQUEST._serialized_end=433
  _SIZEREQUEST._serialized_start=435
  _SIZEREQUEST._serialized_end=478
  _GETREQUEST._serialized_start=480
  _GETREQUEST._serialized_end=551
  _GETALLREQUEST._serialized_start=553
  _GETALLREQUEST._serialized_end=627
  _PUTREQUEST._serialized_start=629
  _PUTREQUEST._serialized_end=728
  _PUTALLREQUEST._serialized_start=730
  _PUTALLREQUEST._serialized_end=824
  _PUTIFABSENTREQUEST._serialized_start=826
  _PUTIFABSENTREQUEST._serialized_end=933
  _REMOVEREQUEST._serialized_start=935
  _REMOVEREQUEST._serialized_end=1009
  _REMOVEMAPPINGREQUEST._serialized_start=1011
  _REMOVEMAPPINGREQUEST._serialized_end=1107
  _REPLACEREQUEST._serialized_start=1109
  _REPLACEREQUEST._serialized_end=1199
  _REPLACEMAPPINGREQUEST._serialized_start=1201
  _REPLACEMAPPINGREQUEST._serialized_end=1324
  _PAGEREQUEST._serialized_start=1326
  _PAGEREQUEST._serialized_end=1401
  _ENTRYRESULT._serialized_start=1403
  _ENTRYRESULT._serialized_end=1460
  _ENTRY._serialized_start=1462
  _ENTRY._serialized_end=1497
  _TRUNCATEREQUEST._serialized_start=1499
  _TRUNCATEREQUEST._serialized_end=1546
  _ADDINDEXREQUEST._serialized_start=1548
  _ADDINDEXREQUEST._serialized_end=1666
  _REMOVEINDEXREQUEST._serialized_start=1668
  _REMOVEINDEXREQUEST._serialized_end=1753
  _AGGREGATEREQUEST._serialized_start=1755
  _AGGREGATEREQUEST._serialized_end=1869
  _INVOKEREQUEST._serialized_start=1871
  _INVOKEREQUEST._serialized_end=1964
  _INVOKEALLREQUEST._serialized_start=1966
  _INVOKEALLREQUEST._serialized_end=2079
  _ENTRYSETREQUEST._serialized_start=2081
  _ENTRYSETREQUEST._serialized_end=2180
  _KEYSETREQUEST._serialized_start=2182
  _KEYSETREQUEST._serialized_end=2259
  _VALUESREQUEST._serialized_start=2261
  _VALUESREQUEST._serialized_end=2358
  _OPTIONALVALUE._serialized_start=2360
  _OPTIONALVALUE._serialized_end=2407
  _MAPLISTENERREQUEST._serialized_start=2410
  _MAPLISTENERREQUEST._serialized_end=2706
  _MAPLISTENERREQUEST_REQUESTTYPE._serialized_start=2662
  _MAPLISTENERREQUEST_REQUESTTYPE._serialized_end=2706
  _MAPLISTENERRESPONSE._serialized_start=2709
  _MAPLISTENERRESPONSE._serialized_end=3091
  _MAPLISTENERSUBSCRIBEDRESPONSE._serialized_start=3093
  _MAPLISTENERSUBSCRIBEDRESPONSE._serialized_end=3137
  _MAPLISTENERUNSUBSCRIBEDRESPONSE._serialized_start=3139
  _MAPLISTENERUNSUBSCRIBEDRESPONSE._serialized_end=3185
  _CACHEDESTROYEDRESPONSE._serialized_start=3187
  _CACHEDESTROYEDRESPONSE._serialized_end=3226
  _CACHETRUNCATEDRESPONSE._serialized_start=3228
  _CACHETRUNCATEDRESPONSE._serialized_end=3267
  _MAPLISTENERERRORRESPONSE._serialized_start=3269
  _MAPLISTENERERRORRESPONSE._serialized_end=3354
  _MAPEVENTRESPONSE._serialized_start=3357
  _MAPEVENTRESPONSE._serialized_end=3651
  _MAPEVENTRESPONSE_TRANSFORMATIONSTATE._serialized_start=3571
  _MAPEVENTRESPONSE_TRANSFORMATIONSTATE._serialized_end=3651
# @@protoc_insertion_point(module_scope)

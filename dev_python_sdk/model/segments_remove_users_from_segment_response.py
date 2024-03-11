# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from dev_python_sdk import schemas  # noqa: F401


class SegmentsRemoveUsersFromSegmentResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def succeeded() -> typing.Type['SegmentsRemoveUsersFromSegmentResponseSucceeded']:
                return SegmentsRemoveUsersFromSegmentResponseSucceeded
        
            @staticmethod
            def failed() -> typing.Type['SegmentsRemoveUsersFromSegmentResponseFailed']:
                return SegmentsRemoveUsersFromSegmentResponseFailed
            __annotations__ = {
                "succeeded": succeeded,
                "failed": failed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["succeeded"]) -> 'SegmentsRemoveUsersFromSegmentResponseSucceeded': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failed"]) -> 'SegmentsRemoveUsersFromSegmentResponseFailed': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["succeeded", "failed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["succeeded"]) -> typing.Union['SegmentsRemoveUsersFromSegmentResponseSucceeded', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failed"]) -> typing.Union['SegmentsRemoveUsersFromSegmentResponseFailed', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["succeeded", "failed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        succeeded: typing.Union['SegmentsRemoveUsersFromSegmentResponseSucceeded', schemas.Unset] = schemas.unset,
        failed: typing.Union['SegmentsRemoveUsersFromSegmentResponseFailed', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SegmentsRemoveUsersFromSegmentResponse':
        return super().__new__(
            cls,
            *args,
            succeeded=succeeded,
            failed=failed,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.segments_remove_users_from_segment_response_failed import SegmentsRemoveUsersFromSegmentResponseFailed
from dev_python_sdk.model.segments_remove_users_from_segment_response_succeeded import SegmentsRemoveUsersFromSegmentResponseSucceeded

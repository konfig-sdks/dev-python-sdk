# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from dev_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from dev_python_sdk.api_response import AsyncGeneratorResponse
from dev_python_sdk import api_client, exceptions
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

from dev_python_sdk.model.segment_user_ids import SegmentUserIds as SegmentUserIdsSchema
from dev_python_sdk.model.segments_add_users_to_segment422_response import SegmentsAddUsersToSegment422Response as SegmentsAddUsersToSegment422ResponseSchema
from dev_python_sdk.model.segments_add_users_to_segment401_response import SegmentsAddUsersToSegment401Response as SegmentsAddUsersToSegment401ResponseSchema
from dev_python_sdk.model.segments_add_users_to_segment_response import SegmentsAddUsersToSegmentResponse as SegmentsAddUsersToSegmentResponseSchema
from dev_python_sdk.model.segments_add_users_to_segment404_response import SegmentsAddUsersToSegment404Response as SegmentsAddUsersToSegment404ResponseSchema
from dev_python_sdk.model.segment_user_ids_user_ids import SegmentUserIdsUserIds as SegmentUserIdsUserIdsSchema

from dev_python_sdk.type.segments_add_users_to_segment422_response import SegmentsAddUsersToSegment422Response
from dev_python_sdk.type.segments_add_users_to_segment401_response import SegmentsAddUsersToSegment401Response
from dev_python_sdk.type.segments_add_users_to_segment404_response import SegmentsAddUsersToSegment404Response
from dev_python_sdk.type.segment_user_ids_user_ids import SegmentUserIdsUserIds
from dev_python_sdk.type.segments_add_users_to_segment_response import SegmentsAddUsersToSegmentResponse
from dev_python_sdk.type.segment_user_ids import SegmentUserIds

from ...api_client import Dictionary
from dev_python_sdk.pydantic.segments_add_users_to_segment422_response import SegmentsAddUsersToSegment422Response as SegmentsAddUsersToSegment422ResponsePydantic
from dev_python_sdk.pydantic.segment_user_ids_user_ids import SegmentUserIdsUserIds as SegmentUserIdsUserIdsPydantic
from dev_python_sdk.pydantic.segments_add_users_to_segment401_response import SegmentsAddUsersToSegment401Response as SegmentsAddUsersToSegment401ResponsePydantic
from dev_python_sdk.pydantic.segments_add_users_to_segment404_response import SegmentsAddUsersToSegment404Response as SegmentsAddUsersToSegment404ResponsePydantic
from dev_python_sdk.pydantic.segments_add_users_to_segment_response import SegmentsAddUsersToSegmentResponse as SegmentsAddUsersToSegmentResponsePydantic
from dev_python_sdk.pydantic.segment_user_ids import SegmentUserIds as SegmentUserIdsPydantic

# Path params


class IdSchema(
    schemas.Int32Schema
):
    pass
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = SegmentUserIdsSchema


request_body_segment_user_ids = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = SegmentsAddUsersToSegmentResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SegmentsAddUsersToSegmentResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SegmentsAddUsersToSegmentResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = SegmentsAddUsersToSegment401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: SegmentsAddUsersToSegment401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: SegmentsAddUsersToSegment401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = SegmentsAddUsersToSegment404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: SegmentsAddUsersToSegment404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: SegmentsAddUsersToSegment404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = SegmentsAddUsersToSegment422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: SegmentsAddUsersToSegment422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: SegmentsAddUsersToSegment422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_users_to_segment_mapped_args(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if user_ids is not None:
            _body["user_ids"] = user_ids
        args.body = _body
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aadd_users_to_segment_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add users to a manually managed audience segment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/segments/{id}/add_users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_segment_user_ids.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _add_users_to_segment_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add users to a manually managed audience segment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/segments/{id}/add_users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_segment_user_ids.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class AddUsersToSegmentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_users_to_segment(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_users_to_segment_mapped_args(
            id=id,
            user_ids=user_ids,
        )
        return await self._aadd_users_to_segment_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_users_to_segment(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_users_to_segment_mapped_args(
            id=id,
            user_ids=user_ids,
        )
        return self._add_users_to_segment_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddUsersToSegment(BaseApi):

    async def aadd_users_to_segment(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
        validate: bool = False,
        **kwargs,
    ) -> SegmentsAddUsersToSegmentResponsePydantic:
        raw_response = await self.raw.aadd_users_to_segment(
            id=id,
            user_ids=user_ids,
            **kwargs,
        )
        if validate:
            return SegmentsAddUsersToSegmentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SegmentsAddUsersToSegmentResponsePydantic, raw_response.body)
    
    
    def add_users_to_segment(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
        validate: bool = False,
    ) -> SegmentsAddUsersToSegmentResponsePydantic:
        raw_response = self.raw.add_users_to_segment(
            id=id,
            user_ids=user_ids,
        )
        if validate:
            return SegmentsAddUsersToSegmentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SegmentsAddUsersToSegmentResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_users_to_segment_mapped_args(
            id=id,
            user_ids=user_ids,
        )
        return await self._aadd_users_to_segment_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        id: int,
        user_ids: typing.Optional[SegmentUserIdsUserIds] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_users_to_segment_mapped_args(
            id=id,
            user_ids=user_ids,
        )
        return self._add_users_to_segment_oapg(
            body=args.body,
            path_params=args.path,
        )

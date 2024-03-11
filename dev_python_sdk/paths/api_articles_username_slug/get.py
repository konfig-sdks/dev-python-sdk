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

from dev_python_sdk.model.articles_get_by_path_response import ArticlesGetByPathResponse as ArticlesGetByPathResponseSchema
from dev_python_sdk.model.articles_get_by_path404_response import ArticlesGetByPath404Response as ArticlesGetByPath404ResponseSchema

from dev_python_sdk.type.articles_get_by_path404_response import ArticlesGetByPath404Response
from dev_python_sdk.type.articles_get_by_path_response import ArticlesGetByPathResponse

from ...api_client import Dictionary
from dev_python_sdk.pydantic.articles_get_by_path404_response import ArticlesGetByPath404Response as ArticlesGetByPath404ResponsePydantic
from dev_python_sdk.pydantic.articles_get_by_path_response import ArticlesGetByPathResponse as ArticlesGetByPathResponsePydantic

from . import path

# Path params
UsernameSchema = schemas.StrSchema
SlugSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'username': typing.Union[UsernameSchema, str, ],
        'slug': typing.Union[SlugSchema, str, ],
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


request_path_username = api_client.PathParameter(
    name="username",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UsernameSchema,
    required=True,
)
request_path_slug = api_client.PathParameter(
    name="slug",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SlugSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ArticlesGetByPathResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ArticlesGetByPathResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ArticlesGetByPathResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ArticlesGetByPath404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ArticlesGetByPath404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ArticlesGetByPath404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_by_path_mapped_args(
        self,
        username: str,
        slug: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if username is not None:
            _path_params["username"] = username
        if slug is not None:
            _path_params["slug"] = slug
        args.path = _path_params
        return args

    async def _aget_by_path_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Published article by path
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_username,
            request_path_slug,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/articles/{username}/{slug}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_by_path_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Published article by path
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_username,
            request_path_slug,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/articles/{username}/{slug}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetByPathRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_by_path(
        self,
        username: str,
        slug: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_path_mapped_args(
            username=username,
            slug=slug,
        )
        return await self._aget_by_path_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_path(
        self,
        username: str,
        slug: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_path_mapped_args(
            username=username,
            slug=slug,
        )
        return self._get_by_path_oapg(
            path_params=args.path,
        )

class GetByPath(BaseApi):

    async def aget_by_path(
        self,
        username: str,
        slug: str,
        validate: bool = False,
        **kwargs,
    ) -> ArticlesGetByPathResponsePydantic:
        raw_response = await self.raw.aget_by_path(
            username=username,
            slug=slug,
            **kwargs,
        )
        if validate:
            return RootModel[ArticlesGetByPathResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ArticlesGetByPathResponsePydantic, raw_response.body)
    
    
    def get_by_path(
        self,
        username: str,
        slug: str,
        validate: bool = False,
    ) -> ArticlesGetByPathResponsePydantic:
        raw_response = self.raw.get_by_path(
            username=username,
            slug=slug,
        )
        if validate:
            return RootModel[ArticlesGetByPathResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ArticlesGetByPathResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        username: str,
        slug: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_path_mapped_args(
            username=username,
            slug=slug,
        )
        return await self._aget_by_path_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        username: str,
        slug: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_path_mapped_args(
            username=username,
            slug=slug,
        )
        return self._get_by_path_oapg(
            path_params=args.path,
        )


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

from dev_python_sdk.model.reactions_create_reaction401_response import ReactionsCreateReaction401Response as ReactionsCreateReaction401ResponseSchema
from dev_python_sdk.model.reactions_create_reaction_response import ReactionsCreateReactionResponse as ReactionsCreateReactionResponseSchema

from dev_python_sdk.type.reactions_create_reaction401_response import ReactionsCreateReaction401Response
from dev_python_sdk.type.reactions_create_reaction_response import ReactionsCreateReactionResponse

from ...api_client import Dictionary
from dev_python_sdk.pydantic.reactions_create_reaction_response import ReactionsCreateReactionResponse as ReactionsCreateReactionResponsePydantic
from dev_python_sdk.pydantic.reactions_create_reaction401_response import ReactionsCreateReaction401Response as ReactionsCreateReaction401ResponsePydantic

from . import path

# Query params


class CategorySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "like": "LIKE",
            "unicorn": "UNICORN",
            "exploding_head": "EXPLODING_HEAD",
            "raised_hands": "RAISED_HANDS",
            "fire": "FIRE",
        }
    
    @schemas.classproperty
    def LIKE(cls):
        return cls("like")
    
    @schemas.classproperty
    def UNICORN(cls):
        return cls("unicorn")
    
    @schemas.classproperty
    def EXPLODING_HEAD(cls):
        return cls("exploding_head")
    
    @schemas.classproperty
    def RAISED_HANDS(cls):
        return cls("raised_hands")
    
    @schemas.classproperty
    def FIRE(cls):
        return cls("fire")
ReactableIdSchema = schemas.Int32Schema


class ReactableTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "Comment": "COMMENT",
            "Article": "ARTICLE",
            "User": "USER",
        }
    
    @schemas.classproperty
    def COMMENT(cls):
        return cls("Comment")
    
    @schemas.classproperty
    def ARTICLE(cls):
        return cls("Article")
    
    @schemas.classproperty
    def USER(cls):
        return cls("User")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'category': typing.Union[CategorySchema, str, ],
        'reactable_id': typing.Union[ReactableIdSchema, decimal.Decimal, int, ],
        'reactable_type': typing.Union[ReactableTypeSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_category = api_client.QueryParameter(
    name="category",
    style=api_client.ParameterStyle.FORM,
    schema=CategorySchema,
    required=True,
    explode=True,
)
request_query_reactable_id = api_client.QueryParameter(
    name="reactable_id",
    style=api_client.ParameterStyle.FORM,
    schema=ReactableIdSchema,
    required=True,
    explode=True,
)
request_query_reactable_type = api_client.QueryParameter(
    name="reactable_type",
    style=api_client.ParameterStyle.FORM,
    schema=ReactableTypeSchema,
    required=True,
    explode=True,
)
_auth = [
    'api-key',
]
SchemaFor200ResponseBodyApplicationJson = ReactionsCreateReactionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReactionsCreateReactionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReactionsCreateReactionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ReactionsCreateReaction401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ReactionsCreateReaction401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ReactionsCreateReaction401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_reaction_mapped_args(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if category is not None:
            _query_params["category"] = category
        if reactable_id is not None:
            _query_params["reactable_id"] = reactable_id
        if reactable_type is not None:
            _query_params["reactable_type"] = reactable_type
        args.query = _query_params
        return args

    async def _acreate_reaction_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        create reaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_category,
            request_query_reactable_id,
            request_query_reactable_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/reactions',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _create_reaction_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        create reaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_category,
            request_query_reactable_id,
            request_query_reactable_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/reactions',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class CreateReactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_reaction(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_reaction_mapped_args(
            category=category,
            reactable_id=reactable_id,
            reactable_type=reactable_type,
        )
        return await self._acreate_reaction_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def create_reaction(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_reaction_mapped_args(
            category=category,
            reactable_id=reactable_id,
            reactable_type=reactable_type,
        )
        return self._create_reaction_oapg(
            query_params=args.query,
        )

class CreateReaction(BaseApi):

    async def acreate_reaction(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
        validate: bool = False,
        **kwargs,
    ) -> ReactionsCreateReactionResponsePydantic:
        raw_response = await self.raw.acreate_reaction(
            category=category,
            reactable_id=reactable_id,
            reactable_type=reactable_type,
            **kwargs,
        )
        if validate:
            return ReactionsCreateReactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReactionsCreateReactionResponsePydantic, raw_response.body)
    
    
    def create_reaction(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
        validate: bool = False,
    ) -> ReactionsCreateReactionResponsePydantic:
        raw_response = self.raw.create_reaction(
            category=category,
            reactable_id=reactable_id,
            reactable_type=reactable_type,
        )
        if validate:
            return ReactionsCreateReactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReactionsCreateReactionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_reaction_mapped_args(
            category=category,
            reactable_id=reactable_id,
            reactable_type=reactable_type,
        )
        return await self._acreate_reaction_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        category: str,
        reactable_id: int,
        reactable_type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_reaction_mapped_args(
            category=category,
            reactable_id=reactable_id,
            reactable_type=reactable_type,
        )
        return self._create_reaction_oapg(
            query_params=args.query,
        )


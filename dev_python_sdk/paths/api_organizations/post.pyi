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

from dev_python_sdk.model.organizations_create_new_organization_response import OrganizationsCreateNewOrganizationResponse as OrganizationsCreateNewOrganizationResponseSchema
from dev_python_sdk.model.organizations_create_new_organization422_response import OrganizationsCreateNewOrganization422Response as OrganizationsCreateNewOrganization422ResponseSchema
from dev_python_sdk.model.organization import Organization as OrganizationSchema

from dev_python_sdk.type.organization import Organization
from dev_python_sdk.type.organizations_create_new_organization_response import OrganizationsCreateNewOrganizationResponse
from dev_python_sdk.type.organizations_create_new_organization422_response import OrganizationsCreateNewOrganization422Response

from ...api_client import Dictionary
from dev_python_sdk.pydantic.organizations_create_new_organization_response import OrganizationsCreateNewOrganizationResponse as OrganizationsCreateNewOrganizationResponsePydantic
from dev_python_sdk.pydantic.organization import Organization as OrganizationPydantic
from dev_python_sdk.pydantic.organizations_create_new_organization422_response import OrganizationsCreateNewOrganization422Response as OrganizationsCreateNewOrganization422ResponsePydantic

# body param
SchemaForRequestBodyApplicationJson = OrganizationSchema


request_body_organization = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = OrganizationsCreateNewOrganizationResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: OrganizationsCreateNewOrganizationResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: OrganizationsCreateNewOrganizationResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)
SchemaFor422ResponseBodyApplicationJson = OrganizationsCreateNewOrganization422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: OrganizationsCreateNewOrganization422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: OrganizationsCreateNewOrganization422Response


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

    def _create_new_organization_mapped_args(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if summary is not None:
            _body["summary"] = summary
        if type_of is not None:
            _body["type_of"] = type_of
        if username is not None:
            _body["username"] = username
        if name is not None:
            _body["name"] = name
        if twitter_username is not None:
            _body["twitter_username"] = twitter_username
        if github_username is not None:
            _body["github_username"] = github_username
        if url is not None:
            _body["url"] = url
        if location is not None:
            _body["location"] = location
        if joined_at is not None:
            _body["joined_at"] = joined_at
        if tech_stack is not None:
            _body["tech_stack"] = tech_stack
        if tag_line is not None:
            _body["tag_line"] = tag_line
        if story is not None:
            _body["story"] = story
        args.body = _body
        return args

    async def _acreate_new_organization_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create an Organization
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/organizations',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_organization.serialize(body, content_type)
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


    def _create_new_organization_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create an Organization
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/organizations',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_organization.serialize(body, content_type)
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


class CreateNewOrganizationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_organization(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_organization_mapped_args(
            summary=summary,
            type_of=type_of,
            username=username,
            name=name,
            twitter_username=twitter_username,
            github_username=github_username,
            url=url,
            location=location,
            joined_at=joined_at,
            tech_stack=tech_stack,
            tag_line=tag_line,
            story=story,
        )
        return await self._acreate_new_organization_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_organization(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_organization_mapped_args(
            summary=summary,
            type_of=type_of,
            username=username,
            name=name,
            twitter_username=twitter_username,
            github_username=github_username,
            url=url,
            location=location,
            joined_at=joined_at,
            tech_stack=tech_stack,
            tag_line=tag_line,
            story=story,
        )
        return self._create_new_organization_oapg(
            body=args.body,
        )

class CreateNewOrganization(BaseApi):

    async def acreate_new_organization(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrganizationsCreateNewOrganizationResponsePydantic:
        raw_response = await self.raw.acreate_new_organization(
            summary=summary,
            type_of=type_of,
            username=username,
            name=name,
            twitter_username=twitter_username,
            github_username=github_username,
            url=url,
            location=location,
            joined_at=joined_at,
            tech_stack=tech_stack,
            tag_line=tag_line,
            story=story,
            **kwargs,
        )
        if validate:
            return OrganizationsCreateNewOrganizationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrganizationsCreateNewOrganizationResponsePydantic, raw_response.body)
    
    
    def create_new_organization(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> OrganizationsCreateNewOrganizationResponsePydantic:
        raw_response = self.raw.create_new_organization(
            summary=summary,
            type_of=type_of,
            username=username,
            name=name,
            twitter_username=twitter_username,
            github_username=github_username,
            url=url,
            location=location,
            joined_at=joined_at,
            tech_stack=tech_stack,
            tag_line=tag_line,
            story=story,
        )
        if validate:
            return OrganizationsCreateNewOrganizationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrganizationsCreateNewOrganizationResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_organization_mapped_args(
            summary=summary,
            type_of=type_of,
            username=username,
            name=name,
            twitter_username=twitter_username,
            github_username=github_username,
            url=url,
            location=location,
            joined_at=joined_at,
            tech_stack=tech_stack,
            tag_line=tag_line,
            story=story,
        )
        return await self._acreate_new_organization_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        summary: typing.Optional[str] = None,
        type_of: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        twitter_username: typing.Optional[str] = None,
        github_username: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        joined_at: typing.Optional[str] = None,
        tech_stack: typing.Optional[str] = None,
        tag_line: typing.Optional[typing.Optional[str]] = None,
        story: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_organization_mapped_args(
            summary=summary,
            type_of=type_of,
            username=username,
            name=name,
            twitter_username=twitter_username,
            github_username=github_username,
            url=url,
            location=location,
            joined_at=joined_at,
            tech_stack=tech_stack,
            tag_line=tag_line,
            story=story,
        )
        return self._create_new_organization_oapg(
            body=args.body,
        )


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


class OrganizationsCreateNewOrganizationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            summary = schemas.StrSchema
            id = schemas.NumberSchema
            name = schemas.StrSchema
            profile_image = schemas.StrSchema
            slug = schemas.StrSchema
            tag_line = schemas.StrSchema
            url = schemas.StrSchema
            __annotations__ = {
                "summary": summary,
                "id": id,
                "name": name,
                "profile_image": profile_image,
                "slug": slug,
                "tag_line": tag_line,
                "url": url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile_image"]) -> MetaOapg.properties.profile_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_line"]) -> MetaOapg.properties.tag_line: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "id", "name", "profile_image", "slug", "tag_line", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile_image"]) -> typing.Union[MetaOapg.properties.profile_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_line"]) -> typing.Union[MetaOapg.properties.tag_line, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "id", "name", "profile_image", "slug", "tag_line", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        profile_image: typing.Union[MetaOapg.properties.profile_image, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        tag_line: typing.Union[MetaOapg.properties.tag_line, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrganizationsCreateNewOrganizationResponse':
        return super().__new__(
            cls,
            *args,
            summary=summary,
            id=id,
            name=name,
            profile_image=profile_image,
            slug=slug,
            tag_line=tag_line,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

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


class PodcastEpisodeIndex(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Representation of a podcast episode returned in a list
    """


    class MetaOapg:
        required = {
            "path",
            "image_url",
            "podcast",
            "type_of",
            "id",
            "title",
            "class_name",
        }
        
        class properties:
            title = schemas.StrSchema
            type_of = schemas.StrSchema
            id = schemas.Int32Schema
            class_name = schemas.StrSchema
            path = schemas.StrSchema
            image_url = schemas.StrSchema
        
            @staticmethod
            def podcast() -> typing.Type['SharedPodcast']:
                return SharedPodcast
            __annotations__ = {
                "title": title,
                "type_of": type_of,
                "id": id,
                "class_name": class_name,
                "path": path,
                "image_url": image_url,
                "podcast": podcast,
            }
    
    path: MetaOapg.properties.path
    image_url: MetaOapg.properties.image_url
    podcast: 'SharedPodcast'
    type_of: MetaOapg.properties.type_of
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    class_name: MetaOapg.properties.class_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_of"]) -> MetaOapg.properties.type_of: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["class_name"]) -> MetaOapg.properties.class_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_url"]) -> MetaOapg.properties.image_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["podcast"]) -> 'SharedPodcast': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "type_of", "id", "class_name", "path", "image_url", "podcast", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_of"]) -> MetaOapg.properties.type_of: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["class_name"]) -> MetaOapg.properties.class_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_url"]) -> MetaOapg.properties.image_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["podcast"]) -> 'SharedPodcast': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "type_of", "id", "class_name", "path", "image_url", "podcast", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        path: typing.Union[MetaOapg.properties.path, str, ],
        image_url: typing.Union[MetaOapg.properties.image_url, str, ],
        podcast: 'SharedPodcast',
        type_of: typing.Union[MetaOapg.properties.type_of, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        class_name: typing.Union[MetaOapg.properties.class_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PodcastEpisodeIndex':
        return super().__new__(
            cls,
            *args,
            path=path,
            image_url=image_url,
            podcast=podcast,
            type_of=type_of,
            id=id,
            title=title,
            class_name=class_name,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.shared_podcast import SharedPodcast
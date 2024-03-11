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


class VideoArticle(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Representation of an Article with video
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            type_of = schemas.StrSchema
            id = schemas.Int64Schema
            path = schemas.StrSchema
            cloudinary_video_url = schemas.StrSchema
            user_id = schemas.Int64Schema
            video_duration_in_minutes = schemas.StrSchema
            video_source_url = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['VideoArticleUser']:
                return VideoArticleUser
            __annotations__ = {
                "title": title,
                "type_of": type_of,
                "id": id,
                "path": path,
                "cloudinary_video_url": cloudinary_video_url,
                "user_id": user_id,
                "video_duration_in_minutes": video_duration_in_minutes,
                "video_source_url": video_source_url,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_of"]) -> MetaOapg.properties.type_of: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloudinary_video_url"]) -> MetaOapg.properties.cloudinary_video_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["video_duration_in_minutes"]) -> MetaOapg.properties.video_duration_in_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["video_source_url"]) -> MetaOapg.properties.video_source_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'VideoArticleUser': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "type_of", "id", "path", "cloudinary_video_url", "user_id", "video_duration_in_minutes", "video_source_url", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_of"]) -> typing.Union[MetaOapg.properties.type_of, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloudinary_video_url"]) -> typing.Union[MetaOapg.properties.cloudinary_video_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["video_duration_in_minutes"]) -> typing.Union[MetaOapg.properties.video_duration_in_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["video_source_url"]) -> typing.Union[MetaOapg.properties.video_source_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['VideoArticleUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "type_of", "id", "path", "cloudinary_video_url", "user_id", "video_duration_in_minutes", "video_source_url", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        type_of: typing.Union[MetaOapg.properties.type_of, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        cloudinary_video_url: typing.Union[MetaOapg.properties.cloudinary_video_url, str, schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        video_duration_in_minutes: typing.Union[MetaOapg.properties.video_duration_in_minutes, str, schemas.Unset] = schemas.unset,
        video_source_url: typing.Union[MetaOapg.properties.video_source_url, str, schemas.Unset] = schemas.unset,
        user: typing.Union['VideoArticleUser', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoArticle':
        return super().__new__(
            cls,
            *args,
            title=title,
            type_of=type_of,
            id=id,
            path=path,
            cloudinary_video_url=cloudinary_video_url,
            user_id=user_id,
            video_duration_in_minutes=video_duration_in_minutes,
            video_source_url=video_source_url,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.video_article_user import VideoArticleUser

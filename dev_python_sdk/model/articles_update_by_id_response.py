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


class ArticlesUpdateByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['ArticlesUpdateByIdResponseTags']:
                return ArticlesUpdateByIdResponseTags
            title = schemas.StrSchema
            description = schemas.StrSchema
            type_of = schemas.StrSchema
            id = schemas.NumberSchema
            readable_publish_date = schemas.StrSchema
            slug = schemas.StrSchema
            path = schemas.StrSchema
            url = schemas.StrSchema
            comments_count = schemas.NumberSchema
            public_reactions_count = schemas.NumberSchema
            
            
            class collection_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'collection_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            published_timestamp = schemas.StrSchema
            positive_reactions_count = schemas.NumberSchema
            cover_image = schemas.StrSchema
            social_image = schemas.StrSchema
            canonical_url = schemas.StrSchema
            created_at = schemas.StrSchema
            edited_at = schemas.StrSchema
            
            
            class crossposted_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'crossposted_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            published_at = schemas.StrSchema
            last_comment_at = schemas.StrSchema
            reading_time_minutes = schemas.NumberSchema
            tag_list = schemas.StrSchema
            body_html = schemas.StrSchema
            body_markdown = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['ArticlesUpdateByIdResponseUser']:
                return ArticlesUpdateByIdResponseUser
            __annotations__ = {
                "tags": tags,
                "title": title,
                "description": description,
                "type_of": type_of,
                "id": id,
                "readable_publish_date": readable_publish_date,
                "slug": slug,
                "path": path,
                "url": url,
                "comments_count": comments_count,
                "public_reactions_count": public_reactions_count,
                "collection_id": collection_id,
                "published_timestamp": published_timestamp,
                "positive_reactions_count": positive_reactions_count,
                "cover_image": cover_image,
                "social_image": social_image,
                "canonical_url": canonical_url,
                "created_at": created_at,
                "edited_at": edited_at,
                "crossposted_at": crossposted_at,
                "published_at": published_at,
                "last_comment_at": last_comment_at,
                "reading_time_minutes": reading_time_minutes,
                "tag_list": tag_list,
                "body_html": body_html,
                "body_markdown": body_markdown,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'ArticlesUpdateByIdResponseTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_of"]) -> MetaOapg.properties.type_of: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readable_publish_date"]) -> MetaOapg.properties.readable_publish_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments_count"]) -> MetaOapg.properties.comments_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_reactions_count"]) -> MetaOapg.properties.public_reactions_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_timestamp"]) -> MetaOapg.properties.published_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positive_reactions_count"]) -> MetaOapg.properties.positive_reactions_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_image"]) -> MetaOapg.properties.cover_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_image"]) -> MetaOapg.properties.social_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canonical_url"]) -> MetaOapg.properties.canonical_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edited_at"]) -> MetaOapg.properties.edited_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crossposted_at"]) -> MetaOapg.properties.crossposted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_at"]) -> MetaOapg.properties.published_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_comment_at"]) -> MetaOapg.properties.last_comment_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reading_time_minutes"]) -> MetaOapg.properties.reading_time_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_list"]) -> MetaOapg.properties.tag_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_html"]) -> MetaOapg.properties.body_html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_markdown"]) -> MetaOapg.properties.body_markdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'ArticlesUpdateByIdResponseUser': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "title", "description", "type_of", "id", "readable_publish_date", "slug", "path", "url", "comments_count", "public_reactions_count", "collection_id", "published_timestamp", "positive_reactions_count", "cover_image", "social_image", "canonical_url", "created_at", "edited_at", "crossposted_at", "published_at", "last_comment_at", "reading_time_minutes", "tag_list", "body_html", "body_markdown", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['ArticlesUpdateByIdResponseTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_of"]) -> typing.Union[MetaOapg.properties.type_of, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readable_publish_date"]) -> typing.Union[MetaOapg.properties.readable_publish_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments_count"]) -> typing.Union[MetaOapg.properties.comments_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_reactions_count"]) -> typing.Union[MetaOapg.properties.public_reactions_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_id"]) -> typing.Union[MetaOapg.properties.collection_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_timestamp"]) -> typing.Union[MetaOapg.properties.published_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positive_reactions_count"]) -> typing.Union[MetaOapg.properties.positive_reactions_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_image"]) -> typing.Union[MetaOapg.properties.cover_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_image"]) -> typing.Union[MetaOapg.properties.social_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canonical_url"]) -> typing.Union[MetaOapg.properties.canonical_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edited_at"]) -> typing.Union[MetaOapg.properties.edited_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crossposted_at"]) -> typing.Union[MetaOapg.properties.crossposted_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_at"]) -> typing.Union[MetaOapg.properties.published_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_comment_at"]) -> typing.Union[MetaOapg.properties.last_comment_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reading_time_minutes"]) -> typing.Union[MetaOapg.properties.reading_time_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_list"]) -> typing.Union[MetaOapg.properties.tag_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_html"]) -> typing.Union[MetaOapg.properties.body_html, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_markdown"]) -> typing.Union[MetaOapg.properties.body_markdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['ArticlesUpdateByIdResponseUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "title", "description", "type_of", "id", "readable_publish_date", "slug", "path", "url", "comments_count", "public_reactions_count", "collection_id", "published_timestamp", "positive_reactions_count", "cover_image", "social_image", "canonical_url", "created_at", "edited_at", "crossposted_at", "published_at", "last_comment_at", "reading_time_minutes", "tag_list", "body_html", "body_markdown", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union['ArticlesUpdateByIdResponseTags', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        type_of: typing.Union[MetaOapg.properties.type_of, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        readable_publish_date: typing.Union[MetaOapg.properties.readable_publish_date, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        comments_count: typing.Union[MetaOapg.properties.comments_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        public_reactions_count: typing.Union[MetaOapg.properties.public_reactions_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        collection_id: typing.Union[MetaOapg.properties.collection_id, None, str, schemas.Unset] = schemas.unset,
        published_timestamp: typing.Union[MetaOapg.properties.published_timestamp, str, schemas.Unset] = schemas.unset,
        positive_reactions_count: typing.Union[MetaOapg.properties.positive_reactions_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cover_image: typing.Union[MetaOapg.properties.cover_image, str, schemas.Unset] = schemas.unset,
        social_image: typing.Union[MetaOapg.properties.social_image, str, schemas.Unset] = schemas.unset,
        canonical_url: typing.Union[MetaOapg.properties.canonical_url, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        edited_at: typing.Union[MetaOapg.properties.edited_at, str, schemas.Unset] = schemas.unset,
        crossposted_at: typing.Union[MetaOapg.properties.crossposted_at, None, str, schemas.Unset] = schemas.unset,
        published_at: typing.Union[MetaOapg.properties.published_at, str, schemas.Unset] = schemas.unset,
        last_comment_at: typing.Union[MetaOapg.properties.last_comment_at, str, schemas.Unset] = schemas.unset,
        reading_time_minutes: typing.Union[MetaOapg.properties.reading_time_minutes, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tag_list: typing.Union[MetaOapg.properties.tag_list, str, schemas.Unset] = schemas.unset,
        body_html: typing.Union[MetaOapg.properties.body_html, str, schemas.Unset] = schemas.unset,
        body_markdown: typing.Union[MetaOapg.properties.body_markdown, str, schemas.Unset] = schemas.unset,
        user: typing.Union['ArticlesUpdateByIdResponseUser', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArticlesUpdateByIdResponse':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            title=title,
            description=description,
            type_of=type_of,
            id=id,
            readable_publish_date=readable_publish_date,
            slug=slug,
            path=path,
            url=url,
            comments_count=comments_count,
            public_reactions_count=public_reactions_count,
            collection_id=collection_id,
            published_timestamp=published_timestamp,
            positive_reactions_count=positive_reactions_count,
            cover_image=cover_image,
            social_image=social_image,
            canonical_url=canonical_url,
            created_at=created_at,
            edited_at=edited_at,
            crossposted_at=crossposted_at,
            published_at=published_at,
            last_comment_at=last_comment_at,
            reading_time_minutes=reading_time_minutes,
            tag_list=tag_list,
            body_html=body_html,
            body_markdown=body_markdown,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.articles_update_by_id_response_tags import ArticlesUpdateByIdResponseTags
from dev_python_sdk.model.articles_update_by_id_response_user import ArticlesUpdateByIdResponseUser
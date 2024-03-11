# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from dev_python_sdk.type.articles_update_by_id_response_tags import ArticlesUpdateByIdResponseTags
from dev_python_sdk.type.articles_update_by_id_response_user import ArticlesUpdateByIdResponseUser

class RequiredArticlesUpdateByIdResponse(TypedDict):
    pass

class OptionalArticlesUpdateByIdResponse(TypedDict, total=False):
    tags: ArticlesUpdateByIdResponseTags

    title: str

    description: str

    type_of: str

    id: typing.Union[int, float]

    readable_publish_date: str

    slug: str

    path: str

    url: str

    comments_count: typing.Union[int, float]

    public_reactions_count: typing.Union[int, float]

    collection_id: typing.Optional[str]

    published_timestamp: str

    positive_reactions_count: typing.Union[int, float]

    cover_image: str

    social_image: str

    canonical_url: str

    created_at: str

    edited_at: str

    crossposted_at: typing.Optional[str]

    published_at: str

    last_comment_at: str

    reading_time_minutes: typing.Union[int, float]

    tag_list: str

    body_html: str

    body_markdown: str

    user: ArticlesUpdateByIdResponseUser

class ArticlesUpdateByIdResponse(RequiredArticlesUpdateByIdResponse, OptionalArticlesUpdateByIdResponse):
    pass

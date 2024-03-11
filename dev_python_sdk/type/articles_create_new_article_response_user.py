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


class RequiredArticlesCreateNewArticleResponseUser(TypedDict):
    pass

class OptionalArticlesCreateNewArticleResponseUser(TypedDict, total=False):
    name: str

    username: str

    twitter_username: str

    github_username: str

    user_id: typing.Union[int, float]

    website_url: typing.Optional[str]

    profile_image: str

    profile_image_90: str

class ArticlesCreateNewArticleResponseUser(RequiredArticlesCreateNewArticleResponseUser, OptionalArticlesCreateNewArticleResponseUser):
    pass

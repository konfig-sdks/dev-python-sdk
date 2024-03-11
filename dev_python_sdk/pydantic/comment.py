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
from pydantic import BaseModel, Field, RootModel


class Comment(BaseModel):
    type_of: typing.Optional[str] = Field(None, alias='type_of')

    id_code: typing.Optional[str] = Field(None, alias='id_code')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # Podcast image url
    image_url: typing.Optional[str] = Field(None, alias='image_url')
    class Config:
        arbitrary_types_allowed = True
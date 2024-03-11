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


class RequiredSegmentsListAudienceSegments401Response(TypedDict):
    pass

class OptionalSegmentsListAudienceSegments401Response(TypedDict, total=False):
    error: str

    status: typing.Union[int, float]

class SegmentsListAudienceSegments401Response(RequiredSegmentsListAudienceSegments401Response, OptionalSegmentsListAudienceSegments401Response):
    pass

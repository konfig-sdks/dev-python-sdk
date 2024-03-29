# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dev_python_sdk.paths.api_follows_tags.get import GetTagList
from dev_python_sdk.paths.api_tags.get import ListByPopularity
from dev_python_sdk.apis.tags.tags_api_raw import TagsApiRaw


class TagsApi(
    GetTagList,
    ListByPopularity,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TagsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TagsApiRaw(api_client)

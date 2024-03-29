# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dev_python_sdk.paths.api_pages.post import CreateNewPage
from dev_python_sdk.paths.api_pages_id.get import GetDetails
from dev_python_sdk.paths.api_pages.get import ListAllDetails
from dev_python_sdk.paths.api_pages_id.delete import RemovePageById
from dev_python_sdk.paths.api_pages_id.put import UpdatePageDetails
from dev_python_sdk.apis.tags.pages_api_raw import PagesApiRaw


class PagesApi(
    CreateNewPage,
    GetDetails,
    ListAllDetails,
    RemovePageById,
    UpdatePageDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PagesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PagesApiRaw(api_client)

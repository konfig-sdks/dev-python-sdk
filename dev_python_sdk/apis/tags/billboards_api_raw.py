# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dev_python_sdk.paths.api_billboards.post import CreateNewBillboardRaw
from dev_python_sdk.paths.api_billboards_id.get import GetByIdRaw
from dev_python_sdk.paths.api_billboards.get import GetListRaw
from dev_python_sdk.paths.api_billboards_id_unpublish.put import UnpublishBillboardRaw
from dev_python_sdk.paths.api_billboards_id.put import UpdateByIdRaw


class BillboardsApiRaw(
    CreateNewBillboardRaw,
    GetByIdRaw,
    GetListRaw,
    UnpublishBillboardRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

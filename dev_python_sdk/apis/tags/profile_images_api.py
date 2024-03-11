# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dev_python_sdk.paths.api_profile_images_username.get import GetByUsername
from dev_python_sdk.apis.tags.profile_images_api_raw import ProfileImagesApiRaw


class ProfileImagesApi(
    GetByUsername,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProfileImagesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProfileImagesApiRaw(api_client)
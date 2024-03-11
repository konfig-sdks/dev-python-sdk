# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import dev_python_sdk
from dev_python_sdk.paths.api_users_id_limited import put
from dev_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiUsersIdLimited(ApiTestMixin, unittest.TestCase):
    """
    ApiUsersIdLimited unit test stubs
        Add limited role for a User
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from dev_python_sdk import Dev

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        dev = Dev(
        
                        api_key = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(dev)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
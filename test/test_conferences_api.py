# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import powerplay
from powerplay.api.conferences_api import ConferencesApi  # noqa: E501
from powerplay.rest import ApiException


class TestConferencesApi(unittest.TestCase):
    """ConferencesApi unit test stubs"""

    def setUp(self):
        self.api = ConferencesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_conference(self):
        """Test case for get_conference

        Get an NHL conference.  # noqa: E501
        """
        pass

    def test_get_conferences(self):
        """Test case for get_conferences

        Get all current NHL conferences.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

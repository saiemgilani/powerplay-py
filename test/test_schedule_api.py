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
from powerplay.api.schedule_api import ScheduleApi  # noqa: E501
from powerplay.rest import ApiException


class TestScheduleApi(unittest.TestCase):
    """ScheduleApi unit test stubs"""

    def setUp(self):
        self.api = ScheduleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_schedule(self):
        """Test case for get_schedule

        Get the NHL game schedule.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
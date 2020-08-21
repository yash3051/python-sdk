# coding: utf-8

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import meli
from meli.api.items_health_api import ItemsHealthApi  # noqa: E501
from meli.rest import ApiException


class TestItemsHealthApi(unittest.TestCase):
    """ItemsHealthApi unit test stubs"""

    def setUp(self):
        self.api = meli.api.items_health_api.ItemsHealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_items_id_health_actions_get(self):
        """Test case for items_id_health_actions_get

        Return item health actions by id.  # noqa: E501
        """
        pass

    def test_items_id_health_get(self):
        """Test case for items_id_health_get

        Return health by id.  # noqa: E501
        """
        pass

    def test_sites_site_id_health_levels_get(self):
        """Test case for sites_site_id_health_levels_get

        Return health levels.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
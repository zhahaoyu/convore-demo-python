# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.api.admin_api import AdminApi


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminApi()

    def tearDown(self) -> None:
        pass

    def test_create_api_key(self) -> None:
        """Test case for create_api_key

        Create an API key
        """
        pass

    def test_create_organization(self) -> None:
        """Test case for create_organization

        Create an organization
        """
        pass

    def test_get_current_user(self) -> None:
        """Test case for get_current_user

        Get the current user
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Get a user
        """
        pass

    def test_list_api_keys(self) -> None:
        """Test case for list_api_keys

        List API keys
        """
        pass

    def test_list_organizations(self) -> None:
        """Test case for list_organizations

        List organizations
        """
        pass

    def test_update_api_key(self) -> None:
        """Test case for update_api_key

        Update an API key
        """
        pass


if __name__ == '__main__':
    unittest.main()

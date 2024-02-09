# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.api.authorization_flows_api import AuthorizationFlowsApi


class TestAuthorizationFlowsApi(unittest.TestCase):
    """AuthorizationFlowsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthorizationFlowsApi()

    def tearDown(self) -> None:
        pass

    def test_create_authorization_flow(self) -> None:
        """Test case for create_authorization_flow

        Create an authorization flow. This is usually an OAuth2 authorization code flow where the user is redirected to the selected provider's authorization page and grants access to their account.
        """
        pass


if __name__ == '__main__':
    unittest.main()

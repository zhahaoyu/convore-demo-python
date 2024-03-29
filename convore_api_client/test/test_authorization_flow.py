# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.authorization_flow import AuthorizationFlow

class TestAuthorizationFlow(unittest.TestCase):
    """AuthorizationFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorizationFlow:
        """Test AuthorizationFlow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorizationFlow`
        """
        model = AuthorizationFlow()
        if include_optional:
            return AuthorizationFlow(
                id = '',
                connector_id = '',
                success_redirect_uri = '',
                error_redirect_uri = '',
                status = 'active',
                grant_url = '',
                connected_channel_id = ''
            )
        else:
            return AuthorizationFlow(
                id = '',
                connector_id = '',
                success_redirect_uri = '',
                error_redirect_uri = '',
                status = 'active',
                grant_url = '',
        )
        """

    def testAuthorizationFlow(self):
        """Test AuthorizationFlow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

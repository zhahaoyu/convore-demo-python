# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.page_api_key import PageApiKey

class TestPageApiKey(unittest.TestCase):
    """PageApiKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageApiKey:
        """Test PageApiKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageApiKey`
        """
        model = PageApiKey()
        if include_optional:
            return PageApiKey(
                data = [
                    convore_api_client.models.api_key.ApiKey(
                        id = '', 
                        name = '', 
                        organization_id = '', 
                        publishable_key = '', 
                        secret_key = '', 
                        secret_key_display = '', 
                        disabled = True, 
                        hide_secret_key = True, )
                    ],
                next_cursor = '',
                total_count = 56
            )
        else:
            return PageApiKey(
                data = [
                    convore_api_client.models.api_key.ApiKey(
                        id = '', 
                        name = '', 
                        organization_id = '', 
                        publishable_key = '', 
                        secret_key = '', 
                        secret_key_display = '', 
                        disabled = True, 
                        hide_secret_key = True, )
                    ],
        )
        """

    def testPageApiKey(self):
        """Test PageApiKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

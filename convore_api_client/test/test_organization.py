# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.organization import Organization

class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Organization:
        """Test Organization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Organization`
        """
        model = Organization()
        if include_optional:
            return Organization(
                id = '',
                name = ''
            )
        else:
            return Organization(
                id = '',
                name = '',
        )
        """

    def testOrganization(self):
        """Test Organization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

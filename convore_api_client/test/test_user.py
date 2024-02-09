# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.user import User

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()
        if include_optional:
            return User(
                id = '',
                first_name = 'John',
                last_name = 'Doe',
                name = '',
                email = 'john@example.com',
                picture = '',
                organization_ids = [
                    ''
                    ],
                system_role = 'user'
            )
        else:
            return User(
                id = '',
                first_name = 'John',
                last_name = 'Doe',
                name = '',
                email = 'john@example.com',
                organization_ids = [
                    ''
                    ],
                system_role = 'user',
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
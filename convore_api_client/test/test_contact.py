# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.contact import Contact

class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Contact:
        """Test Contact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Contact`
        """
        model = Contact()
        if include_optional:
            return Contact(
                id = 'cntct_01hcf9x766fqk8g7hz74363j9q',
                name = 'John Doe',
                description = 'Head of Sales, Acme Corp.',
                handles = [
                    convore_api_client.models.contact_handle.ContactHandle(
                        type = 'email', 
                        value = 'john@example.com', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Contact(
                id = 'cntct_01hcf9x766fqk8g7hz74363j9q',
                name = 'John Doe',
                handles = [
                    convore_api_client.models.contact_handle.ContactHandle(
                        type = 'email', 
                        value = 'john@example.com', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testContact(self):
        """Test Contact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
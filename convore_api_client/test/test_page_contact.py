# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.page_contact import PageContact

class TestPageContact(unittest.TestCase):
    """PageContact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageContact:
        """Test PageContact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageContact`
        """
        model = PageContact()
        if include_optional:
            return PageContact(
                data = [
                    convore_api_client.models.contact.Contact(
                        id = 'cntct_01hcf9x766fqk8g7hz74363j9q', 
                        name = 'John Doe', 
                        description = 'Head of Sales, Acme Corp.', 
                        handles = [
                            convore_api_client.models.contact_handle.ContactHandle(
                                type = 'email', 
                                value = 'john@example.com', )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_cursor = '',
                total_count = 56
            )
        else:
            return PageContact(
                data = [
                    convore_api_client.models.contact.Contact(
                        id = 'cntct_01hcf9x766fqk8g7hz74363j9q', 
                        name = 'John Doe', 
                        description = 'Head of Sales, Acme Corp.', 
                        handles = [
                            convore_api_client.models.contact_handle.ContactHandle(
                                type = 'email', 
                                value = 'john@example.com', )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testPageContact(self):
        """Test PageContact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

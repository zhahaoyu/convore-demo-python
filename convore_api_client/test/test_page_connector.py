# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.page_connector import PageConnector

class TestPageConnector(unittest.TestCase):
    """PageConnector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageConnector:
        """Test PageConnector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageConnector`
        """
        model = PageConnector()
        if include_optional:
            return PageConnector(
                data = [
                    convore_api_client.models.connector.Connector(
                        id = 'conntr_01hcf9x766fqk8g7hz74363j9q', 
                        provider = 'convore_mail', 
                        name = 'Acme Corp's Gmail OAuth App', 
                        gmail = convore_api_client.models.gmail_connector.GmailConnector(
                            client_id = '', ), 
                        ses = convore_api_client.models.ses_connector.SesConnector(
                            access_key_id = '', 
                            region = '', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_cursor = '',
                total_count = 56
            )
        else:
            return PageConnector(
                data = [
                    convore_api_client.models.connector.Connector(
                        id = 'conntr_01hcf9x766fqk8g7hz74363j9q', 
                        provider = 'convore_mail', 
                        name = 'Acme Corp's Gmail OAuth App', 
                        gmail = convore_api_client.models.gmail_connector.GmailConnector(
                            client_id = '', ), 
                        ses = convore_api_client.models.ses_connector.SesConnector(
                            access_key_id = '', 
                            region = '', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testPageConnector(self):
        """Test PageConnector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

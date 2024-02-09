# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.connector import Connector

class TestConnector(unittest.TestCase):
    """Connector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Connector:
        """Test Connector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Connector`
        """
        model = Connector()
        if include_optional:
            return Connector(
                id = 'conntr_01hcf9x766fqk8g7hz74363j9q',
                provider = 'convore_mail',
                name = 'Acme Corp's Gmail OAuth App',
                gmail = convore_api_client.models.gmail_connector.GmailConnector(
                    client_id = '', ),
                ses = convore_api_client.models.ses_connector.SesConnector(
                    access_key_id = '', 
                    region = '', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Connector(
                id = 'conntr_01hcf9x766fqk8g7hz74363j9q',
                provider = 'convore_mail',
                name = 'Acme Corp's Gmail OAuth App',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testConnector(self):
        """Test Connector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
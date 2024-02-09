# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.create_connector_request import CreateConnectorRequest

class TestCreateConnectorRequest(unittest.TestCase):
    """CreateConnectorRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateConnectorRequest:
        """Test CreateConnectorRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateConnectorRequest`
        """
        model = CreateConnectorRequest()
        if include_optional:
            return CreateConnectorRequest(
                provider = 'convore_mail',
                name = 'Acme Corp's Gmail OAuth App',
                gmail = convore_api_client.models.create_gmail_connector_params.CreateGmailConnectorParams(
                    client_id = '', 
                    client_secret = '', ),
                ses = convore_api_client.models.create_ses_connector_params.CreateSesConnectorParams(
                    access_key_id = '', 
                    secret_access_key = '', 
                    region = '', )
            )
        else:
            return CreateConnectorRequest(
                provider = 'convore_mail',
        )
        """

    def testCreateConnectorRequest(self):
        """Test CreateConnectorRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

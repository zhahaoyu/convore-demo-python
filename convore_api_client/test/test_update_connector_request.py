# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.update_connector_request import UpdateConnectorRequest

class TestUpdateConnectorRequest(unittest.TestCase):
    """UpdateConnectorRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateConnectorRequest:
        """Test UpdateConnectorRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateConnectorRequest`
        """
        model = UpdateConnectorRequest()
        if include_optional:
            return UpdateConnectorRequest(
                name = 'Acme Corp's Gmail OAuth App',
                gmail = convore_api_client.models.update_gmail_connector_params.UpdateGmailConnectorParams(
                    client_id = '', 
                    client_secret = '', ),
                ses = convore_api_client.models.update_ses_connector_params.UpdateSesConnectorParams(
                    access_key_id = '', 
                    secret_access_key = '', 
                    region = '', )
            )
        else:
            return UpdateConnectorRequest(
        )
        """

    def testUpdateConnectorRequest(self):
        """Test UpdateConnectorRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

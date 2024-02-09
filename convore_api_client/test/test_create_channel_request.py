# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.create_channel_request import CreateChannelRequest

class TestCreateChannelRequest(unittest.TestCase):
    """CreateChannelRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateChannelRequest:
        """Test CreateChannelRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateChannelRequest`
        """
        model = CreateChannelRequest()
        if include_optional:
            return CreateChannelRequest(
                connector_id = 'conntr_01hcf9x766fqk8g7hz74363j9q',
                name = 'John's Gmail account',
                convore_mail = convore_api_client.models.create_convore_mail_channel_params.CreateConvoreMailChannelParams(
                    sender_name = 'John Smith', 
                    address = 'johnsmith@convoremail.com', ),
                ses = convore_api_client.models.create_ses_channel_params.CreateSesChannelParams(
                    sns_topic_arn = '', )
            )
        else:
            return CreateChannelRequest(
                connector_id = 'conntr_01hcf9x766fqk8g7hz74363j9q',
        )
        """

    def testCreateChannelRequest(self):
        """Test CreateChannelRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

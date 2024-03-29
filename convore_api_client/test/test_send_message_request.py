# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.send_message_request import SendMessageRequest

class TestSendMessageRequest(unittest.TestCase):
    """SendMessageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendMessageRequest:
        """Test SendMessageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendMessageRequest`
        """
        model = SendMessageRequest()
        if include_optional:
            return SendMessageRequest(
                channel_id = 'chnnl_01h2xcejqtf2nbrexx3vqjhp41',
                conversation_id = 'conv_01h2xcejqtf2nbrexx3vqjhp41',
                reply_to_message_id = 'msg_01h2xcejqtf2nbrexx3vqjhp41',
                reply_type = 'reply',
                var_from = '',
                to = [
                    ''
                    ],
                cc = [
                    ''
                    ],
                bcc = [
                    ''
                    ],
                sender = convore_api_client.models.message_participant.MessageParticipant(
                    name = 'John Doe', 
                    handle = convore_api_client.models.contact_handle.ContactHandle(
                        type = 'email', 
                        value = 'john@example.com', ), 
                    role = 'from', ),
                recipients = [
                    convore_api_client.models.message_participant.MessageParticipant(
                        name = 'John Doe', 
                        handle = convore_api_client.models.contact_handle.ContactHandle(
                            type = 'email', 
                            value = 'john@example.com', ), 
                        role = 'from', )
                    ],
                subject = 'Re: Issue with Verification Process',
                body = '...',
                quote_body = 'On Dec 15, 2023, at 6:54 PM, John Doe <john@example.com> wrote: ...'
            )
        else:
            return SendMessageRequest(
                body = '...',
        )
        """

    def testSendMessageRequest(self):
        """Test SendMessageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

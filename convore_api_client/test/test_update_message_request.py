# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.update_message_request import UpdateMessageRequest

class TestUpdateMessageRequest(unittest.TestCase):
    """UpdateMessageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateMessageRequest:
        """Test UpdateMessageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateMessageRequest`
        """
        model = UpdateMessageRequest()
        if include_optional:
            return UpdateMessageRequest(
                subject = 'Issue with Verification Process',
                direction = 'inbound',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
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
                body = '',
                snippet = ''
            )
        else:
            return UpdateMessageRequest(
        )
        """

    def testUpdateMessageRequest(self):
        """Test UpdateMessageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

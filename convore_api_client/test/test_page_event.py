# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.page_event import PageEvent

class TestPageEvent(unittest.TestCase):
    """PageEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageEvent:
        """Test PageEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageEvent`
        """
        model = PageEvent()
        if include_optional:
            return PageEvent(
                data = [
                    convore_api_client.models.event.Event(
                        id = 'event_01hggtpfewf0y91nde7cz02p0k', 
                        type = 'message_inbound_received', 
                        object_id = 'conv_01h2xcejqtf2nbrexx3vqjhp41', 
                        object_type = 'conversation', 
                        conversation_id = '', 
                        message_id = '', 
                        label_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_cursor = '',
                total_count = 56
            )
        else:
            return PageEvent(
                data = [
                    convore_api_client.models.event.Event(
                        id = 'event_01hggtpfewf0y91nde7cz02p0k', 
                        type = 'message_inbound_received', 
                        object_id = 'conv_01h2xcejqtf2nbrexx3vqjhp41', 
                        object_type = 'conversation', 
                        conversation_id = '', 
                        message_id = '', 
                        label_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testPageEvent(self):
        """Test PageEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

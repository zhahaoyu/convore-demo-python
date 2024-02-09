# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.api.messages_api import MessagesApi


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MessagesApi()

    def tearDown(self) -> None:
        pass

    def test_get_message(self) -> None:
        """Test case for get_message

        Retrieve a message
        """
        pass

    def test_import_message(self) -> None:
        """Test case for import_message

        Import a message without sending it
        """
        pass

    def test_list_messages(self) -> None:
        """Test case for list_messages

        List messages
        """
        pass

    def test_send_message(self) -> None:
        """Test case for send_message

        Send a message
        """
        pass

    def test_update_message(self) -> None:
        """Test case for update_message

        Update a message
        """
        pass


if __name__ == '__main__':
    unittest.main()

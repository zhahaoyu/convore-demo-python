# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.update_label_request import UpdateLabelRequest

class TestUpdateLabelRequest(unittest.TestCase):
    """UpdateLabelRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateLabelRequest:
        """Test UpdateLabelRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateLabelRequest`
        """
        model = UpdateLabelRequest()
        if include_optional:
            return UpdateLabelRequest(
                name = 'Technical support',
                description = 'Urgent and important',
                shared_label_id = ''
            )
        else:
            return UpdateLabelRequest(
        )
        """

    def testUpdateLabelRequest(self):
        """Test UpdateLabelRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from convore_api_client.models.update_convore_mail_channel_params import UpdateConvoreMailChannelParams

class TestUpdateConvoreMailChannelParams(unittest.TestCase):
    """UpdateConvoreMailChannelParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateConvoreMailChannelParams:
        """Test UpdateConvoreMailChannelParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateConvoreMailChannelParams`
        """
        model = UpdateConvoreMailChannelParams()
        if include_optional:
            return UpdateConvoreMailChannelParams(
                sender_name = ''
            )
        else:
            return UpdateConvoreMailChannelParams(
        )
        """

    def testUpdateConvoreMailChannelParams(self):
        """Test UpdateConvoreMailChannelParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# SesChannel

The specific ses channel information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sns_topic_arn** | **str** | The SNS topic for SES to publish incoming message events to | [optional] 
**subscription_arn** | **str** | The SNS subscription ARN that Convore uses to listen to the SNS topic | [optional] 
**inbound_webhook** | [**InboundWebhook**](InboundWebhook.md) |  | [optional] 

## Example

```python
from convore_api_client.models.ses_channel import SesChannel

# TODO update the JSON string below
json = "{}"
# create an instance of SesChannel from a JSON string
ses_channel_instance = SesChannel.from_json(json)
# print the JSON string representation of the object
print SesChannel.to_json()

# convert the object into a dict
ses_channel_dict = ses_channel_instance.to_dict()
# create an instance of SesChannel from a dict
ses_channel_form_dict = ses_channel.from_dict(ses_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateSesChannelParams

Configuration used to create a channel for SES

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sns_topic_arn** | **str** | The SNS topic for SES to publish incoming message events to. | [optional] 

## Example

```python
from convore_api_client.models.create_ses_channel_params import CreateSesChannelParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSesChannelParams from a JSON string
create_ses_channel_params_instance = CreateSesChannelParams.from_json(json)
# print the JSON string representation of the object
print CreateSesChannelParams.to_json()

# convert the object into a dict
create_ses_channel_params_dict = create_ses_channel_params_instance.to_dict()
# create an instance of CreateSesChannelParams from a dict
create_ses_channel_params_form_dict = create_ses_channel_params.from_dict(create_ses_channel_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



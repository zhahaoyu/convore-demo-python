# UpdateChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the channel | [optional] 
**status** | [**ChannelStatus**](ChannelStatus.md) |  | [optional] 
**convore_mail** | [**UpdateConvoreMailChannelParams**](UpdateConvoreMailChannelParams.md) |  | [optional] 

## Example

```python
from convore_api_client.models.update_channel_request import UpdateChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChannelRequest from a JSON string
update_channel_request_instance = UpdateChannelRequest.from_json(json)
# print the JSON string representation of the object
print UpdateChannelRequest.to_json()

# convert the object into a dict
update_channel_request_dict = update_channel_request_instance.to_dict()
# create an instance of UpdateChannelRequest from a dict
update_channel_request_form_dict = update_channel_request.from_dict(update_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



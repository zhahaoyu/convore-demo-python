# CreateChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** | Unique identifier for the channel&#39;s connector | 
**name** | **str** | Name of the channel. | [optional] 
**convore_mail** | [**CreateConvoreMailChannelParams**](CreateConvoreMailChannelParams.md) |  | [optional] 
**ses** | [**CreateSesChannelParams**](CreateSesChannelParams.md) |  | [optional] 

## Example

```python
from convore_api_client.models.create_channel_request import CreateChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChannelRequest from a JSON string
create_channel_request_instance = CreateChannelRequest.from_json(json)
# print the JSON string representation of the object
print CreateChannelRequest.to_json()

# convert the object into a dict
create_channel_request_dict = create_channel_request_instance.to_dict()
# create an instance of CreateChannelRequest from a dict
create_channel_request_form_dict = create_channel_request.from_dict(create_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



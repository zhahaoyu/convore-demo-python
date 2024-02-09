# Channel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the channel | 
**connector_id** | **str** | Unique identifier for the channel&#39;s connector | 
**provider** | [**ProviderType**](ProviderType.md) |  | 
**name** | **str** | Name of the channel | 
**addresses** | [**List[ChannelAddress]**](ChannelAddress.md) | A collection of communication addresses associated with the channel. These addresses are used for sending and receiving messages, ensuring proper routing and delivery of content. Each address specifies a unique handle, such as an email or a phone number, along with associated details like the participant&#39;s name and role. | 
**status** | [**ChannelStatus**](ChannelStatus.md) |  | 
**created_at** | **datetime** | The ISO 8601 time at which the Channel was created. | 
**convore_mail** | [**ConvoreMailChannel**](ConvoreMailChannel.md) |  | [optional] 
**ses** | [**SesChannel**](SesChannel.md) |  | [optional] 

## Example

```python
from convore_api_client.models.channel import Channel

# TODO update the JSON string below
json = "{}"
# create an instance of Channel from a JSON string
channel_instance = Channel.from_json(json)
# print the JSON string representation of the object
print Channel.to_json()

# convert the object into a dict
channel_dict = channel_instance.to_dict()
# create an instance of Channel from a dict
channel_form_dict = channel.from_dict(channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



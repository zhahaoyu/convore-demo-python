# ChannelAddress

A collection of communication addresses associated with the channel. These addresses are used for sending and receiving messages, ensuring proper routing and delivery of content. Each address specifies a unique handle, such as an email or a phone number, along with associated details like the participant's name and role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the sender. | [optional] 
**handle** | [**ContactHandle**](ContactHandle.md) |  | 
**is_primary** | **bool** | Whether the address is the primary address for the channel. | [optional] 

## Example

```python
from convore_api_client.models.channel_address import ChannelAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelAddress from a JSON string
channel_address_instance = ChannelAddress.from_json(json)
# print the JSON string representation of the object
print ChannelAddress.to_json()

# convert the object into a dict
channel_address_dict = channel_address_instance.to_dict()
# create an instance of ChannelAddress from a dict
channel_address_form_dict = channel_address.from_dict(channel_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



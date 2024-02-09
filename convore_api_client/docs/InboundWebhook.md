# InboundWebhook

The inbound webhook that this connector is associated with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | [**InboundWebhookStatus**](InboundWebhookStatus.md) |  | 
**url** | **str** |  | 

## Example

```python
from convore_api_client.models.inbound_webhook import InboundWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of InboundWebhook from a JSON string
inbound_webhook_instance = InboundWebhook.from_json(json)
# print the JSON string representation of the object
print InboundWebhook.to_json()

# convert the object into a dict
inbound_webhook_dict = inbound_webhook_instance.to_dict()
# create an instance of InboundWebhook from a dict
inbound_webhook_form_dict = inbound_webhook.from_dict(inbound_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



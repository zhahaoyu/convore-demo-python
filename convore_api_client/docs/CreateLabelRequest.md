# CreateLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the label. | 
**description** | **str** | Help with website or app functionality, technical glitches, and navigation. | [optional] 
**type** | [**LabelType**](LabelType.md) |  | [optional] 
**channel_id** | **str** | The identifier of the channel this label is associated with, required for CHANNEL_PRIVATE labels. This links the label to a specific communication channel. | [optional] 
**external_label_id** | **str** | Identifier of the label in an external system, required for CHANNEL_PRIVATE labels that map to external systems. | [optional] 
**shared_label_id** | **str** | An identifier used to associate a CHANNEL_PRIVATE label with a corresponding SHARED label within the organization, facilitating unified label management across different channels. | [optional] 

## Example

```python
from convore_api_client.models.create_label_request import CreateLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLabelRequest from a JSON string
create_label_request_instance = CreateLabelRequest.from_json(json)
# print the JSON string representation of the object
print CreateLabelRequest.to_json()

# convert the object into a dict
create_label_request_dict = create_label_request_instance.to_dict()
# create an instance of CreateLabelRequest from a dict
create_label_request_form_dict = create_label_request.from_dict(create_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



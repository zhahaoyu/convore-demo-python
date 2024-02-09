# Label


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the label. | 
**name** | **str** | The human-readable name of the label, used for easy identification. This name can be something descriptive related to the label&#39;s purpose, like &#39;Technical Support&#39; or &#39;Urgent&#39;. | 
**description** | **str** | An optional detailed description of the label, providing additional context about its purpose. | [optional] 
**created_at** | **datetime** | The ISO 8601 time at which the Label was created. | 
**type** | [**LabelType**](LabelType.md) |  | 
**channel_id** | **str** | The identifier of the channel this label is associated with, required for CHANNEL_PRIVATE labels. This links the label to a specific communication channel. | [optional] 
**external_label_id** | **str** | Identifier of the label in an external system, required for CHANNEL_PRIVATE labels that map to external systems. | [optional] 
**shared_label_id** | **str** | An identifier used to associate this CHANNEL_PRIVATE label with a corresponding SHARED label within the organization, facilitating unified label management across different channels. | [optional] 

## Example

```python
from convore_api_client.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print Label.to_json()

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_form_dict = label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



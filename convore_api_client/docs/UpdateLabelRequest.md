# UpdateLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the label. | [optional] 
**description** | **str** | Help with website or app functionality, technical glitches, and navigation. | [optional] 
**shared_label_id** | **str** | An identifier used to associate a CHANNEL_PRIVATE label with a corresponding SHARED label within the organization, facilitating unified label management across different channels. | [optional] 

## Example

```python
from convore_api_client.models.update_label_request import UpdateLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLabelRequest from a JSON string
update_label_request_instance = UpdateLabelRequest.from_json(json)
# print the JSON string representation of the object
print UpdateLabelRequest.to_json()

# convert the object into a dict
update_label_request_dict = update_label_request_instance.to_dict()
# create an instance of UpdateLabelRequest from a dict
update_label_request_form_dict = update_label_request.from_dict(update_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



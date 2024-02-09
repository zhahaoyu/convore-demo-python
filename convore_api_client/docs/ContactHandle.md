# ContactHandle

Handle of the contact. Can be any string used to uniquely identify the contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ContactHandleType**](ContactHandleType.md) |  | 
**value** | **str** | Handle used to reach the contact. | 

## Example

```python
from convore_api_client.models.contact_handle import ContactHandle

# TODO update the JSON string below
json = "{}"
# create an instance of ContactHandle from a JSON string
contact_handle_instance = ContactHandle.from_json(json)
# print the JSON string representation of the object
print ContactHandle.to_json()

# convert the object into a dict
contact_handle_dict = contact_handle_instance.to_dict()
# create an instance of ContactHandle from a dict
contact_handle_form_dict = contact_handle.from_dict(contact_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



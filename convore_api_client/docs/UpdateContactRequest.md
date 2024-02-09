# UpdateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Contact name. | [optional] 
**description** | **str** | Contact description. | [optional] 
**handles** | [**List[ContactHandle]**](ContactHandle.md) | List of the handles for this contact. | [optional] 

## Example

```python
from convore_api_client.models.update_contact_request import UpdateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactRequest from a JSON string
update_contact_request_instance = UpdateContactRequest.from_json(json)
# print the JSON string representation of the object
print UpdateContactRequest.to_json()

# convert the object into a dict
update_contact_request_dict = update_contact_request_instance.to_dict()
# create an instance of UpdateContactRequest from a dict
update_contact_request_form_dict = update_contact_request.from_dict(update_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



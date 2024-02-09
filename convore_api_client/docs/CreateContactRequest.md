# CreateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Contact name. | 
**description** | **str** | Contact description. | [optional] 
**handles** | [**List[ContactHandle]**](ContactHandle.md) | List of the handles for this contact. | 

## Example

```python
from convore_api_client.models.create_contact_request import CreateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactRequest from a JSON string
create_contact_request_instance = CreateContactRequest.from_json(json)
# print the JSON string representation of the object
print CreateContactRequest.to_json()

# convert the object into a dict
create_contact_request_dict = create_contact_request_instance.to_dict()
# create an instance of CreateContactRequest from a dict
create_contact_request_form_dict = create_contact_request.from_dict(create_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Contact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the contact. | 
**name** | **str** | Contact name. | 
**description** | **str** | Contact description. | [optional] 
**handles** | [**List[ContactHandle]**](ContactHandle.md) | List of the handles for this contact. | 
**created_at** | **datetime** | The ISO 8601 time at which the Contact was created. | 

## Example

```python
from convore_api_client.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print Contact.to_json()

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_form_dict = contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



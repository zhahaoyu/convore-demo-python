# PageContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Contact]**](Contact.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_contact import PageContact

# TODO update the JSON string below
json = "{}"
# create an instance of PageContact from a JSON string
page_contact_instance = PageContact.from_json(json)
# print the JSON string representation of the object
print PageContact.to_json()

# convert the object into a dict
page_contact_dict = page_contact_instance.to_dict()
# create an instance of PageContact from a dict
page_contact_form_dict = page_contact.from_dict(page_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



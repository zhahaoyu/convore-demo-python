# PageApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiKey]**](ApiKey.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_api_key import PageApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of PageApiKey from a JSON string
page_api_key_instance = PageApiKey.from_json(json)
# print the JSON string representation of the object
print PageApiKey.to_json()

# convert the object into a dict
page_api_key_dict = page_api_key_instance.to_dict()
# create an instance of PageApiKey from a dict
page_api_key_form_dict = page_api_key.from_dict(page_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PageMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Message]**](Message.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_message import PageMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PageMessage from a JSON string
page_message_instance = PageMessage.from_json(json)
# print the JSON string representation of the object
print PageMessage.to_json()

# convert the object into a dict
page_message_dict = page_message_instance.to_dict()
# create an instance of PageMessage from a dict
page_message_form_dict = page_message.from_dict(page_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



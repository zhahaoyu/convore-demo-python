# PageConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Conversation]**](Conversation.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_conversation import PageConversation

# TODO update the JSON string below
json = "{}"
# create an instance of PageConversation from a JSON string
page_conversation_instance = PageConversation.from_json(json)
# print the JSON string representation of the object
print PageConversation.to_json()

# convert the object into a dict
page_conversation_dict = page_conversation_instance.to_dict()
# create an instance of PageConversation from a dict
page_conversation_form_dict = page_conversation.from_dict(page_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



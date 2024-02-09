# UpdateConversationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConversationStatus**](ConversationStatus.md) |  | [optional] 
**priority** | [**ConversationPriority**](ConversationPriority.md) |  | [optional] 
**label_ids** | **List[str]** | List of labels for this conversation | [optional] 
**participants** | [**List[MessageParticipant]**](MessageParticipant.md) |  | [optional] 
**subject** | **str** | Subject of the conversation, if applicable. Null for non-email conversations. | [optional] 
**snippet** | **str** | A shortened plain-text preview of the message body. | [optional] 
**is_unread** | **bool** | Whether the conversation has been read. | [optional] 
**last_message_date** | **datetime** | ISO 8601 time of the most recent message. | [optional] 

## Example

```python
from convore_api_client.models.update_conversation_request import UpdateConversationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConversationRequest from a JSON string
update_conversation_request_instance = UpdateConversationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateConversationRequest.to_json()

# convert the object into a dict
update_conversation_request_dict = update_conversation_request_instance.to_dict()
# create an instance of UpdateConversationRequest from a dict
update_conversation_request_form_dict = update_conversation_request.from_dict(update_conversation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



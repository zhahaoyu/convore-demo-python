# CreateConversationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Identifier of the channel through which the conversation is taking place. | 
**status** | [**ConversationStatus**](ConversationStatus.md) |  | [optional] 
**priority** | [**ConversationPriority**](ConversationPriority.md) |  | [optional] 
**label_ids** | **List[str]** | List of labels for this conversation | 
**participants** | [**List[MessageParticipant]**](MessageParticipant.md) |  | 
**subject** | **str** | Subject of the conversation, if applicable. Null for non-email conversations. | [optional] 
**snippet** | **str** | A shortened plain-text preview of the message body. | [optional] 
**is_unread** | **bool** | Whether the conversation has been read. | [optional] 
**last_message_date** | **datetime** | ISO 8601 time of the most recent message. | [optional] 

## Example

```python
from convore_api_client.models.create_conversation_request import CreateConversationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConversationRequest from a JSON string
create_conversation_request_instance = CreateConversationRequest.from_json(json)
# print the JSON string representation of the object
print CreateConversationRequest.to_json()

# convert the object into a dict
create_conversation_request_dict = create_conversation_request_instance.to_dict()
# create an instance of CreateConversationRequest from a dict
create_conversation_request_form_dict = create_conversation_request.from_dict(create_conversation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



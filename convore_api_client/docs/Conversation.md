# Conversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the conversation. | 
**channel_id** | **str** | Identifier of the channel through which the conversation is taking place. | 
**status** | [**ConversationStatus**](ConversationStatus.md) |  | 
**priority** | [**ConversationPriority**](ConversationPriority.md) |  | 
**labels** | [**List[Label]**](Label.md) | List of labels for this conversation | 
**participants** | [**List[MessageParticipant]**](MessageParticipant.md) |  | 
**subject** | **str** | Subject of the conversation, if applicable. Null for non-email conversations. | [optional] 
**snippet** | **str** | A shortened plain-text preview of the message body. | [optional] 
**is_unread** | **bool** | Whether the conversation has been read. | [optional] 
**last_message_date** | **datetime** | ISO 8601 time of the most recent message. | [optional] 
**external_conversation_id** | **str** | The identifier of the conversation in an external system. | [optional] 
**message_count** | **int** | The number of messages in this conversation. | [optional] 
**draft_count** | **int** | The number of drafts in this conversation. | [optional] 
**attachment_count** | **int** | The number of attachments in this conversation. | [optional] 
**created_at** | **datetime** | The ISO 8601 time at which the Conversation was created. | 

## Example

```python
from convore_api_client.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print Conversation.to_json()

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_form_dict = conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



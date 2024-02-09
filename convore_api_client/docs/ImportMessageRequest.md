# ImportMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | Identifier of the conversation the message belongs to. Either conversationId or channelId must be provided. | [optional] 
**channel_id** | **str** | Identifier of the channel through which the conversation is taking place. Either conversationId or channelId must be provided. | [optional] 
**subject** | **str** | Subject of the email message, if applicable. Null for non-email conversations. | [optional] 
**direction** | [**MessageDirection**](MessageDirection.md) |  | [optional] 
**var_date** | **datetime** | ISO 8601 time of when the message was sent. | 
**sender** | [**MessageParticipant**](MessageParticipant.md) |  | 
**recipients** | [**List[MessageParticipant]**](MessageParticipant.md) |  | 
**body** | **str** |  | [optional] 
**snippet** | **str** |  | [optional] 
**reply_to_message_id** | **str** | The ID of the message that you&#39;re replying to. | [optional] 
**reply_type** | [**MessageReplyType**](MessageReplyType.md) |  | [optional] 

## Example

```python
from convore_api_client.models.import_message_request import ImportMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportMessageRequest from a JSON string
import_message_request_instance = ImportMessageRequest.from_json(json)
# print the JSON string representation of the object
print ImportMessageRequest.to_json()

# convert the object into a dict
import_message_request_dict = import_message_request_instance.to_dict()
# create an instance of ImportMessageRequest from a dict
import_message_request_form_dict = import_message_request.from_dict(import_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SendMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Identifier of the channel through which the conversation is taking place. Either channelId or replyToMessageId must be provided. | [optional] 
**conversation_id** | **str** | Identifier of the conversation the message belongs to. | [optional] 
**reply_to_message_id** | **str** | The ID of the message that you&#39;re replying to. Either channelId or replyToMessageId must be provided | [optional] 
**reply_type** | [**MessageReplyType**](MessageReplyType.md) |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**sender** | [**MessageParticipant**](MessageParticipant.md) |  | [optional] 
**recipients** | [**List[MessageParticipant]**](MessageParticipant.md) | The name/handle pairs of the recipients, including to, cc, and bcc. | [optional] 
**subject** | **str** | Subject of the email message, if applicable. Null for non-email conversations. | [optional] 
**body** | **str** | The full HTML body of the message. Messages with only plain-text representations are up-converted to HTML. | 
**quote_body** | **str** | Body for the quote that the message is referencing. Only available on email channels. | [optional] 

## Example

```python
from convore_api_client.models.send_message_request import SendMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequest from a JSON string
send_message_request_instance = SendMessageRequest.from_json(json)
# print the JSON string representation of the object
print SendMessageRequest.to_json()

# convert the object into a dict
send_message_request_dict = send_message_request_instance.to_dict()
# create an instance of SendMessageRequest from a dict
send_message_request_form_dict = send_message_request.from_dict(send_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



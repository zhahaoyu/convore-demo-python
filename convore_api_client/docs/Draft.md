# Draft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the draft. | 
**channel_id** | **str** | Identifier of the channel through which the conversation is taking place. | 
**conversation_id** | **str** | Identifier of the conversation the draft belongs to. | 
**message_id** | **str** | The ID of the message created by the draft. | [optional] 
**reply_to_message_id** | **str** | The ID of the message that you&#39;re replying to. | [optional] 
**reply_type** | [**MessageReplyType**](MessageReplyType.md) |  | [optional] 
**sender** | [**MessageParticipant**](MessageParticipant.md) |  | 
**recipients** | [**List[MessageParticipant]**](MessageParticipant.md) | The name/handle pairs of the recipients, including to, cc, and bcc. | 
**subject** | **str** | Subject of the email message, if applicable. Null for non-email conversations. | [optional] 
**raw_body** | **str** | The full HTML body of the message. Messages with only plain-text representations are up-converted to HTML. | [optional] 
**body** | **str** | The full HTML body of the message without quotations. | [optional] 
**quote_body** | **str** | Body for the quote that the message is referencing. Only available on email channels. | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | An array of Attachment objects. | 
**external_draft_id** | **str** | The identifier of the draft in an external system. | [optional] 
**created_at** | **datetime** | The ISO 8601 time at which the Draft was created. | 

## Example

```python
from convore_api_client.models.draft import Draft

# TODO update the JSON string below
json = "{}"
# create an instance of Draft from a JSON string
draft_instance = Draft.from_json(json)
# print the JSON string representation of the object
print Draft.to_json()

# convert the object into a dict
draft_dict = draft_instance.to_dict()
# create an instance of Draft from a dict
draft_form_dict = draft.from_dict(draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



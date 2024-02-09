# Attachment

An array of Attachment objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the attachment. | 
**conversation_id** | **str** | Conversation ID of the conversation the attachment belongs to.. | 
**draft_id** | **str** | Draft ID of the draft the attachment belongs to. Either this or message_id must be provided, but not both. | [optional] 
**message_id** | **str** | Message ID of the message the attachment belongs to. Either this or draft_id must be provided, but not both. | [optional] 
**content_type** | **str** | MIME type of the attachment (e.g., image/png, application/pdf). | 
**filename** | **str** | Original filename of the attachment. | 
**is_inline** | **bool** | Only applies to Email messages. Indicates if the attachment is displayed inline (using CID) within the message content or as a regular attachment. | 
**content_id** | **str** | Applicable to Email messages with inline attachments. Corresponds to the Content-ID (CID) of an inline image or other attachment displayed within the message content. For instance, an inline image might be referenced in the HTML message body as &lt;img src&#x3D;\&quot;cid:image01.png\&quot;&gt;. In this example, the &#39;contentId&#39; would be &#39;image01.png&#39;. | [optional] 
**size** | **int** | Size of the attachment in bytes. | 

## Example

```python
from convore_api_client.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print Attachment.to_json()

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_form_dict = attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



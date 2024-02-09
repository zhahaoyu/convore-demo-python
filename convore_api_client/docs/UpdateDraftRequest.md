# UpdateDraftRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Identifier of the channel through which the conversation is taking place. | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**subject** | **str** | Subject of the email message, if applicable. Null for non-email conversations. | [optional] 
**body** | **str** | The full HTML body of the message without quotations. | [optional] 
**raw_body** | **str** | The full HTML body of the message. Messages with only plain-text representations are up-converted to HTML. | [optional] 
**sender** | [**MessageParticipant**](MessageParticipant.md) |  | [optional] 
**recipients** | [**List[MessageParticipant]**](MessageParticipant.md) | The name/handle pairs of the recipients, including to, cc, and bcc. | [optional] 

## Example

```python
from convore_api_client.models.update_draft_request import UpdateDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDraftRequest from a JSON string
update_draft_request_instance = UpdateDraftRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDraftRequest.to_json()

# convert the object into a dict
update_draft_request_dict = update_draft_request_instance.to_dict()
# create an instance of UpdateDraftRequest from a dict
update_draft_request_form_dict = update_draft_request.from_dict(update_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



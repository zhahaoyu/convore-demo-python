# UpdateMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject of the email message, if applicable. Null for non-email conversations. | [optional] 
**direction** | [**MessageDirection**](MessageDirection.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**sender** | [**MessageParticipant**](MessageParticipant.md) |  | [optional] 
**recipients** | [**List[MessageParticipant]**](MessageParticipant.md) |  | [optional] 
**body** | **str** |  | [optional] 
**snippet** | **str** |  | [optional] 

## Example

```python
from convore_api_client.models.update_message_request import UpdateMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMessageRequest from a JSON string
update_message_request_instance = UpdateMessageRequest.from_json(json)
# print the JSON string representation of the object
print UpdateMessageRequest.to_json()

# convert the object into a dict
update_message_request_dict = update_message_request_instance.to_dict()
# create an instance of UpdateMessageRequest from a dict
update_message_request_form_dict = update_message_request.from_dict(update_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



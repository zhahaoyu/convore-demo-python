# MessageParticipant

The name/handle pairs of the recipients, including to, cc, and bcc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the participant. Used to create the contact if needed. | [optional] 
**handle** | [**ContactHandle**](ContactHandle.md) |  | 
**role** | [**MessageParticipantRole**](MessageParticipantRole.md) |  | 

## Example

```python
from convore_api_client.models.message_participant import MessageParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of MessageParticipant from a JSON string
message_participant_instance = MessageParticipant.from_json(json)
# print the JSON string representation of the object
print MessageParticipant.to_json()

# convert the object into a dict
message_participant_dict = message_participant_instance.to_dict()
# create an instance of MessageParticipant from a dict
message_participant_form_dict = message_participant.from_dict(message_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the event. | 
**type** | [**EventType**](EventType.md) |  | 
**object_id** | **str** | The ID of the object associated with the event. | 
**object_type** | [**ObjectType**](ObjectType.md) |  | 
**conversation_id** | **str** | The ID of the conversation associated with the event. | [optional] 
**message_id** | **str** | The ID of the message associated with the event. | [optional] 
**label_id** | **str** | The ID of the label associated with the event. | [optional] 
**created_at** | **datetime** | The ISO 8601 time at which the Event was created. | 

## Example

```python
from convore_api_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PageEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Event]**](Event.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_event import PageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PageEvent from a JSON string
page_event_instance = PageEvent.from_json(json)
# print the JSON string representation of the object
print PageEvent.to_json()

# convert the object into a dict
page_event_dict = page_event_instance.to_dict()
# create an instance of PageEvent from a dict
page_event_form_dict = page_event.from_dict(page_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



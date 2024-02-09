# PageChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Channel]**](Channel.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_channel import PageChannel

# TODO update the JSON string below
json = "{}"
# create an instance of PageChannel from a JSON string
page_channel_instance = PageChannel.from_json(json)
# print the JSON string representation of the object
print PageChannel.to_json()

# convert the object into a dict
page_channel_dict = page_channel_instance.to_dict()
# create an instance of PageChannel from a dict
page_channel_form_dict = page_channel.from_dict(page_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



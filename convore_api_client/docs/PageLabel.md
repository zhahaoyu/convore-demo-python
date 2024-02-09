# PageLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Label]**](Label.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_label import PageLabel

# TODO update the JSON string below
json = "{}"
# create an instance of PageLabel from a JSON string
page_label_instance = PageLabel.from_json(json)
# print the JSON string representation of the object
print PageLabel.to_json()

# convert the object into a dict
page_label_dict = page_label_instance.to_dict()
# create an instance of PageLabel from a dict
page_label_form_dict = page_label.from_dict(page_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



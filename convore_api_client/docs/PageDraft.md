# PageDraft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Draft]**](Draft.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_draft import PageDraft

# TODO update the JSON string below
json = "{}"
# create an instance of PageDraft from a JSON string
page_draft_instance = PageDraft.from_json(json)
# print the JSON string representation of the object
print PageDraft.to_json()

# convert the object into a dict
page_draft_dict = page_draft_instance.to_dict()
# create an instance of PageDraft from a dict
page_draft_form_dict = page_draft.from_dict(page_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



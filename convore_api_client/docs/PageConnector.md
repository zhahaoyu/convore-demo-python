# PageConnector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Connector]**](Connector.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total_count** | **int** | The total number of objects that match the query | [optional] 

## Example

```python
from convore_api_client.models.page_connector import PageConnector

# TODO update the JSON string below
json = "{}"
# create an instance of PageConnector from a JSON string
page_connector_instance = PageConnector.from_json(json)
# print the JSON string representation of the object
print PageConnector.to_json()

# convert the object into a dict
page_connector_dict = page_connector_instance.to_dict()
# create an instance of PageConnector from a dict
page_connector_form_dict = page_connector.from_dict(page_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



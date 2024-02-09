# Connector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the connector. | 
**provider** | [**ProviderType**](ProviderType.md) |  | 
**name** | **str** | Name of the connector | 
**gmail** | [**GmailConnector**](GmailConnector.md) |  | [optional] 
**ses** | [**SesConnector**](SesConnector.md) |  | [optional] 
**created_at** | **datetime** | The ISO 8601 time at which the Connector was created. | 

## Example

```python
from convore_api_client.models.connector import Connector

# TODO update the JSON string below
json = "{}"
# create an instance of Connector from a JSON string
connector_instance = Connector.from_json(json)
# print the JSON string representation of the object
print Connector.to_json()

# convert the object into a dict
connector_dict = connector_instance.to_dict()
# create an instance of Connector from a dict
connector_form_dict = connector.from_dict(connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



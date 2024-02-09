# UpdateConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connector | [optional] 
**gmail** | [**UpdateGmailConnectorParams**](UpdateGmailConnectorParams.md) |  | [optional] 
**ses** | [**UpdateSesConnectorParams**](UpdateSesConnectorParams.md) |  | [optional] 

## Example

```python
from convore_api_client.models.update_connector_request import UpdateConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConnectorRequest from a JSON string
update_connector_request_instance = UpdateConnectorRequest.from_json(json)
# print the JSON string representation of the object
print UpdateConnectorRequest.to_json()

# convert the object into a dict
update_connector_request_dict = update_connector_request_instance.to_dict()
# create an instance of UpdateConnectorRequest from a dict
update_connector_request_form_dict = update_connector_request.from_dict(update_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



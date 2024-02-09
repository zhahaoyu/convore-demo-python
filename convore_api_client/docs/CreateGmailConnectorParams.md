# CreateGmailConnectorParams

Gmail configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from convore_api_client.models.create_gmail_connector_params import CreateGmailConnectorParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGmailConnectorParams from a JSON string
create_gmail_connector_params_instance = CreateGmailConnectorParams.from_json(json)
# print the JSON string representation of the object
print CreateGmailConnectorParams.to_json()

# convert the object into a dict
create_gmail_connector_params_dict = create_gmail_connector_params_instance.to_dict()
# create an instance of CreateGmailConnectorParams from a dict
create_gmail_connector_params_form_dict = create_gmail_connector_params.from_dict(create_gmail_connector_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



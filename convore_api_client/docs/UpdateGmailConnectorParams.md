# UpdateGmailConnectorParams

Gmail configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from convore_api_client.models.update_gmail_connector_params import UpdateGmailConnectorParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGmailConnectorParams from a JSON string
update_gmail_connector_params_instance = UpdateGmailConnectorParams.from_json(json)
# print the JSON string representation of the object
print UpdateGmailConnectorParams.to_json()

# convert the object into a dict
update_gmail_connector_params_dict = update_gmail_connector_params_instance.to_dict()
# create an instance of UpdateGmailConnectorParams from a dict
update_gmail_connector_params_form_dict = update_gmail_connector_params.from_dict(update_gmail_connector_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



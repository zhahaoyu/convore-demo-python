# GmailConnector

Gmail configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 

## Example

```python
from convore_api_client.models.gmail_connector import GmailConnector

# TODO update the JSON string below
json = "{}"
# create an instance of GmailConnector from a JSON string
gmail_connector_instance = GmailConnector.from_json(json)
# print the JSON string representation of the object
print GmailConnector.to_json()

# convert the object into a dict
gmail_connector_dict = gmail_connector_instance.to_dict()
# create an instance of GmailConnector from a dict
gmail_connector_form_dict = gmail_connector.from_dict(gmail_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



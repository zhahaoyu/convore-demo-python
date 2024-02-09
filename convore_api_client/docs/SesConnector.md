# SesConnector

SES configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The AWS access key ID of the user used to access SES and subscribe to the SNS topic | 
**region** | **str** | The region of the S3 bucket and SES connection | 

## Example

```python
from convore_api_client.models.ses_connector import SesConnector

# TODO update the JSON string below
json = "{}"
# create an instance of SesConnector from a JSON string
ses_connector_instance = SesConnector.from_json(json)
# print the JSON string representation of the object
print SesConnector.to_json()

# convert the object into a dict
ses_connector_dict = ses_connector_instance.to_dict()
# create an instance of SesConnector from a dict
ses_connector_form_dict = ses_connector.from_dict(ses_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



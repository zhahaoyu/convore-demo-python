# CreateSesConnectorParams

SES configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The AWS access key ID of the user used to access SES and subscribe to the SNS topic | 
**secret_access_key** | **str** | The AWS secret access key of the user used to access SES and subscribe to the SNS topic | 
**region** | **str** | The region of the S3 bucket and SES connection | 

## Example

```python
from convore_api_client.models.create_ses_connector_params import CreateSesConnectorParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSesConnectorParams from a JSON string
create_ses_connector_params_instance = CreateSesConnectorParams.from_json(json)
# print the JSON string representation of the object
print CreateSesConnectorParams.to_json()

# convert the object into a dict
create_ses_connector_params_dict = create_ses_connector_params_instance.to_dict()
# create an instance of CreateSesConnectorParams from a dict
create_ses_connector_params_form_dict = create_ses_connector_params.from_dict(create_ses_connector_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



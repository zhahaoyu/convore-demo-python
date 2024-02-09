# UpdateSesConnectorParams

SES configuration. Only the non-null fields are set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The AWS access key ID of the user used to access SES and subscribe to the SNS topic | [optional] 
**secret_access_key** | **str** | The AWS secret access key of the user used to access SES and subscribe to the SNS topic | [optional] 
**region** | **str** | The region of the S3 bucket and SES connection | [optional] 

## Example

```python
from convore_api_client.models.update_ses_connector_params import UpdateSesConnectorParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSesConnectorParams from a JSON string
update_ses_connector_params_instance = UpdateSesConnectorParams.from_json(json)
# print the JSON string representation of the object
print UpdateSesConnectorParams.to_json()

# convert the object into a dict
update_ses_connector_params_dict = update_ses_connector_params_instance.to_dict()
# create an instance of UpdateSesConnectorParams from a dict
update_ses_connector_params_form_dict = update_ses_connector_params.from_dict(update_ses_connector_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



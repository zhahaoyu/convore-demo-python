# AuthorizationFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**connector_id** | **str** |  | 
**success_redirect_uri** | **str** |  | 
**error_redirect_uri** | **str** |  | 
**status** | [**AuthorizationFlowStatus**](AuthorizationFlowStatus.md) |  | 
**grant_url** | **str** |  | 
**connected_channel_id** | **str** |  | [optional] 

## Example

```python
from convore_api_client.models.authorization_flow import AuthorizationFlow

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationFlow from a JSON string
authorization_flow_instance = AuthorizationFlow.from_json(json)
# print the JSON string representation of the object
print AuthorizationFlow.to_json()

# convert the object into a dict
authorization_flow_dict = authorization_flow_instance.to_dict()
# create an instance of AuthorizationFlow from a dict
authorization_flow_form_dict = authorization_flow.from_dict(authorization_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



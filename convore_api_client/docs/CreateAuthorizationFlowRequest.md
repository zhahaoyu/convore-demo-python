# CreateAuthorizationFlowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | 
**success_redirect_uri** | **str** |  | 
**error_redirect_uri** | **str** |  | 

## Example

```python
from convore_api_client.models.create_authorization_flow_request import CreateAuthorizationFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthorizationFlowRequest from a JSON string
create_authorization_flow_request_instance = CreateAuthorizationFlowRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthorizationFlowRequest.to_json()

# convert the object into a dict
create_authorization_flow_request_dict = create_authorization_flow_request_instance.to_dict()
# create an instance of CreateAuthorizationFlowRequest from a dict
create_authorization_flow_request_form_dict = create_authorization_flow_request.from_dict(create_authorization_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



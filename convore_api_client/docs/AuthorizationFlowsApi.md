# convore_api_client.AuthorizationFlowsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authorization_flow**](AuthorizationFlowsApi.md#create_authorization_flow) | **POST** /v1/authorization_flows | Create an authorization flow. This is usually an OAuth2 authorization code flow where the user is redirected to the selected provider&#39;s authorization page and grants access to their account.


# **create_authorization_flow**
> AuthorizationFlow create_authorization_flow(create_authorization_flow_request)

Create an authorization flow. This is usually an OAuth2 authorization code flow where the user is redirected to the selected provider's authorization page and grants access to their account.

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.authorization_flow import AuthorizationFlow
from convore_api_client.models.create_authorization_flow_request import CreateAuthorizationFlowRequest
from convore_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = convore_api_client.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = convore_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with convore_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = convore_api_client.AuthorizationFlowsApi(api_client)
    create_authorization_flow_request = convore_api_client.CreateAuthorizationFlowRequest() # CreateAuthorizationFlowRequest | 

    try:
        # Create an authorization flow. This is usually an OAuth2 authorization code flow where the user is redirected to the selected provider's authorization page and grants access to their account.
        api_response = api_instance.create_authorization_flow(create_authorization_flow_request)
        print("The response of AuthorizationFlowsApi->create_authorization_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationFlowsApi->create_authorization_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_authorization_flow_request** | [**CreateAuthorizationFlowRequest**](CreateAuthorizationFlowRequest.md)|  | 

### Return type

[**AuthorizationFlow**](AuthorizationFlow.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization Flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


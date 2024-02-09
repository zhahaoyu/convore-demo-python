# convore_api_client.ConnectApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_authorization_code**](ConnectApi.md#handle_authorization_code) | **GET** /connect/callback | Handle a callback from an OAuth provider


# **handle_authorization_code**
> handle_authorization_code(code=code, state=state, error=error)

Handle a callback from an OAuth provider

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
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
    api_instance = convore_api_client.ConnectApi(api_client)
    code = 'code_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    error = 'error_example' # str |  (optional)

    try:
        # Handle a callback from an OAuth provider
        api_instance.handle_authorization_code(code=code, state=state, error=error)
    except Exception as e:
        print("Exception when calling ConnectApi->handle_authorization_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **error** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirects to the specified frontend success or error page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


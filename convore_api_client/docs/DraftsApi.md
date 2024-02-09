# convore_api_client.DraftsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_draft**](DraftsApi.md#create_draft) | **POST** /v1/drafts | Create a draft
[**delete_draft**](DraftsApi.md#delete_draft) | **DELETE** /v1/drafts/{draft_id} | Delete a draft
[**get_draft**](DraftsApi.md#get_draft) | **GET** /v1/drafts/{draft_id} | Retrieve a draft
[**list_drafts**](DraftsApi.md#list_drafts) | **GET** /v1/drafts | List drafts
[**send_draft**](DraftsApi.md#send_draft) | **POST** /v1/drafts/{draft_id}/send | Send a draft
[**update_draft**](DraftsApi.md#update_draft) | **PATCH** /v1/drafts/{draft_id} | Update a draft


# **create_draft**
> Draft create_draft(create_draft_request)

Create a draft

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.create_draft_request import CreateDraftRequest
from convore_api_client.models.draft import Draft
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
    api_instance = convore_api_client.DraftsApi(api_client)
    create_draft_request = convore_api_client.CreateDraftRequest() # CreateDraftRequest | 

    try:
        # Create a draft
        api_response = api_instance.create_draft(create_draft_request)
        print("The response of DraftsApi->create_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->create_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_draft_request** | [**CreateDraftRequest**](CreateDraftRequest.md)|  | 

### Return type

[**Draft**](Draft.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_draft**
> delete_draft(draft_id)

Delete a draft

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
    api_instance = convore_api_client.DraftsApi(api_client)
    draft_id = 'draft_id_example' # str | 

    try:
        # Delete a draft
        api_instance.delete_draft(draft_id)
    except Exception as e:
        print("Exception when calling DraftsApi->delete_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**|  | 

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
**200** | Draft |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft**
> Draft get_draft(draft_id)

Retrieve a draft

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.draft import Draft
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
    api_instance = convore_api_client.DraftsApi(api_client)
    draft_id = 'draft_id_example' # str | 

    try:
        # Retrieve a draft
        api_response = api_instance.get_draft(draft_id)
        print("The response of DraftsApi->get_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->get_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**|  | 

### Return type

[**Draft**](Draft.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drafts**
> PageDraft list_drafts(conversation_id=conversation_id, cursor=cursor, limit=limit)

List drafts

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.page_draft import PageDraft
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
    api_instance = convore_api_client.DraftsApi(api_client)
    conversation_id = 'conversation_id_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List drafts
        api_response = api_instance.list_drafts(conversation_id=conversation_id, cursor=cursor, limit=limit)
        print("The response of DraftsApi->list_drafts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->list_drafts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageDraft**](PageDraft.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_draft**
> Message send_draft(draft_id)

Send a draft

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.message import Message
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
    api_instance = convore_api_client.DraftsApi(api_client)
    draft_id = 'draft_id_example' # str | 

    try:
        # Send a draft
        api_response = api_instance.send_draft(draft_id)
        print("The response of DraftsApi->send_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->send_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**|  | 

### Return type

[**Message**](Message.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_draft**
> Draft update_draft(draft_id, update_draft_request)

Update a draft

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.draft import Draft
from convore_api_client.models.update_draft_request import UpdateDraftRequest
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
    api_instance = convore_api_client.DraftsApi(api_client)
    draft_id = 'draft_id_example' # str | 
    update_draft_request = convore_api_client.UpdateDraftRequest() # UpdateDraftRequest | 

    try:
        # Update a draft
        api_response = api_instance.update_draft(draft_id, update_draft_request)
        print("The response of DraftsApi->update_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->update_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**|  | 
 **update_draft_request** | [**UpdateDraftRequest**](UpdateDraftRequest.md)|  | 

### Return type

[**Draft**](Draft.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Draft |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# convore_api_client.LabelsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label**](LabelsApi.md#create_label) | **POST** /v1/labels | Create a label
[**delete_label**](LabelsApi.md#delete_label) | **DELETE** /v1/labels/{label_id} | Delete a label
[**get_label**](LabelsApi.md#get_label) | **GET** /v1/labels/{label_id} | Retrieve a label
[**list_labels**](LabelsApi.md#list_labels) | **GET** /v1/labels | List labels
[**update_label**](LabelsApi.md#update_label) | **PATCH** /v1/labels/{label_id} | Update a label


# **create_label**
> Label create_label(create_label_request)

Create a label

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.create_label_request import CreateLabelRequest
from convore_api_client.models.label import Label
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
    api_instance = convore_api_client.LabelsApi(api_client)
    create_label_request = convore_api_client.CreateLabelRequest() # CreateLabelRequest | 

    try:
        # Create a label
        api_response = api_instance.create_label(create_label_request)
        print("The response of LabelsApi->create_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->create_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_label_request** | [**CreateLabelRequest**](CreateLabelRequest.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label**
> delete_label(label_id)

Delete a label

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
    api_instance = convore_api_client.LabelsApi(api_client)
    label_id = 'label_id_example' # str | 

    try:
        # Delete a label
        api_instance.delete_label(label_id)
    except Exception as e:
        print("Exception when calling LabelsApi->delete_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**|  | 

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
**200** | Label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label**
> Label get_label(label_id)

Retrieve a label

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.label import Label
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
    api_instance = convore_api_client.LabelsApi(api_client)
    label_id = 'label_id_example' # str | 

    try:
        # Retrieve a label
        api_response = api_instance.get_label(label_id)
        print("The response of LabelsApi->get_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->get_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**|  | 

### Return type

[**Label**](Label.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_labels**
> PageLabel list_labels(channel_id=channel_id, channel_ids=channel_ids, type=type, cursor=cursor, limit=limit)

List labels

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.label_type import LabelType
from convore_api_client.models.page_label import PageLabel
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
    api_instance = convore_api_client.LabelsApi(api_client)
    channel_id = ['channel_id_example'] # List[str] |  (optional)
    channel_ids = ['channel_ids_example'] # List[str] |  (optional)
    type = convore_api_client.LabelType() # LabelType |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List labels
        api_response = api_instance.list_labels(channel_id=channel_id, channel_ids=channel_ids, type=type, cursor=cursor, limit=limit)
        print("The response of LabelsApi->list_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->list_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**List[str]**](str.md)|  | [optional] 
 **channel_ids** | [**List[str]**](str.md)|  | [optional] 
 **type** | [**LabelType**](.md)|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageLabel**](PageLabel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_label**
> Label update_label(label_id, update_label_request)

Update a label

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.label import Label
from convore_api_client.models.update_label_request import UpdateLabelRequest
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
    api_instance = convore_api_client.LabelsApi(api_client)
    label_id = 'label_id_example' # str | 
    update_label_request = convore_api_client.UpdateLabelRequest() # UpdateLabelRequest | 

    try:
        # Update a label
        api_response = api_instance.update_label(label_id, update_label_request)
        print("The response of LabelsApi->update_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->update_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**|  | 
 **update_label_request** | [**UpdateLabelRequest**](UpdateLabelRequest.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


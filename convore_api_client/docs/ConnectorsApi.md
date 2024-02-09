# convore_api_client.ConnectorsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector**](ConnectorsApi.md#create_connector) | **POST** /v1/connectors | Create a connector
[**get_connector**](ConnectorsApi.md#get_connector) | **GET** /v1/connectors/{connector_id} | Retrieve a connector
[**list_connectors**](ConnectorsApi.md#list_connectors) | **GET** /v1/connectors | List connectors
[**update_connector**](ConnectorsApi.md#update_connector) | **PATCH** /v1/connectors/{connector_id} | Update a connector


# **create_connector**
> Connector create_connector(create_connector_request)

Create a connector

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.connector import Connector
from convore_api_client.models.create_connector_request import CreateConnectorRequest
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
    api_instance = convore_api_client.ConnectorsApi(api_client)
    create_connector_request = convore_api_client.CreateConnectorRequest() # CreateConnectorRequest | 

    try:
        # Create a connector
        api_response = api_instance.create_connector(create_connector_request)
        print("The response of ConnectorsApi->create_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->create_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connector_request** | [**CreateConnectorRequest**](CreateConnectorRequest.md)|  | 

### Return type

[**Connector**](Connector.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> Connector get_connector(connector_id)

Retrieve a connector

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.connector import Connector
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
    api_instance = convore_api_client.ConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 

    try:
        # Retrieve a connector
        api_response = api_instance.get_connector(connector_id)
        print("The response of ConnectorsApi->get_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->get_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 

### Return type

[**Connector**](Connector.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> PageConnector list_connectors(cursor=cursor, limit=limit)

List connectors

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.page_connector import PageConnector
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
    api_instance = convore_api_client.ConnectorsApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List connectors
        api_response = api_instance.list_connectors(cursor=cursor, limit=limit)
        print("The response of ConnectorsApi->list_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->list_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageConnector**](PageConnector.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector**
> Connector update_connector(connector_id, update_connector_request)

Update a connector

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.connector import Connector
from convore_api_client.models.update_connector_request import UpdateConnectorRequest
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
    api_instance = convore_api_client.ConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 
    update_connector_request = convore_api_client.UpdateConnectorRequest() # UpdateConnectorRequest | 

    try:
        # Update a connector
        api_response = api_instance.update_connector(connector_id, update_connector_request)
        print("The response of ConnectorsApi->update_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->update_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **update_connector_request** | [**UpdateConnectorRequest**](UpdateConnectorRequest.md)|  | 

### Return type

[**Connector**](Connector.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


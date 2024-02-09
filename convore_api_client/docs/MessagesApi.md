# convore_api_client.MessagesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message**](MessagesApi.md#get_message) | **GET** /v1/messages/{message_id} | Retrieve a message
[**import_message**](MessagesApi.md#import_message) | **POST** /v1/messages/import | Import a message without sending it
[**list_messages**](MessagesApi.md#list_messages) | **GET** /v1/messages | List messages
[**send_message**](MessagesApi.md#send_message) | **POST** /v1/messages | Send a message
[**update_message**](MessagesApi.md#update_message) | **PATCH** /v1/messages/{message_id} | Update a message


# **get_message**
> Message get_message(message_id)

Retrieve a message

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
    api_instance = convore_api_client.MessagesApi(api_client)
    message_id = 'message_id_example' # str | 

    try:
        # Retrieve a message
        api_response = api_instance.get_message(message_id)
        print("The response of MessagesApi->get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

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
**200** | Message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_message**
> Message import_message(import_message_request)

Import a message without sending it

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.import_message_request import ImportMessageRequest
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
    api_instance = convore_api_client.MessagesApi(api_client)
    import_message_request = convore_api_client.ImportMessageRequest() # ImportMessageRequest | 

    try:
        # Import a message without sending it
        api_response = api_instance.import_message(import_message_request)
        print("The response of MessagesApi->import_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->import_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_message_request** | [**ImportMessageRequest**](ImportMessageRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> PageMessage list_messages(conversation_id=conversation_id, format=format, cursor=cursor, limit=limit)

List messages

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.message_format import MessageFormat
from convore_api_client.models.page_message import PageMessage
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
    api_instance = convore_api_client.MessagesApi(api_client)
    conversation_id = 'conversation_id_example' # str |  (optional)
    format = convore_api_client.MessageFormat() # MessageFormat |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List messages
        api_response = api_instance.list_messages(conversation_id=conversation_id, format=format, cursor=cursor, limit=limit)
        print("The response of MessagesApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | [optional] 
 **format** | [**MessageFormat**](.md)|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageMessage**](PageMessage.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> Message send_message(send_message_request)

Send a message

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.message import Message
from convore_api_client.models.send_message_request import SendMessageRequest
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
    api_instance = convore_api_client.MessagesApi(api_client)
    send_message_request = convore_api_client.SendMessageRequest() # SendMessageRequest | 

    try:
        # Send a message
        api_response = api_instance.send_message(send_message_request)
        print("The response of MessagesApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_request** | [**SendMessageRequest**](SendMessageRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message**
> Message update_message(message_id, update_message_request)

Update a message

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.message import Message
from convore_api_client.models.update_message_request import UpdateMessageRequest
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
    api_instance = convore_api_client.MessagesApi(api_client)
    message_id = 'message_id_example' # str | 
    update_message_request = convore_api_client.UpdateMessageRequest() # UpdateMessageRequest | 

    try:
        # Update a message
        api_response = api_instance.update_message(message_id, update_message_request)
        print("The response of MessagesApi->update_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->update_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 
 **update_message_request** | [**UpdateMessageRequest**](UpdateMessageRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


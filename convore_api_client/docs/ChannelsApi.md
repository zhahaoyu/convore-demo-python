# convore_api_client.ChannelsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel**](ChannelsApi.md#create_channel) | **POST** /v1/channels | Create a channel
[**get_channel**](ChannelsApi.md#get_channel) | **GET** /v1/channels/{channel_id} | Retrieve a channel
[**list_channels**](ChannelsApi.md#list_channels) | **GET** /v1/channels | List channels
[**update_channel**](ChannelsApi.md#update_channel) | **PATCH** /v1/channels/{channel_id} | Update a channel


# **create_channel**
> Channel create_channel(create_channel_request)

Create a channel

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.channel import Channel
from convore_api_client.models.create_channel_request import CreateChannelRequest
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
    api_instance = convore_api_client.ChannelsApi(api_client)
    create_channel_request = convore_api_client.CreateChannelRequest() # CreateChannelRequest | 

    try:
        # Create a channel
        api_response = api_instance.create_channel(create_channel_request)
        print("The response of ChannelsApi->create_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->create_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_channel_request** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | 

### Return type

[**Channel**](Channel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> Channel get_channel(channel_id)

Retrieve a channel

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.channel import Channel
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
    api_instance = convore_api_client.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        # Retrieve a channel
        api_response = api_instance.get_channel(channel_id)
        print("The response of ChannelsApi->get_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**Channel**](Channel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channels**
> PageChannel list_channels(cursor=cursor, limit=limit)

List channels

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.page_channel import PageChannel
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
    api_instance = convore_api_client.ChannelsApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List channels
        api_response = api_instance.list_channels(cursor=cursor, limit=limit)
        print("The response of ChannelsApi->list_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->list_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageChannel**](PageChannel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel**
> Channel update_channel(channel_id, update_channel_request)

Update a channel

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.channel import Channel
from convore_api_client.models.update_channel_request import UpdateChannelRequest
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
    api_instance = convore_api_client.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | 
    update_channel_request = convore_api_client.UpdateChannelRequest() # UpdateChannelRequest | 

    try:
        # Update a channel
        api_response = api_instance.update_channel(channel_id, update_channel_request)
        print("The response of ChannelsApi->update_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->update_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **update_channel_request** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | 

### Return type

[**Channel**](Channel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


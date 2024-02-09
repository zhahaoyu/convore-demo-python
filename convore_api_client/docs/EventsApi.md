# convore_api_client.EventsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /v1/events/{event_id} | Retrieve an event
[**list_events**](EventsApi.md#list_events) | **GET** /v1/events | List events


# **get_event**
> Event get_event(event_id)

Retrieve an event

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.event import Event
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
    api_instance = convore_api_client.EventsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Retrieve an event
        api_response = api_instance.get_event(event_id)
        print("The response of EventsApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**Event**](Event.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> PageEvent list_events(cursor=cursor, limit=limit, types=types, type=type, object_id=object_id, object_type=object_type, created_at_before=created_at_before, created_at_after=created_at_after)

List events

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.event_type import EventType
from convore_api_client.models.object_type import ObjectType
from convore_api_client.models.page_event import PageEvent
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
    api_instance = convore_api_client.EventsApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    types = [convore_api_client.EventType()] # List[EventType] |  (optional)
    type = convore_api_client.EventType() # EventType |  (optional)
    object_id = 'object_id_example' # str |  (optional)
    object_type = convore_api_client.ObjectType() # ObjectType |  (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # List events
        api_response = api_instance.list_events(cursor=cursor, limit=limit, types=types, type=type, object_id=object_id, object_type=object_type, created_at_before=created_at_before, created_at_after=created_at_after)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **types** | [**List[EventType]**](EventType.md)|  | [optional] 
 **type** | [**EventType**](.md)|  | [optional] 
 **object_id** | **str**|  | [optional] 
 **object_type** | [**ObjectType**](.md)|  | [optional] 
 **created_at_before** | **datetime**|  | [optional] 
 **created_at_after** | **datetime**|  | [optional] 

### Return type

[**PageEvent**](PageEvent.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


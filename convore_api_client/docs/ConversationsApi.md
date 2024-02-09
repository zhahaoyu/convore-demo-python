# convore_api_client.ConversationsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conversation**](ConversationsApi.md#create_conversation) | **POST** /v1/conversations | Create a conversation
[**get_conversation**](ConversationsApi.md#get_conversation) | **GET** /v1/conversations/{conversation_id} | Retrieve a conversation
[**list_conversations**](ConversationsApi.md#list_conversations) | **GET** /v1/conversations | List conversations
[**update_conversation**](ConversationsApi.md#update_conversation) | **PATCH** /v1/conversations/{conversation_id} | Update a conversation


# **create_conversation**
> Conversation create_conversation(create_conversation_request)

Create a conversation

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.conversation import Conversation
from convore_api_client.models.create_conversation_request import CreateConversationRequest
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
    api_instance = convore_api_client.ConversationsApi(api_client)
    create_conversation_request = convore_api_client.CreateConversationRequest() # CreateConversationRequest | 

    try:
        # Create a conversation
        api_response = api_instance.create_conversation(create_conversation_request)
        print("The response of ConversationsApi->create_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->create_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_conversation_request** | [**CreateConversationRequest**](CreateConversationRequest.md)|  | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> Conversation get_conversation(conversation_id)

Retrieve a conversation

Retrieves a conversation by its ID.

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.conversation import Conversation
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
    api_instance = convore_api_client.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | 

    try:
        # Retrieve a conversation
        api_response = api_instance.get_conversation(conversation_id)
        print("The response of ConversationsApi->get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversations**
> PageConversation list_conversations(channel_id=channel_id, status=status, statuses=statuses, label_ids=label_ids, has_no_label=has_no_label, contact_handle_tokens=contact_handle_tokens, has_drafts=has_drafts, has_messages=has_messages, has_outbound_messages=has_outbound_messages, created_at_before=created_at_before, created_at_after=created_at_after, last_message_date_before=last_message_date_before, last_message_date_after=last_message_date_after, cursor=cursor, limit=limit)

List conversations

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.conversation_status import ConversationStatus
from convore_api_client.models.page_conversation import PageConversation
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
    api_instance = convore_api_client.ConversationsApi(api_client)
    channel_id = 'channel_id_example' # str |  (optional)
    status = convore_api_client.ConversationStatus() # ConversationStatus |  (optional)
    statuses = [convore_api_client.ConversationStatus()] # List[ConversationStatus] |  (optional)
    label_ids = ['label_ids_example'] # List[str] |  (optional)
    has_no_label = True # bool |  (optional)
    contact_handle_tokens = ['contact_handle_tokens_example'] # List[str] |  (optional)
    has_drafts = True # bool |  (optional)
    has_messages = True # bool |  (optional)
    has_outbound_messages = True # bool |  (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    last_message_date_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    last_message_date_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List conversations
        api_response = api_instance.list_conversations(channel_id=channel_id, status=status, statuses=statuses, label_ids=label_ids, has_no_label=has_no_label, contact_handle_tokens=contact_handle_tokens, has_drafts=has_drafts, has_messages=has_messages, has_outbound_messages=has_outbound_messages, created_at_before=created_at_before, created_at_after=created_at_after, last_message_date_before=last_message_date_before, last_message_date_after=last_message_date_after, cursor=cursor, limit=limit)
        print("The response of ConversationsApi->list_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->list_conversations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | [optional] 
 **status** | [**ConversationStatus**](.md)|  | [optional] 
 **statuses** | [**List[ConversationStatus]**](ConversationStatus.md)|  | [optional] 
 **label_ids** | [**List[str]**](str.md)|  | [optional] 
 **has_no_label** | **bool**|  | [optional] 
 **contact_handle_tokens** | [**List[str]**](str.md)|  | [optional] 
 **has_drafts** | **bool**|  | [optional] 
 **has_messages** | **bool**|  | [optional] 
 **has_outbound_messages** | **bool**|  | [optional] 
 **created_at_before** | **datetime**|  | [optional] 
 **created_at_after** | **datetime**|  | [optional] 
 **last_message_date_before** | **datetime**|  | [optional] 
 **last_message_date_after** | **datetime**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageConversation**](PageConversation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversation page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conversation**
> Conversation update_conversation(conversation_id, update_conversation_request)

Update a conversation

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.conversation import Conversation
from convore_api_client.models.update_conversation_request import UpdateConversationRequest
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
    api_instance = convore_api_client.ConversationsApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    update_conversation_request = convore_api_client.UpdateConversationRequest() # UpdateConversationRequest | 

    try:
        # Update a conversation
        api_response = api_instance.update_conversation(conversation_id, update_conversation_request)
        print("The response of ConversationsApi->update_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->update_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **update_conversation_request** | [**UpdateConversationRequest**](UpdateConversationRequest.md)|  | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


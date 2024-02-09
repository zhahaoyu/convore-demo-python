# convore_api_client.ContactsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /v1/contacts | Create a contact
[**get_contact**](ContactsApi.md#get_contact) | **GET** /v1/contacts/{contact_id} | Retrieve a contact
[**list_contacts**](ContactsApi.md#list_contacts) | **GET** /v1/contacts | List contacts
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /v1/contacts/{contact_id} | Update a contact


# **create_contact**
> Contact create_contact(create_contact_request)

Create a contact

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.contact import Contact
from convore_api_client.models.create_contact_request import CreateContactRequest
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
    api_instance = convore_api_client.ContactsApi(api_client)
    create_contact_request = convore_api_client.CreateContactRequest() # CreateContactRequest | 

    try:
        # Create a contact
        api_response = api_instance.create_contact(create_contact_request)
        print("The response of ContactsApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_request** | [**CreateContactRequest**](CreateContactRequest.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contact get_contact(contact_id)

Retrieve a contact

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.contact import Contact
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
    api_instance = convore_api_client.ContactsApi(api_client)
    contact_id = 'contact_id_example' # str | 

    try:
        # Retrieve a contact
        api_response = api_instance.get_contact(contact_id)
        print("The response of ContactsApi->get_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> PageContact list_contacts(keyword=keyword, contact_handle_token=contact_handle_token, cursor=cursor, limit=limit)

List contacts

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.page_contact import PageContact
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
    api_instance = convore_api_client.ContactsApi(api_client)
    keyword = 'keyword_example' # str |  (optional)
    contact_handle_token = ['contact_handle_token_example'] # List[str] |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List contacts
        api_response = api_instance.list_contacts(keyword=keyword, contact_handle_token=contact_handle_token, cursor=cursor, limit=limit)
        print("The response of ContactsApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->list_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  | [optional] 
 **contact_handle_token** | [**List[str]**](str.md)|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PageContact**](PageContact.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contact update_contact(contact_id, update_contact_request)

Update a contact

### Example

* Bearer Authentication (ApiKey):

```python
import convore_api_client
from convore_api_client.models.contact import Contact
from convore_api_client.models.update_contact_request import UpdateContactRequest
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
    api_instance = convore_api_client.ContactsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    update_contact_request = convore_api_client.UpdateContactRequest() # UpdateContactRequest | 

    try:
        # Update a contact
        api_response = api_instance.update_contact(contact_id, update_contact_request)
        print("The response of ContactsApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **update_contact_request** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


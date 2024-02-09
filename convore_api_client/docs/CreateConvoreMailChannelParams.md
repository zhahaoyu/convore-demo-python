# CreateConvoreMailChannelParams

Configuration used to create a channel for convore mail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_name** | **str** | The default name of the sender. Can be overriden on a per-message basis. | 
**address** | **str** | It should consist only of lowercase alphanumeric characters (a-z, 0-9), include at least 5 digits, and end with &#39;@convoremail.com&#39; or &#39;@convoreapplication.com&#39;. Additionally, aliases are supported by appending &#39;+alias&#39; to the local part of the email address. For instance, &#39;foobar@convoremail.com&#39; can have an alias like &#39;foobar+1@convoremail.com&#39;. Emails sent to an alias are routed to the primary mailbox. | 

## Example

```python
from convore_api_client.models.create_convore_mail_channel_params import CreateConvoreMailChannelParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConvoreMailChannelParams from a JSON string
create_convore_mail_channel_params_instance = CreateConvoreMailChannelParams.from_json(json)
# print the JSON string representation of the object
print CreateConvoreMailChannelParams.to_json()

# convert the object into a dict
create_convore_mail_channel_params_dict = create_convore_mail_channel_params_instance.to_dict()
# create an instance of CreateConvoreMailChannelParams from a dict
create_convore_mail_channel_params_form_dict = create_convore_mail_channel_params.from_dict(create_convore_mail_channel_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



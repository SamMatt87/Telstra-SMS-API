# swagger_client.SMSApi

All URIs are relative to *https://sapi.telstra.com/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_sms_incoming**](SMSApi.md#messages_sms_incoming) | **GET** /messages/sms | Retrieve the unread incoming SMS messages
[**messages_sms_send**](SMSApi.md#messages_sms_send) | **POST** /messages/sms | Send an SMS to a Australian or International mobile phone.
[**messages_sms_status**](SMSApi.md#messages_sms_status) | **GET** /messages/sms/{messageId}/status | Retrieve the status of a single outgoing SMS message.


# **messages_sms_incoming**
> list[InlineResponse200] messages_sms_incoming(authorization)

Retrieve the unread incoming SMS messages

Returns a list of unread incoming SMS messages that were sent to the mobile phone nubmer registered with the developer's application.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSApi()
authorization = 'authorization_example' # str | Authorization header in the format 'Bearer {access_token}' - get the token by using the OAuth API with the scope 'SMS'

try: 
    # Retrieve the unread incoming SMS messages
    api_response = api_instance.messages_sms_incoming(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->messages_sms_incoming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header in the format &#39;Bearer {access_token}&#39; - get the token by using the OAuth API with the scope &#39;SMS&#39; | 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_sms_send**
> InlineResponse201 messages_sms_send(authorization, payload)

Send an SMS to a Australian or International mobile phone.

Sends a SMS to a single Australian or International mobile phone number. A unique identifier (messageId) returned in the response, which may be used to query for the delivery status of the message. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSApi()
authorization = 'authorization_example' # str | A header in the format 'Bearer {access_token}' - get the token by using the OAuth API with the scope 'SMS'
payload = swagger_client.Payload() # Payload | A JSON or XML payload containing the recipient's phone number and text message. The recipient number should be in the format '04xxxxxxxx' where x is a digit

try: 
    # Send an SMS to a Australian or International mobile phone.
    api_response = api_instance.messages_sms_send(authorization, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->messages_sms_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A header in the format &#39;Bearer {access_token}&#39; - get the token by using the OAuth API with the scope &#39;SMS&#39; | 
 **payload** | [**Payload**](Payload.md)| A JSON or XML payload containing the recipient&#39;s phone number and text message. The recipient number should be in the format &#39;04xxxxxxxx&#39; where x is a digit | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_sms_status**
> InlineResponse2001 messages_sms_status(authorization, message_id)

Retrieve the status of a single outgoing SMS message.

Retrieve the status of a message by using the 'messageId' that returned as returned in the response from the Send SMS method to get the status. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSApi()
authorization = 'authorization_example' # str | Authorization header in the format 'Bearer {access_token}' - get the token by using the OAuth API with the scope 'SMS'
message_id = 'message_id_example' # str | Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms

try: 
    # Retrieve the status of a single outgoing SMS message.
    api_response = api_instance.messages_sms_status(authorization, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->messages_sms_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header in the format &#39;Bearer {access_token}&#39; - get the token by using the OAuth API with the scope &#39;SMS&#39; | 
 **message_id** | **str**| Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


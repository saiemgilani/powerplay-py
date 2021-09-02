# powerplay.ConferencesApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conference**](ConferencesApi.md#get_conference) | **GET** /conferences/{id} | Get an NHL conference.
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /conferences | Get all current NHL conferences.

# **get_conference**
> Division get_conference(id)

Get an NHL conference.

You can use this to also retrieve inactive conferences. For example, the ID for the World Cup of Hockey is `7`.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.ConferencesApi()
id = 1.2 # float | The ID of the conference.

try:
    # Get an NHL conference.
    api_response = api_instance.get_conference(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConferencesApi->get_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the conference. | 

### Return type

[**Division**](Division.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conferences**
> Conferences get_conferences()

Get all current NHL conferences.

This only retrieves active conferences. For inactive conferences, use `/conferences/{id}`.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.ConferencesApi()

try:
    # Get all current NHL conferences.
    api_response = api_instance.get_conferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Conferences**](Conferences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


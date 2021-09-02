# powerplay.StatsApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stat_types**](StatsApi.md#get_stat_types) | **GET** /statTypes | Get all available NHL statistic types.

# **get_stat_types**
> StatTypes get_stat_types()

Get all available NHL statistic types.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.StatsApi()

try:
    # Get all available NHL statistic types.
    api_response = api_instance.get_stat_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stat_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatTypes**](StatTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


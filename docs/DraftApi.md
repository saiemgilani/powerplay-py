# powerplay.DraftApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft**](DraftApi.md#get_draft) | **GET** /draft | Get round-by-round data for current year&#x27;s NHL Entry Draft.
[**get_draft_by_year**](DraftApi.md#get_draft_by_year) | **GET** /draft/{year} | Get round-by-round data for a specific year&#x27;s NHL Entry Draft.
[**get_draft_prospect**](DraftApi.md#get_draft_prospect) | **GET** /draft/prospects/{id} | Get an NHL Entry Draft prospect.
[**get_draft_prospects**](DraftApi.md#get_draft_prospects) | **GET** /draft/prospects | Get all NHL Entry Draft prospects.

# **get_draft**
> Draft get_draft()

Get round-by-round data for current year's NHL Entry Draft.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.DraftApi()

try:
    # Get round-by-round data for current year's NHL Entry Draft.
    api_response = api_instance.get_draft()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_draft: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Draft**](Draft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_by_year**
> Draft get_draft_by_year(year)

Get round-by-round data for a specific year's NHL Entry Draft.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.DraftApi()
year = 1.2 # float | The draft year.

try:
    # Get round-by-round data for a specific year's NHL Entry Draft.
    api_response = api_instance.get_draft_by_year(year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_draft_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**| The draft year. | 

### Return type

[**Draft**](Draft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_prospect**
> DraftProspects get_draft_prospect(id)

Get an NHL Entry Draft prospect.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.DraftApi()
id = 1.2 # float | The prospect ID.

try:
    # Get an NHL Entry Draft prospect.
    api_response = api_instance.get_draft_prospect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_draft_prospect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The prospect ID. | 

### Return type

[**DraftProspects**](DraftProspects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_prospects**
> DraftProspects get_draft_prospects()

Get all NHL Entry Draft prospects.

Be forewarned that this endpoint returns a **lot** of data and there does not appear to be a way to paginate results.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.DraftApi()

try:
    # Get all NHL Entry Draft prospects.
    api_response = api_instance.get_draft_prospects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_draft_prospects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DraftProspects**](DraftProspects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


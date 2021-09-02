# powerplay.StandingsApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_standing_types**](StandingsApi.md#get_standing_types) | **GET** /standingsTypes | Get all available NHL standing types.
[**get_standings**](StandingsApi.md#get_standings) | **GET** /standings | Get NHL division standings.
[**get_standings_by_type**](StandingsApi.md#get_standings_by_type) | **GET** /standings/{type} | Get NHL standings for a specific standing type.

# **get_standing_types**
> StandingTypes get_standing_types()

Get all available NHL standing types.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.StandingsApi()

try:
    # Get all available NHL standing types.
    api_response = api_instance.get_standing_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandingsApi->get_standing_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StandingTypes**](StandingTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standings**
> Standings get_standings(season=season, _date=_date)

Get NHL division standings.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.StandingsApi()
season = '2013-10-20' # date | Standings for a specified season. (optional)
_date = '2013-10-20' # date | Standings on a specified date. (optional)

try:
    # Get NHL division standings.
    api_response = api_instance.get_standings(season=season, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandingsApi->get_standings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **date**| Standings for a specified season. | [optional] 
 **_date** | **date**| Standings on a specified date. | [optional] 

### Return type

[**Standings**](Standings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standings_by_type**
> Standings get_standings_by_type(type)

Get NHL standings for a specific standing type.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.StandingsApi()
type = 'type_example' # str | Standing types:   * `byConference` - Standings by Conference   * `byDivision` - Standings by Division   * `byLeague` - Standings by League   * `divisionLeaders` - Division Leader standings   * `postseason` - Postseason Standings   * `preseason` - Preseason Standings   * `regularSeason` - Regular Season Standings   * `wildCard` - Wild card standings   * `wildCardWithLeaders` - Wild card standings with Division Leaders 

try:
    # Get NHL standings for a specific standing type.
    api_response = api_instance.get_standings_by_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandingsApi->get_standings_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Standing types:   * &#x60;byConference&#x60; - Standings by Conference   * &#x60;byDivision&#x60; - Standings by Division   * &#x60;byLeague&#x60; - Standings by League   * &#x60;divisionLeaders&#x60; - Division Leader standings   * &#x60;postseason&#x60; - Postseason Standings   * &#x60;preseason&#x60; - Preseason Standings   * &#x60;regularSeason&#x60; - Regular Season Standings   * &#x60;wildCard&#x60; - Wild card standings   * &#x60;wildCardWithLeaders&#x60; - Wild card standings with Division Leaders  | 

### Return type

[**Standings**](Standings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


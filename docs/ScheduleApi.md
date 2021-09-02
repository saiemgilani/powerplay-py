# powerplay.ScheduleApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule**](ScheduleApi.md#get_schedule) | **GET** /schedule | Get the NHL game schedule.

# **get_schedule**
> Schedule get_schedule(expand=expand, team_id=team_id, start_date=start_date, end_date=end_date)

Get the NHL game schedule.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.ScheduleApi()
expand = 'expand_example' # str | Expand explanations:   * `schedule.brodcasts` - Shows the broadcasts of the game.   * `schedule.linescore` - Linescore for completed games.   * `schedule.ticket` - Provides the different places to buy tickets for the upcoming games.   * `team.schedule.previous` - Same as above but for the last game played.  (optional)
team_id = 'team_id_example' # str | Limit results to a specific team. Team ids can be found through the teams endpoint (optional)
start_date = '2013-10-20' # date | Start date for the search. (optional)
end_date = '2013-10-20' # date | End date for the search. (optional)

try:
    # Get the NHL game schedule.
    api_response = api_instance.get_schedule(expand=expand, team_id=team_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->get_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand explanations:   * &#x60;schedule.brodcasts&#x60; - Shows the broadcasts of the game.   * &#x60;schedule.linescore&#x60; - Linescore for completed games.   * &#x60;schedule.ticket&#x60; - Provides the different places to buy tickets for the upcoming games.   * &#x60;team.schedule.previous&#x60; - Same as above but for the last game played.  | [optional] 
 **team_id** | **str**| Limit results to a specific team. Team ids can be found through the teams endpoint | [optional] 
 **start_date** | **date**| Start date for the search. | [optional] 
 **end_date** | **date**| End date for the search. | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


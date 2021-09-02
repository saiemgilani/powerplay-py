# powerplay.PlayersApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /people/{id} | Get an NHL player.
[**get_player_stats**](PlayersApi.md#get_player_stats) | **GET** /people/{id}/stats | Get specific statistics for an NHL player.

# **get_player**
> Players get_player(id)

Get an NHL player.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.PlayersApi()
id = 1.2 # float | The ID of the player.

try:
    # Get an NHL player.
    api_response = api_instance.get_player(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the player. | 

### Return type

[**Players**](Players.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_stats**
> PlayerStats get_player_stats(id, stats, season=season)

Get specific statistics for an NHL player.

### Example
```python
from __future__ import print_function
import time
import powerplay
from powerplay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = powerplay.PlayersApi()
id = 1.2 # float | The ID of the player.
stats = 'stats_example' # str | Stats explanations:   * `homeAndAway` - Provides a split between home and away games.   * `byMonth` - Monthly split of stats.   * `byDayOfWeek` - Split done by day of the week.   * `goalsByGameSituation` - Shows number on when goals for a player happened like how many in the shootout, how many in each period, etc.   * `onPaceRegularSeason` - This only works with the current in-progress season and shows projected totals based on current onPaceRegularSeason.   * `regularSeasonStatRankings` - Returns where someone stands vs the rest of the league for a specific regularSeasonStatRankings   * `statsSingleSeason` - Obtains single season statistics for a player.   * `vsConference` - Conference stats split.   * `vsDivision` - Division stats split.   * `vsTeam` - Conference stats split.   * `winLoss` - Very similar to the previous modifier except it provides the W/L/OT split instead of Home and Away. 
season = 1.2 # float | Return a team's specific season. (optional)

try:
    # Get specific statistics for an NHL player.
    api_response = api_instance.get_player_stats(id, stats, season=season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the player. | 
 **stats** | **str**| Stats explanations:   * &#x60;homeAndAway&#x60; - Provides a split between home and away games.   * &#x60;byMonth&#x60; - Monthly split of stats.   * &#x60;byDayOfWeek&#x60; - Split done by day of the week.   * &#x60;goalsByGameSituation&#x60; - Shows number on when goals for a player happened like how many in the shootout, how many in each period, etc.   * &#x60;onPaceRegularSeason&#x60; - This only works with the current in-progress season and shows projected totals based on current onPaceRegularSeason.   * &#x60;regularSeasonStatRankings&#x60; - Returns where someone stands vs the rest of the league for a specific regularSeasonStatRankings   * &#x60;statsSingleSeason&#x60; - Obtains single season statistics for a player.   * &#x60;vsConference&#x60; - Conference stats split.   * &#x60;vsDivision&#x60; - Division stats split.   * &#x60;vsTeam&#x60; - Conference stats split.   * &#x60;winLoss&#x60; - Very similar to the previous modifier except it provides the W/L/OT split instead of Home and Away.  | 
 **season** | **float**| Return a team&#x27;s specific season. | [optional] 

### Return type

[**PlayerStats**](PlayerStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


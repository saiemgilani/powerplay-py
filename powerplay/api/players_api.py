# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from powerplay.api_client import ApiClient


class PlayersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_player(self, id, **kwargs):  # noqa: E501
        """Get an NHL player.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float id: The ID of the player. (required)
        :return: Players
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_player_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get an NHL player.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float id: The ID of the player. (required)
        :return: Players
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_player`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/people/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Players',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_stats(self, id, stats, **kwargs):  # noqa: E501
        """Get specific statistics for an NHL player.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_stats(id, stats, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float id: The ID of the player. (required)
        :param str stats: Stats explanations:   * `homeAndAway` - Provides a split between home and away games.   * `byMonth` - Monthly split of stats.   * `byDayOfWeek` - Split done by day of the week.   * `goalsByGameSituation` - Shows number on when goals for a player happened like how many in the shootout, how many in each period, etc.   * `onPaceRegularSeason` - This only works with the current in-progress season and shows projected totals based on current onPaceRegularSeason.   * `regularSeasonStatRankings` - Returns where someone stands vs the rest of the league for a specific regularSeasonStatRankings   * `statsSingleSeason` - Obtains single season statistics for a player.   * `vsConference` - Conference stats split.   * `vsDivision` - Division stats split.   * `vsTeam` - Conference stats split.   * `winLoss` - Very similar to the previous modifier except it provides the W/L/OT split instead of Home and Away.  (required)
        :param float season: Return a team's specific season.
        :return: PlayerStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_stats_with_http_info(id, stats, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_stats_with_http_info(id, stats, **kwargs)  # noqa: E501
            return data

    def get_player_stats_with_http_info(self, id, stats, **kwargs):  # noqa: E501
        """Get specific statistics for an NHL player.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_stats_with_http_info(id, stats, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float id: The ID of the player. (required)
        :param str stats: Stats explanations:   * `homeAndAway` - Provides a split between home and away games.   * `byMonth` - Monthly split of stats.   * `byDayOfWeek` - Split done by day of the week.   * `goalsByGameSituation` - Shows number on when goals for a player happened like how many in the shootout, how many in each period, etc.   * `onPaceRegularSeason` - This only works with the current in-progress season and shows projected totals based on current onPaceRegularSeason.   * `regularSeasonStatRankings` - Returns where someone stands vs the rest of the league for a specific regularSeasonStatRankings   * `statsSingleSeason` - Obtains single season statistics for a player.   * `vsConference` - Conference stats split.   * `vsDivision` - Division stats split.   * `vsTeam` - Conference stats split.   * `winLoss` - Very similar to the previous modifier except it provides the W/L/OT split instead of Home and Away.  (required)
        :param float season: Return a team's specific season.
        :return: PlayerStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'stats', 'season']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_player_stats`")  # noqa: E501
        # verify the required parameter 'stats' is set
        if ('stats' not in params or
                params['stats'] is None):
            raise ValueError("Missing the required parameter `stats` when calling `get_player_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'stats' in params:
            query_params.append(('stats', params['stats']))  # noqa: E501
        if 'season' in params:
            query_params.append(('season', params['season']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/people/{id}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

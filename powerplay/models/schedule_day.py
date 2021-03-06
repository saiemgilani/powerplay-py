# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ScheduleDay(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_date': 'date',
        'total_items': 'float',
        'total_events': 'float',
        'total_games': 'float',
        'total_matches': 'float',
        'games': 'list[ScheduleGame]',
        'events': 'list[object]',
        'matches': 'list[object]'
    }

    attribute_map = {
        '_date': 'date',
        'total_items': 'totalItems',
        'total_events': 'totalEvents',
        'total_games': 'totalGames',
        'total_matches': 'totalMatches',
        'games': 'games',
        'events': 'events',
        'matches': 'matches'
    }

    def __init__(self, _date=None, total_items=None, total_events=None, total_games=None, total_matches=None, games=None, events=None, matches=None):  # noqa: E501
        """ScheduleDay - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._total_items = None
        self._total_events = None
        self._total_games = None
        self._total_matches = None
        self._games = None
        self._events = None
        self._matches = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if total_items is not None:
            self.total_items = total_items
        if total_events is not None:
            self.total_events = total_events
        if total_games is not None:
            self.total_games = total_games
        if total_matches is not None:
            self.total_matches = total_matches
        if games is not None:
            self.games = games
        if events is not None:
            self.events = events
        if matches is not None:
            self.matches = matches

    @property
    def _date(self):
        """Gets the _date of this ScheduleDay.  # noqa: E501


        :return: The _date of this ScheduleDay.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ScheduleDay.


        :param _date: The _date of this ScheduleDay.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def total_items(self):
        """Gets the total_items of this ScheduleDay.  # noqa: E501


        :return: The total_items of this ScheduleDay.  # noqa: E501
        :rtype: float
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this ScheduleDay.


        :param total_items: The total_items of this ScheduleDay.  # noqa: E501
        :type: float
        """

        self._total_items = total_items

    @property
    def total_events(self):
        """Gets the total_events of this ScheduleDay.  # noqa: E501


        :return: The total_events of this ScheduleDay.  # noqa: E501
        :rtype: float
        """
        return self._total_events

    @total_events.setter
    def total_events(self, total_events):
        """Sets the total_events of this ScheduleDay.


        :param total_events: The total_events of this ScheduleDay.  # noqa: E501
        :type: float
        """

        self._total_events = total_events

    @property
    def total_games(self):
        """Gets the total_games of this ScheduleDay.  # noqa: E501


        :return: The total_games of this ScheduleDay.  # noqa: E501
        :rtype: float
        """
        return self._total_games

    @total_games.setter
    def total_games(self, total_games):
        """Sets the total_games of this ScheduleDay.


        :param total_games: The total_games of this ScheduleDay.  # noqa: E501
        :type: float
        """

        self._total_games = total_games

    @property
    def total_matches(self):
        """Gets the total_matches of this ScheduleDay.  # noqa: E501


        :return: The total_matches of this ScheduleDay.  # noqa: E501
        :rtype: float
        """
        return self._total_matches

    @total_matches.setter
    def total_matches(self, total_matches):
        """Sets the total_matches of this ScheduleDay.


        :param total_matches: The total_matches of this ScheduleDay.  # noqa: E501
        :type: float
        """

        self._total_matches = total_matches

    @property
    def games(self):
        """Gets the games of this ScheduleDay.  # noqa: E501


        :return: The games of this ScheduleDay.  # noqa: E501
        :rtype: list[ScheduleGame]
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this ScheduleDay.


        :param games: The games of this ScheduleDay.  # noqa: E501
        :type: list[ScheduleGame]
        """

        self._games = games

    @property
    def events(self):
        """Gets the events of this ScheduleDay.  # noqa: E501


        :return: The events of this ScheduleDay.  # noqa: E501
        :rtype: list[object]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ScheduleDay.


        :param events: The events of this ScheduleDay.  # noqa: E501
        :type: list[object]
        """

        self._events = events

    @property
    def matches(self):
        """Gets the matches of this ScheduleDay.  # noqa: E501


        :return: The matches of this ScheduleDay.  # noqa: E501
        :rtype: list[object]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ScheduleDay.


        :param matches: The matches of this ScheduleDay.  # noqa: E501
        :type: list[object]
        """

        self._matches = matches

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScheduleDay, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduleDay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

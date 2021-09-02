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

class GameLiveDataPlaysPlaysByPeriod(object):
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
        'start_index': 'float',
        'plays': 'list[float]',
        'end_index': 'float'
    }

    attribute_map = {
        'start_index': 'startIndex',
        'plays': 'plays',
        'end_index': 'endIndex'
    }

    def __init__(self, start_index=None, plays=None, end_index=None):  # noqa: E501
        """GameLiveDataPlaysPlaysByPeriod - a model defined in Swagger"""  # noqa: E501
        self._start_index = None
        self._plays = None
        self._end_index = None
        self.discriminator = None
        if start_index is not None:
            self.start_index = start_index
        if plays is not None:
            self.plays = plays
        if end_index is not None:
            self.end_index = end_index

    @property
    def start_index(self):
        """Gets the start_index of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501


        :return: The start_index of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501
        :rtype: float
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this GameLiveDataPlaysPlaysByPeriod.


        :param start_index: The start_index of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501
        :type: float
        """

        self._start_index = start_index

    @property
    def plays(self):
        """Gets the plays of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501


        :return: The plays of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501
        :rtype: list[float]
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this GameLiveDataPlaysPlaysByPeriod.


        :param plays: The plays of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501
        :type: list[float]
        """

        self._plays = plays

    @property
    def end_index(self):
        """Gets the end_index of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501


        :return: The end_index of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501
        :rtype: float
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """Sets the end_index of this GameLiveDataPlaysPlaysByPeriod.


        :param end_index: The end_index of this GameLiveDataPlaysPlaysByPeriod.  # noqa: E501
        :type: float
        """

        self._end_index = end_index

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
        if issubclass(GameLiveDataPlaysPlaysByPeriod, dict):
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
        if not isinstance(other, GameLiveDataPlaysPlaysByPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
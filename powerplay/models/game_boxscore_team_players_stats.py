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

class GameBoxscoreTeamPlayersStats(object):
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
        'skater_stats': 'GameBoxscoreTeamPlayersStatsSkaterStats'
    }

    attribute_map = {
        'skater_stats': 'skaterStats'
    }

    def __init__(self, skater_stats=None):  # noqa: E501
        """GameBoxscoreTeamPlayersStats - a model defined in Swagger"""  # noqa: E501
        self._skater_stats = None
        self.discriminator = None
        if skater_stats is not None:
            self.skater_stats = skater_stats

    @property
    def skater_stats(self):
        """Gets the skater_stats of this GameBoxscoreTeamPlayersStats.  # noqa: E501


        :return: The skater_stats of this GameBoxscoreTeamPlayersStats.  # noqa: E501
        :rtype: GameBoxscoreTeamPlayersStatsSkaterStats
        """
        return self._skater_stats

    @skater_stats.setter
    def skater_stats(self, skater_stats):
        """Sets the skater_stats of this GameBoxscoreTeamPlayersStats.


        :param skater_stats: The skater_stats of this GameBoxscoreTeamPlayersStats.  # noqa: E501
        :type: GameBoxscoreTeamPlayersStatsSkaterStats
        """

        self._skater_stats = skater_stats

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
        if issubclass(GameBoxscoreTeamPlayersStats, dict):
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
        if not isinstance(other, GameBoxscoreTeamPlayersStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class TeamNextGameScheduleTeams(object):
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
        'away': 'TeamNextGameScheduleTeamsAway',
        'home': 'TeamNextGameScheduleTeamsHome'
    }

    attribute_map = {
        'away': 'away',
        'home': 'home'
    }

    def __init__(self, away=None, home=None):  # noqa: E501
        """TeamNextGameScheduleTeams - a model defined in Swagger"""  # noqa: E501
        self._away = None
        self._home = None
        self.discriminator = None
        if away is not None:
            self.away = away
        if home is not None:
            self.home = home

    @property
    def away(self):
        """Gets the away of this TeamNextGameScheduleTeams.  # noqa: E501


        :return: The away of this TeamNextGameScheduleTeams.  # noqa: E501
        :rtype: TeamNextGameScheduleTeamsAway
        """
        return self._away

    @away.setter
    def away(self, away):
        """Sets the away of this TeamNextGameScheduleTeams.


        :param away: The away of this TeamNextGameScheduleTeams.  # noqa: E501
        :type: TeamNextGameScheduleTeamsAway
        """

        self._away = away

    @property
    def home(self):
        """Gets the home of this TeamNextGameScheduleTeams.  # noqa: E501


        :return: The home of this TeamNextGameScheduleTeams.  # noqa: E501
        :rtype: TeamNextGameScheduleTeamsHome
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this TeamNextGameScheduleTeams.


        :param home: The home of this TeamNextGameScheduleTeams.  # noqa: E501
        :type: TeamNextGameScheduleTeamsHome
        """

        self._home = home

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
        if issubclass(TeamNextGameScheduleTeams, dict):
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
        if not isinstance(other, TeamNextGameScheduleTeams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

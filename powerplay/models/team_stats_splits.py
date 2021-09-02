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

class TeamStatsSplits(object):
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
        'stat': 'TeamStatsStat',
        'team': 'PlayerCurrentTeam'
    }

    attribute_map = {
        'stat': 'stat',
        'team': 'team'
    }

    def __init__(self, stat=None, team=None):  # noqa: E501
        """TeamStatsSplits - a model defined in Swagger"""  # noqa: E501
        self._stat = None
        self._team = None
        self.discriminator = None
        if stat is not None:
            self.stat = stat
        if team is not None:
            self.team = team

    @property
    def stat(self):
        """Gets the stat of this TeamStatsSplits.  # noqa: E501


        :return: The stat of this TeamStatsSplits.  # noqa: E501
        :rtype: TeamStatsStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this TeamStatsSplits.


        :param stat: The stat of this TeamStatsSplits.  # noqa: E501
        :type: TeamStatsStat
        """

        self._stat = stat

    @property
    def team(self):
        """Gets the team of this TeamStatsSplits.  # noqa: E501


        :return: The team of this TeamStatsSplits.  # noqa: E501
        :rtype: PlayerCurrentTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamStatsSplits.


        :param team: The team of this TeamStatsSplits.  # noqa: E501
        :type: PlayerCurrentTeam
        """

        self._team = team

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
        if issubclass(TeamStatsSplits, dict):
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
        if not isinstance(other, TeamStatsSplits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

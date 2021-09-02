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

class ScheduleGameTeamsHome(object):
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
        'league_record': 'ScheduleGameTeamsHomeLeagueRecord',
        'score': 'float',
        'team': 'PlayerCurrentTeam'
    }

    attribute_map = {
        'league_record': 'leagueRecord',
        'score': 'score',
        'team': 'team'
    }

    def __init__(self, league_record=None, score=None, team=None):  # noqa: E501
        """ScheduleGameTeamsHome - a model defined in Swagger"""  # noqa: E501
        self._league_record = None
        self._score = None
        self._team = None
        self.discriminator = None
        if league_record is not None:
            self.league_record = league_record
        if score is not None:
            self.score = score
        if team is not None:
            self.team = team

    @property
    def league_record(self):
        """Gets the league_record of this ScheduleGameTeamsHome.  # noqa: E501


        :return: The league_record of this ScheduleGameTeamsHome.  # noqa: E501
        :rtype: ScheduleGameTeamsHomeLeagueRecord
        """
        return self._league_record

    @league_record.setter
    def league_record(self, league_record):
        """Sets the league_record of this ScheduleGameTeamsHome.


        :param league_record: The league_record of this ScheduleGameTeamsHome.  # noqa: E501
        :type: ScheduleGameTeamsHomeLeagueRecord
        """

        self._league_record = league_record

    @property
    def score(self):
        """Gets the score of this ScheduleGameTeamsHome.  # noqa: E501


        :return: The score of this ScheduleGameTeamsHome.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ScheduleGameTeamsHome.


        :param score: The score of this ScheduleGameTeamsHome.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def team(self):
        """Gets the team of this ScheduleGameTeamsHome.  # noqa: E501


        :return: The team of this ScheduleGameTeamsHome.  # noqa: E501
        :rtype: PlayerCurrentTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this ScheduleGameTeamsHome.


        :param team: The team of this ScheduleGameTeamsHome.  # noqa: E501
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
        if issubclass(ScheduleGameTeamsHome, dict):
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
        if not isinstance(other, ScheduleGameTeamsHome):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

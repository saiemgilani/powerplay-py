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

class GameBoxscoreTeamCoaches(object):
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
        'person': 'GameBoxscoreTeamPerson',
        'position': 'GameBoxscoreTeamPosition'
    }

    attribute_map = {
        'person': 'person',
        'position': 'position'
    }

    def __init__(self, person=None, position=None):  # noqa: E501
        """GameBoxscoreTeamCoaches - a model defined in Swagger"""  # noqa: E501
        self._person = None
        self._position = None
        self.discriminator = None
        if person is not None:
            self.person = person
        if position is not None:
            self.position = position

    @property
    def person(self):
        """Gets the person of this GameBoxscoreTeamCoaches.  # noqa: E501


        :return: The person of this GameBoxscoreTeamCoaches.  # noqa: E501
        :rtype: GameBoxscoreTeamPerson
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this GameBoxscoreTeamCoaches.


        :param person: The person of this GameBoxscoreTeamCoaches.  # noqa: E501
        :type: GameBoxscoreTeamPerson
        """

        self._person = person

    @property
    def position(self):
        """Gets the position of this GameBoxscoreTeamCoaches.  # noqa: E501


        :return: The position of this GameBoxscoreTeamCoaches.  # noqa: E501
        :rtype: GameBoxscoreTeamPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GameBoxscoreTeamCoaches.


        :param position: The position of this GameBoxscoreTeamCoaches.  # noqa: E501
        :type: GameBoxscoreTeamPosition
        """

        self._position = position

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
        if issubclass(GameBoxscoreTeamCoaches, dict):
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
        if not isinstance(other, GameBoxscoreTeamCoaches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

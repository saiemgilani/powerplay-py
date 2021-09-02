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

class GameBoxscoreTeamPlayersPosition(object):
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
        'code': 'str',
        'name': 'str',
        'type': 'str',
        'abbreviation': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'type': 'type',
        'abbreviation': 'abbreviation'
    }

    def __init__(self, code=None, name=None, type=None, abbreviation=None):  # noqa: E501
        """GameBoxscoreTeamPlayersPosition - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name = None
        self._type = None
        self._abbreviation = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if abbreviation is not None:
            self.abbreviation = abbreviation

    @property
    def code(self):
        """Gets the code of this GameBoxscoreTeamPlayersPosition.  # noqa: E501


        :return: The code of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GameBoxscoreTeamPlayersPosition.


        :param code: The code of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this GameBoxscoreTeamPlayersPosition.  # noqa: E501


        :return: The name of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GameBoxscoreTeamPlayersPosition.


        :param name: The name of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this GameBoxscoreTeamPlayersPosition.  # noqa: E501


        :return: The type of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GameBoxscoreTeamPlayersPosition.


        :param type: The type of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def abbreviation(self):
        """Gets the abbreviation of this GameBoxscoreTeamPlayersPosition.  # noqa: E501


        :return: The abbreviation of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this GameBoxscoreTeamPlayersPosition.


        :param abbreviation: The abbreviation of this GameBoxscoreTeamPlayersPosition.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

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
        if issubclass(GameBoxscoreTeamPlayersPosition, dict):
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
        if not isinstance(other, GameBoxscoreTeamPlayersPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

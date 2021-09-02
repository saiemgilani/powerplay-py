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

class GameOfficial(object):
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
        'official': 'GameOfficialOfficial',
        'official_type': 'str'
    }

    attribute_map = {
        'official': 'official',
        'official_type': 'officialType'
    }

    def __init__(self, official=None, official_type=None):  # noqa: E501
        """GameOfficial - a model defined in Swagger"""  # noqa: E501
        self._official = None
        self._official_type = None
        self.discriminator = None
        if official is not None:
            self.official = official
        if official_type is not None:
            self.official_type = official_type

    @property
    def official(self):
        """Gets the official of this GameOfficial.  # noqa: E501


        :return: The official of this GameOfficial.  # noqa: E501
        :rtype: GameOfficialOfficial
        """
        return self._official

    @official.setter
    def official(self, official):
        """Sets the official of this GameOfficial.


        :param official: The official of this GameOfficial.  # noqa: E501
        :type: GameOfficialOfficial
        """

        self._official = official

    @property
    def official_type(self):
        """Gets the official_type of this GameOfficial.  # noqa: E501


        :return: The official_type of this GameOfficial.  # noqa: E501
        :rtype: str
        """
        return self._official_type

    @official_type.setter
    def official_type(self, official_type):
        """Sets the official_type of this GameOfficial.


        :param official_type: The official_type of this GameOfficial.  # noqa: E501
        :type: str
        """
        allowed_values = ["Linesman", "Referee"]  # noqa: E501
        if official_type not in allowed_values:
            raise ValueError(
                "Invalid value for `official_type` ({0}), must be one of {1}"  # noqa: E501
                .format(official_type, allowed_values)
            )

        self._official_type = official_type

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
        if issubclass(GameOfficial, dict):
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
        if not isinstance(other, GameOfficial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

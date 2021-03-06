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

class DraftRounds(object):
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
        'round_number': 'float',
        'round': 'float',
        'picks': 'list[DraftPicks]'
    }

    attribute_map = {
        'round_number': 'roundNumber',
        'round': 'round',
        'picks': 'picks'
    }

    def __init__(self, round_number=None, round=None, picks=None):  # noqa: E501
        """DraftRounds - a model defined in Swagger"""  # noqa: E501
        self._round_number = None
        self._round = None
        self._picks = None
        self.discriminator = None
        if round_number is not None:
            self.round_number = round_number
        if round is not None:
            self.round = round
        if picks is not None:
            self.picks = picks

    @property
    def round_number(self):
        """Gets the round_number of this DraftRounds.  # noqa: E501


        :return: The round_number of this DraftRounds.  # noqa: E501
        :rtype: float
        """
        return self._round_number

    @round_number.setter
    def round_number(self, round_number):
        """Sets the round_number of this DraftRounds.


        :param round_number: The round_number of this DraftRounds.  # noqa: E501
        :type: float
        """

        self._round_number = round_number

    @property
    def round(self):
        """Gets the round of this DraftRounds.  # noqa: E501


        :return: The round of this DraftRounds.  # noqa: E501
        :rtype: float
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this DraftRounds.


        :param round: The round of this DraftRounds.  # noqa: E501
        :type: float
        """

        self._round = round

    @property
    def picks(self):
        """Gets the picks of this DraftRounds.  # noqa: E501


        :return: The picks of this DraftRounds.  # noqa: E501
        :rtype: list[DraftPicks]
        """
        return self._picks

    @picks.setter
    def picks(self, picks):
        """Sets the picks of this DraftRounds.


        :param picks: The picks of this DraftRounds.  # noqa: E501
        :type: list[DraftPicks]
        """

        self._picks = picks

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
        if issubclass(DraftRounds, dict):
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
        if not isinstance(other, DraftRounds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

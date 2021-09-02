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

class GameGameDataDatetime(object):
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
        'date_time': 'datetime',
        'end_date_time': 'datetime'
    }

    attribute_map = {
        'date_time': 'dateTime',
        'end_date_time': 'endDateTime'
    }

    def __init__(self, date_time=None, end_date_time=None):  # noqa: E501
        """GameGameDataDatetime - a model defined in Swagger"""  # noqa: E501
        self._date_time = None
        self._end_date_time = None
        self.discriminator = None
        if date_time is not None:
            self.date_time = date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time

    @property
    def date_time(self):
        """Gets the date_time of this GameGameDataDatetime.  # noqa: E501


        :return: The date_time of this GameGameDataDatetime.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this GameGameDataDatetime.


        :param date_time: The date_time of this GameGameDataDatetime.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this GameGameDataDatetime.  # noqa: E501


        :return: The end_date_time of this GameGameDataDatetime.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this GameGameDataDatetime.


        :param end_date_time: The end_date_time of this GameGameDataDatetime.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

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
        if issubclass(GameGameDataDatetime, dict):
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
        if not isinstance(other, GameGameDataDatetime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

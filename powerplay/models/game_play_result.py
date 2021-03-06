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

class GamePlayResult(object):
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
        'event': 'str',
        'event_code': 'str',
        'event_type_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'event': 'event',
        'event_code': 'eventCode',
        'event_type_id': 'eventTypeId',
        'description': 'description'
    }

    def __init__(self, event=None, event_code=None, event_type_id=None, description=None):  # noqa: E501
        """GamePlayResult - a model defined in Swagger"""  # noqa: E501
        self._event = None
        self._event_code = None
        self._event_type_id = None
        self._description = None
        self.discriminator = None
        if event is not None:
            self.event = event
        if event_code is not None:
            self.event_code = event_code
        if event_type_id is not None:
            self.event_type_id = event_type_id
        if description is not None:
            self.description = description

    @property
    def event(self):
        """Gets the event of this GamePlayResult.  # noqa: E501


        :return: The event of this GamePlayResult.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this GamePlayResult.


        :param event: The event of this GamePlayResult.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def event_code(self):
        """Gets the event_code of this GamePlayResult.  # noqa: E501


        :return: The event_code of this GamePlayResult.  # noqa: E501
        :rtype: str
        """
        return self._event_code

    @event_code.setter
    def event_code(self, event_code):
        """Sets the event_code of this GamePlayResult.


        :param event_code: The event_code of this GamePlayResult.  # noqa: E501
        :type: str
        """

        self._event_code = event_code

    @property
    def event_type_id(self):
        """Gets the event_type_id of this GamePlayResult.  # noqa: E501


        :return: The event_type_id of this GamePlayResult.  # noqa: E501
        :rtype: str
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this GamePlayResult.


        :param event_type_id: The event_type_id of this GamePlayResult.  # noqa: E501
        :type: str
        """

        self._event_type_id = event_type_id

    @property
    def description(self):
        """Gets the description of this GamePlayResult.  # noqa: E501


        :return: The description of this GamePlayResult.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GamePlayResult.


        :param description: The description of this GamePlayResult.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(GamePlayResult, dict):
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
        if not isinstance(other, GamePlayResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class GameOfficialOfficial(object):
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
        'id': 'float',
        'full_name': 'str',
        'link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'fullName',
        'link': 'link'
    }

    def __init__(self, id=None, full_name=None, link=None):  # noqa: E501
        """GameOfficialOfficial - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._full_name = None
        self._link = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if full_name is not None:
            self.full_name = full_name
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this GameOfficialOfficial.  # noqa: E501


        :return: The id of this GameOfficialOfficial.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GameOfficialOfficial.


        :param id: The id of this GameOfficialOfficial.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def full_name(self):
        """Gets the full_name of this GameOfficialOfficial.  # noqa: E501


        :return: The full_name of this GameOfficialOfficial.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GameOfficialOfficial.


        :param full_name: The full_name of this GameOfficialOfficial.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def link(self):
        """Gets the link of this GameOfficialOfficial.  # noqa: E501


        :return: The link of this GameOfficialOfficial.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this GameOfficialOfficial.


        :param link: The link of this GameOfficialOfficial.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if issubclass(GameOfficialOfficial, dict):
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
        if not isinstance(other, GameOfficialOfficial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

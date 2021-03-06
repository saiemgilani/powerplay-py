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

class GameMediaAudioItems(object):
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
        'media_state': 'str',
        'media_playback_id': 'str',
        'media_feed_type': 'str',
        'call_letters': 'str',
        'event_id': 'str',
        'language': 'str',
        'free_game': 'bool',
        'feed_name': 'str',
        'game_plus': 'bool'
    }

    attribute_map = {
        'media_state': 'mediaState',
        'media_playback_id': 'mediaPlaybackId',
        'media_feed_type': 'mediaFeedType',
        'call_letters': 'callLetters',
        'event_id': 'eventId',
        'language': 'language',
        'free_game': 'freeGame',
        'feed_name': 'feedName',
        'game_plus': 'gamePlus'
    }

    def __init__(self, media_state=None, media_playback_id=None, media_feed_type=None, call_letters=None, event_id=None, language=None, free_game=None, feed_name=None, game_plus=None):  # noqa: E501
        """GameMediaAudioItems - a model defined in Swagger"""  # noqa: E501
        self._media_state = None
        self._media_playback_id = None
        self._media_feed_type = None
        self._call_letters = None
        self._event_id = None
        self._language = None
        self._free_game = None
        self._feed_name = None
        self._game_plus = None
        self.discriminator = None
        if media_state is not None:
            self.media_state = media_state
        if media_playback_id is not None:
            self.media_playback_id = media_playback_id
        if media_feed_type is not None:
            self.media_feed_type = media_feed_type
        if call_letters is not None:
            self.call_letters = call_letters
        if event_id is not None:
            self.event_id = event_id
        if language is not None:
            self.language = language
        if free_game is not None:
            self.free_game = free_game
        if feed_name is not None:
            self.feed_name = feed_name
        if game_plus is not None:
            self.game_plus = game_plus

    @property
    def media_state(self):
        """Gets the media_state of this GameMediaAudioItems.  # noqa: E501


        :return: The media_state of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._media_state

    @media_state.setter
    def media_state(self, media_state):
        """Sets the media_state of this GameMediaAudioItems.


        :param media_state: The media_state of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._media_state = media_state

    @property
    def media_playback_id(self):
        """Gets the media_playback_id of this GameMediaAudioItems.  # noqa: E501


        :return: The media_playback_id of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._media_playback_id

    @media_playback_id.setter
    def media_playback_id(self, media_playback_id):
        """Sets the media_playback_id of this GameMediaAudioItems.


        :param media_playback_id: The media_playback_id of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._media_playback_id = media_playback_id

    @property
    def media_feed_type(self):
        """Gets the media_feed_type of this GameMediaAudioItems.  # noqa: E501


        :return: The media_feed_type of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._media_feed_type

    @media_feed_type.setter
    def media_feed_type(self, media_feed_type):
        """Sets the media_feed_type of this GameMediaAudioItems.


        :param media_feed_type: The media_feed_type of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._media_feed_type = media_feed_type

    @property
    def call_letters(self):
        """Gets the call_letters of this GameMediaAudioItems.  # noqa: E501


        :return: The call_letters of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._call_letters

    @call_letters.setter
    def call_letters(self, call_letters):
        """Sets the call_letters of this GameMediaAudioItems.


        :param call_letters: The call_letters of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._call_letters = call_letters

    @property
    def event_id(self):
        """Gets the event_id of this GameMediaAudioItems.  # noqa: E501


        :return: The event_id of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this GameMediaAudioItems.


        :param event_id: The event_id of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def language(self):
        """Gets the language of this GameMediaAudioItems.  # noqa: E501


        :return: The language of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this GameMediaAudioItems.


        :param language: The language of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def free_game(self):
        """Gets the free_game of this GameMediaAudioItems.  # noqa: E501


        :return: The free_game of this GameMediaAudioItems.  # noqa: E501
        :rtype: bool
        """
        return self._free_game

    @free_game.setter
    def free_game(self, free_game):
        """Sets the free_game of this GameMediaAudioItems.


        :param free_game: The free_game of this GameMediaAudioItems.  # noqa: E501
        :type: bool
        """

        self._free_game = free_game

    @property
    def feed_name(self):
        """Gets the feed_name of this GameMediaAudioItems.  # noqa: E501


        :return: The feed_name of this GameMediaAudioItems.  # noqa: E501
        :rtype: str
        """
        return self._feed_name

    @feed_name.setter
    def feed_name(self, feed_name):
        """Sets the feed_name of this GameMediaAudioItems.


        :param feed_name: The feed_name of this GameMediaAudioItems.  # noqa: E501
        :type: str
        """

        self._feed_name = feed_name

    @property
    def game_plus(self):
        """Gets the game_plus of this GameMediaAudioItems.  # noqa: E501


        :return: The game_plus of this GameMediaAudioItems.  # noqa: E501
        :rtype: bool
        """
        return self._game_plus

    @game_plus.setter
    def game_plus(self, game_plus):
        """Sets the game_plus of this GameMediaAudioItems.


        :param game_plus: The game_plus of this GameMediaAudioItems.  # noqa: E501
        :type: bool
        """

        self._game_plus = game_plus

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
        if issubclass(GameMediaAudioItems, dict):
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
        if not isinstance(other, GameMediaAudioItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

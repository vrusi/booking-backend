# coding: utf-8

"""
    MTAA API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Orders.api_models.configuration import Configuration


class Rating(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'author': 'User',
        'rating': 'int',
        'title': 'str',
        'content': 'str',
        'image': 'str',
        'created_at': 'str',
        'replies': 'list[RatingReply]'
    }

    attribute_map = {
        'id': 'id',
        'author': 'author',
        'rating': 'rating',
        'title': 'title',
        'content': 'content',
        'image': 'image',
        'created_at': 'createdAt',
        'replies': 'replies'
    }

    def __init__(self, id=None, author=None, rating=None, title=None, content=None, image=None, created_at=None, replies=None, local_vars_configuration=None):  # noqa: E501
        """Rating - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._author = None
        self._rating = None
        self._title = None
        self._content = None
        self._image = None
        self._created_at = None
        self._replies = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if author is not None:
            self.author = author
        if rating is not None:
            self.rating = rating
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if image is not None:
            self.image = image
        if created_at is not None:
            self.created_at = created_at
        if replies is not None:
            self.replies = replies

    @property
    def id(self):
        """Gets the id of this Rating.  # noqa: E501


        :return: The id of this Rating.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rating.


        :param id: The id of this Rating.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def author(self):
        """Gets the author of this Rating.  # noqa: E501


        :return: The author of this Rating.  # noqa: E501
        :rtype: User
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Rating.


        :param author: The author of this Rating.  # noqa: E501
        :type: User
        """

        self._author = author

    @property
    def rating(self):
        """Gets the rating of this Rating.  # noqa: E501


        :return: The rating of this Rating.  # noqa: E501
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Rating.


        :param rating: The rating of this Rating.  # noqa: E501
        :type: int
        """

        self._rating = rating

    @property
    def title(self):
        """Gets the title of this Rating.  # noqa: E501


        :return: The title of this Rating.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Rating.


        :param title: The title of this Rating.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this Rating.  # noqa: E501


        :return: The content of this Rating.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Rating.


        :param content: The content of this Rating.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def image(self):
        """Gets the image of this Rating.  # noqa: E501


        :return: The image of this Rating.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Rating.


        :param image: The image of this Rating.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def created_at(self):
        """Gets the created_at of this Rating.  # noqa: E501


        :return: The created_at of this Rating.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Rating.


        :param created_at: The created_at of this Rating.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def replies(self):
        """Gets the replies of this Rating.  # noqa: E501


        :return: The replies of this Rating.  # noqa: E501
        :rtype: list[RatingReply]
        """
        return self._replies

    @replies.setter
    def replies(self, replies):
        """Sets the replies of this Rating.


        :param replies: The replies of this Rating.  # noqa: E501
        :type: list[RatingReply]
        """

        self._replies = replies

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Rating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rating):
            return True

        return self.to_dict() != other.to_dict()
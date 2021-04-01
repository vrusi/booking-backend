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


class Order(object):
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
        'state': 'str',
        'accommodation': 'Accommodation',
        'occupant_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'accommodation': 'accommodation',
        'occupant_count': 'occupant_count'
    }

    def __init__(self, id=None, state=None, accommodation=None, occupant_count=None, local_vars_configuration=None):  # noqa: E501
        """Order - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._state = None
        self._accommodation = None
        self._occupant_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if accommodation is not None:
            self.accommodation = accommodation
        if occupant_count is not None:
            self.occupant_count = occupant_count

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        :return: The id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this Order.  # noqa: E501


        :return: The state of this Order.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Order.


        :param state: The state of this Order.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def accommodation(self):
        """Gets the accommodation of this Order.  # noqa: E501


        :return: The accommodation of this Order.  # noqa: E501
        :rtype: Accommodation
        """
        return self._accommodation

    @accommodation.setter
    def accommodation(self, accommodation):
        """Sets the accommodation of this Order.


        :param accommodation: The accommodation of this Order.  # noqa: E501
        :type: Accommodation
        """

        self._accommodation = accommodation

    @property
    def occupant_count(self):
        """Gets the occupant_count of this Order.  # noqa: E501


        :return: The occupant_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._occupant_count

    @occupant_count.setter
    def occupant_count(self, occupant_count):
        """Sets the occupant_count of this Order.


        :param occupant_count: The occupant_count of this Order.  # noqa: E501
        :type: int
        """

        self._occupant_count = occupant_count

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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()

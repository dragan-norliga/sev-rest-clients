# coding: utf-8

"""
    Sev Data flex API v1.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustDKRReading(object):
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
        'time_stamp': 'datetime',
        'reading': 'float',
        'unit': 'str',
        'price_unit': 'float',
        'tarif': 'int'
    }

    attribute_map = {
        'time_stamp': 'time_stamp',
        'reading': 'reading',
        'unit': 'unit',
        'price_unit': 'price_unit',
        'tarif': 'tarif'
    }

    def __init__(self, time_stamp=None, reading=None, unit=None, price_unit=None, tarif=None):  # noqa: E501
        """CustDKRReading - a model defined in Swagger"""  # noqa: E501
        self._time_stamp = None
        self._reading = None
        self._unit = None
        self._price_unit = None
        self._tarif = None
        self.discriminator = None
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if reading is not None:
            self.reading = reading
        if unit is not None:
            self.unit = unit
        if price_unit is not None:
            self.price_unit = price_unit
        if tarif is not None:
            self.tarif = tarif

    @property
    def time_stamp(self):
        """Gets the time_stamp of this CustDKRReading.  # noqa: E501


        :return: The time_stamp of this CustDKRReading.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this CustDKRReading.


        :param time_stamp: The time_stamp of this CustDKRReading.  # noqa: E501
        :type: datetime
        """

        self._time_stamp = time_stamp

    @property
    def reading(self):
        """Gets the reading of this CustDKRReading.  # noqa: E501


        :return: The reading of this CustDKRReading.  # noqa: E501
        :rtype: float
        """
        return self._reading

    @reading.setter
    def reading(self, reading):
        """Sets the reading of this CustDKRReading.


        :param reading: The reading of this CustDKRReading.  # noqa: E501
        :type: float
        """

        self._reading = reading

    @property
    def unit(self):
        """Gets the unit of this CustDKRReading.  # noqa: E501


        :return: The unit of this CustDKRReading.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CustDKRReading.


        :param unit: The unit of this CustDKRReading.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def price_unit(self):
        """Gets the price_unit of this CustDKRReading.  # noqa: E501


        :return: The price_unit of this CustDKRReading.  # noqa: E501
        :rtype: float
        """
        return self._price_unit

    @price_unit.setter
    def price_unit(self, price_unit):
        """Sets the price_unit of this CustDKRReading.


        :param price_unit: The price_unit of this CustDKRReading.  # noqa: E501
        :type: float
        """

        self._price_unit = price_unit

    @property
    def tarif(self):
        """Gets the tarif of this CustDKRReading.  # noqa: E501


        :return: The tarif of this CustDKRReading.  # noqa: E501
        :rtype: int
        """
        return self._tarif

    @tarif.setter
    def tarif(self, tarif):
        """Sets the tarif of this CustDKRReading.


        :param tarif: The tarif of this CustDKRReading.  # noqa: E501
        :type: int
        """

        self._tarif = tarif

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
        if issubclass(CustDKRReading, dict):
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
        if not isinstance(other, CustDKRReading):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
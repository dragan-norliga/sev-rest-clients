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

class CustomerWithInstallations(object):
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
        'customer_name': 'str',
        'installations': 'list[CustInstallation]'
    }

    attribute_map = {
        'customer_name': 'customer_name',
        'installations': 'installations'
    }

    def __init__(self, customer_name=None, installations=None):  # noqa: E501
        """CustomerWithInstallations - a model defined in Swagger"""  # noqa: E501
        self._customer_name = None
        self._installations = None
        self.discriminator = None
        if customer_name is not None:
            self.customer_name = customer_name
        if installations is not None:
            self.installations = installations

    @property
    def customer_name(self):
        """Gets the customer_name of this CustomerWithInstallations.  # noqa: E501


        :return: The customer_name of this CustomerWithInstallations.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this CustomerWithInstallations.


        :param customer_name: The customer_name of this CustomerWithInstallations.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def installations(self):
        """Gets the installations of this CustomerWithInstallations.  # noqa: E501


        :return: The installations of this CustomerWithInstallations.  # noqa: E501
        :rtype: list[CustInstallation]
        """
        return self._installations

    @installations.setter
    def installations(self, installations):
        """Sets the installations of this CustomerWithInstallations.


        :param installations: The installations of this CustomerWithInstallations.  # noqa: E501
        :type: list[CustInstallation]
        """

        self._installations = installations

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
        if issubclass(CustomerWithInstallations, dict):
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
        if not isinstance(other, CustomerWithInstallations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

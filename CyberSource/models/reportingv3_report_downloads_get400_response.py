# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Reportingv3ReportDownloadsGet400Response(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'submit_time_utc': 'datetime',
        'reason': 'str',
        'message': 'str',
        'details': 'list[Reportingv3ReportDownloadsGet400ResponseDetails]'
    }

    attribute_map = {
        'submit_time_utc': 'submitTimeUtc',
        'reason': 'reason',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, submit_time_utc=None, reason=None, message=None, details=None):
        """
        Reportingv3ReportDownloadsGet400Response - a model defined in Swagger
        """

        self._submit_time_utc = None
        self._reason = None
        self._message = None
        self._details = None

        self.submit_time_utc = submit_time_utc
        self.reason = reason
        self.message = message
        self.details = details

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this Reportingv3ReportDownloadsGet400Response.
        Time of request in UTC.  

        :return: The submit_time_utc of this Reportingv3ReportDownloadsGet400Response.
        :rtype: datetime
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this Reportingv3ReportDownloadsGet400Response.
        Time of request in UTC.  

        :param submit_time_utc: The submit_time_utc of this Reportingv3ReportDownloadsGet400Response.
        :type: datetime
        """
        if submit_time_utc is None:
            raise ValueError("Invalid value for `submit_time_utc`, must not be `None`")

        self._submit_time_utc = submit_time_utc

    @property
    def reason(self):
        """
        Gets the reason of this Reportingv3ReportDownloadsGet400Response.
        Documented reason code 

        :return: The reason of this Reportingv3ReportDownloadsGet400Response.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Reportingv3ReportDownloadsGet400Response.
        Documented reason code 

        :param reason: The reason of this Reportingv3ReportDownloadsGet400Response.
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")

        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this Reportingv3ReportDownloadsGet400Response.
        Short descriptive message to the user. 

        :return: The message of this Reportingv3ReportDownloadsGet400Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Reportingv3ReportDownloadsGet400Response.
        Short descriptive message to the user. 

        :param message: The message of this Reportingv3ReportDownloadsGet400Response.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def details(self):
        """
        Gets the details of this Reportingv3ReportDownloadsGet400Response.
        Error field list 

        :return: The details of this Reportingv3ReportDownloadsGet400Response.
        :rtype: list[Reportingv3ReportDownloadsGet400ResponseDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Reportingv3ReportDownloadsGet400Response.
        Error field list 

        :param details: The details of this Reportingv3ReportDownloadsGet400Response.
        :type: list[Reportingv3ReportDownloadsGet400ResponseDetails]
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")

        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Reportingv3ReportDownloadsGet400Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
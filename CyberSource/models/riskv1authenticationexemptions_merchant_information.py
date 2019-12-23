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


class Riskv1authenticationexemptionsMerchantInformation(object):
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
        'visa_merchant_id': 'str',
        'card_acceptor_id': 'str',
        'merchant_category_code': 'str',
        'merchant_descriptor': 'Riskv1authenticationexemptionsMerchantInformationMerchantDescriptor'
    }

    attribute_map = {
        'visa_merchant_id': 'visaMerchantId',
        'card_acceptor_id': 'cardAcceptorId',
        'merchant_category_code': 'merchantCategoryCode',
        'merchant_descriptor': 'merchantDescriptor'
    }

    def __init__(self, visa_merchant_id=None, card_acceptor_id=None, merchant_category_code=None, merchant_descriptor=None):
        """
        Riskv1authenticationexemptionsMerchantInformation - a model defined in Swagger
        """

        self._visa_merchant_id = None
        self._card_acceptor_id = None
        self._merchant_category_code = None
        self._merchant_descriptor = None

        if visa_merchant_id is not None:
          self.visa_merchant_id = visa_merchant_id
        if card_acceptor_id is not None:
          self.card_acceptor_id = card_acceptor_id
        if merchant_category_code is not None:
          self.merchant_category_code = merchant_category_code
        if merchant_descriptor is not None:
          self.merchant_descriptor = merchant_descriptor

    @property
    def visa_merchant_id(self):
        """
        Gets the visa_merchant_id of this Riskv1authenticationexemptionsMerchantInformation.
        Network assigned merchant identifier. 

        :return: The visa_merchant_id of this Riskv1authenticationexemptionsMerchantInformation.
        :rtype: str
        """
        return self._visa_merchant_id

    @visa_merchant_id.setter
    def visa_merchant_id(self, visa_merchant_id):
        """
        Sets the visa_merchant_id of this Riskv1authenticationexemptionsMerchantInformation.
        Network assigned merchant identifier. 

        :param visa_merchant_id: The visa_merchant_id of this Riskv1authenticationexemptionsMerchantInformation.
        :type: str
        """
        if visa_merchant_id is not None and len(visa_merchant_id) > 16:
            raise ValueError("Invalid value for `visa_merchant_id`, length must be less than or equal to `16`")

        self._visa_merchant_id = visa_merchant_id

    @property
    def card_acceptor_id(self):
        """
        Gets the card_acceptor_id of this Riskv1authenticationexemptionsMerchantInformation.
        Card Acceptor ID (CAID) for the current transaction. 

        :return: The card_acceptor_id of this Riskv1authenticationexemptionsMerchantInformation.
        :rtype: str
        """
        return self._card_acceptor_id

    @card_acceptor_id.setter
    def card_acceptor_id(self, card_acceptor_id):
        """
        Sets the card_acceptor_id of this Riskv1authenticationexemptionsMerchantInformation.
        Card Acceptor ID (CAID) for the current transaction. 

        :param card_acceptor_id: The card_acceptor_id of this Riskv1authenticationexemptionsMerchantInformation.
        :type: str
        """
        if card_acceptor_id is not None and len(card_acceptor_id) > 15:
            raise ValueError("Invalid value for `card_acceptor_id`, length must be less than or equal to `15`")

        self._card_acceptor_id = card_acceptor_id

    @property
    def merchant_category_code(self):
        """
        Gets the merchant_category_code of this Riskv1authenticationexemptionsMerchantInformation.
        Merchant Category Code (MCC). 4 digit numeric. 

        :return: The merchant_category_code of this Riskv1authenticationexemptionsMerchantInformation.
        :rtype: str
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """
        Sets the merchant_category_code of this Riskv1authenticationexemptionsMerchantInformation.
        Merchant Category Code (MCC). 4 digit numeric. 

        :param merchant_category_code: The merchant_category_code of this Riskv1authenticationexemptionsMerchantInformation.
        :type: str
        """
        if merchant_category_code is not None and len(merchant_category_code) > 20:
            raise ValueError("Invalid value for `merchant_category_code`, length must be less than or equal to `20`")

        self._merchant_category_code = merchant_category_code

    @property
    def merchant_descriptor(self):
        """
        Gets the merchant_descriptor of this Riskv1authenticationexemptionsMerchantInformation.

        :return: The merchant_descriptor of this Riskv1authenticationexemptionsMerchantInformation.
        :rtype: Riskv1authenticationexemptionsMerchantInformationMerchantDescriptor
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """
        Sets the merchant_descriptor of this Riskv1authenticationexemptionsMerchantInformation.

        :param merchant_descriptor: The merchant_descriptor of this Riskv1authenticationexemptionsMerchantInformation.
        :type: Riskv1authenticationexemptionsMerchantInformationMerchantDescriptor
        """

        self._merchant_descriptor = merchant_descriptor

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
        if not isinstance(other, Riskv1authenticationexemptionsMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
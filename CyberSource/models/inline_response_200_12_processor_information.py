# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20012ProcessorInformation(object):
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
        'processor': 'InlineResponse20012ProcessorInformationProcessor',
        'transaction_id': 'str',
        'network_transaction_id': 'str',
        'response_id': 'str',
        'provider_transaction_id': 'str',
        'approval_code': 'str',
        'response_code': 'str',
        'avs': 'InlineResponse201ProcessorInformationAvs',
        'card_verification': 'InlineResponse20012ProcessorInformationCardVerification',
        'ach_verification': 'InlineResponse20012ProcessorInformationAchVerification',
        'electronic_verification_results': 'InlineResponse20012ProcessorInformationElectronicVerificationResults'
    }

    attribute_map = {
        'processor': 'processor',
        'transaction_id': 'transactionId',
        'network_transaction_id': 'networkTransactionId',
        'response_id': 'responseId',
        'provider_transaction_id': 'providerTransactionId',
        'approval_code': 'approvalCode',
        'response_code': 'responseCode',
        'avs': 'avs',
        'card_verification': 'cardVerification',
        'ach_verification': 'achVerification',
        'electronic_verification_results': 'electronicVerificationResults'
    }

    def __init__(self, processor=None, transaction_id=None, network_transaction_id=None, response_id=None, provider_transaction_id=None, approval_code=None, response_code=None, avs=None, card_verification=None, ach_verification=None, electronic_verification_results=None):
        """
        InlineResponse20012ProcessorInformation - a model defined in Swagger
        """

        self._processor = None
        self._transaction_id = None
        self._network_transaction_id = None
        self._response_id = None
        self._provider_transaction_id = None
        self._approval_code = None
        self._response_code = None
        self._avs = None
        self._card_verification = None
        self._ach_verification = None
        self._electronic_verification_results = None

        if processor is not None:
          self.processor = processor
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if network_transaction_id is not None:
          self.network_transaction_id = network_transaction_id
        if response_id is not None:
          self.response_id = response_id
        if provider_transaction_id is not None:
          self.provider_transaction_id = provider_transaction_id
        if approval_code is not None:
          self.approval_code = approval_code
        if response_code is not None:
          self.response_code = response_code
        if avs is not None:
          self.avs = avs
        if card_verification is not None:
          self.card_verification = card_verification
        if ach_verification is not None:
          self.ach_verification = ach_verification
        if electronic_verification_results is not None:
          self.electronic_verification_results = electronic_verification_results

    @property
    def processor(self):
        """
        Gets the processor of this InlineResponse20012ProcessorInformation.

        :return: The processor of this InlineResponse20012ProcessorInformation.
        :rtype: InlineResponse20012ProcessorInformationProcessor
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """
        Sets the processor of this InlineResponse20012ProcessorInformation.

        :param processor: The processor of this InlineResponse20012ProcessorInformation.
        :type: InlineResponse20012ProcessorInformationProcessor
        """

        self._processor = processor

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this InlineResponse20012ProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this  value. 

        :return: The transaction_id of this InlineResponse20012ProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this InlineResponse20012ProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this  value. 

        :param transaction_id: The transaction_id of this InlineResponse20012ProcessorInformation.
        :type: str
        """
        if transaction_id is not None and len(transaction_id) > 50:
            raise ValueError("Invalid value for `transaction_id`, length must be less than or equal to `50`")

        self._transaction_id = transaction_id

    @property
    def network_transaction_id(self):
        """
        Gets the network_transaction_id of this InlineResponse20012ProcessorInformation.
        The description for this field is not available.

        :return: The network_transaction_id of this InlineResponse20012ProcessorInformation.
        :rtype: str
        """
        return self._network_transaction_id

    @network_transaction_id.setter
    def network_transaction_id(self, network_transaction_id):
        """
        Sets the network_transaction_id of this InlineResponse20012ProcessorInformation.
        The description for this field is not available.

        :param network_transaction_id: The network_transaction_id of this InlineResponse20012ProcessorInformation.
        :type: str
        """

        self._network_transaction_id = network_transaction_id

    @property
    def response_id(self):
        """
        Gets the response_id of this InlineResponse20012ProcessorInformation.
        The description for this field is not available.

        :return: The response_id of this InlineResponse20012ProcessorInformation.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """
        Sets the response_id of this InlineResponse20012ProcessorInformation.
        The description for this field is not available.

        :param response_id: The response_id of this InlineResponse20012ProcessorInformation.
        :type: str
        """

        self._response_id = response_id

    @property
    def provider_transaction_id(self):
        """
        Gets the provider_transaction_id of this InlineResponse20012ProcessorInformation.
        The description for this field is not available.

        :return: The provider_transaction_id of this InlineResponse20012ProcessorInformation.
        :rtype: str
        """
        return self._provider_transaction_id

    @provider_transaction_id.setter
    def provider_transaction_id(self, provider_transaction_id):
        """
        Sets the provider_transaction_id of this InlineResponse20012ProcessorInformation.
        The description for this field is not available.

        :param provider_transaction_id: The provider_transaction_id of this InlineResponse20012ProcessorInformation.
        :type: str
        """

        self._provider_transaction_id = provider_transaction_id

    @property
    def approval_code(self):
        """
        Gets the approval_code of this InlineResponse20012ProcessorInformation.
        Authorization code. Returned only when the processor returns this value. 

        :return: The approval_code of this InlineResponse20012ProcessorInformation.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this InlineResponse20012ProcessorInformation.
        Authorization code. Returned only when the processor returns this value. 

        :param approval_code: The approval_code of this InlineResponse20012ProcessorInformation.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def response_code(self):
        """
        Gets the response_code of this InlineResponse20012ProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  Important Do not use this field to evaluate the result of the authorization. 

        :return: The response_code of this InlineResponse20012ProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this InlineResponse20012ProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  Important Do not use this field to evaluate the result of the authorization. 

        :param response_code: The response_code of this InlineResponse20012ProcessorInformation.
        :type: str
        """
        if response_code is not None and len(response_code) > 10:
            raise ValueError("Invalid value for `response_code`, length must be less than or equal to `10`")

        self._response_code = response_code

    @property
    def avs(self):
        """
        Gets the avs of this InlineResponse20012ProcessorInformation.

        :return: The avs of this InlineResponse20012ProcessorInformation.
        :rtype: InlineResponse201ProcessorInformationAvs
        """
        return self._avs

    @avs.setter
    def avs(self, avs):
        """
        Sets the avs of this InlineResponse20012ProcessorInformation.

        :param avs: The avs of this InlineResponse20012ProcessorInformation.
        :type: InlineResponse201ProcessorInformationAvs
        """

        self._avs = avs

    @property
    def card_verification(self):
        """
        Gets the card_verification of this InlineResponse20012ProcessorInformation.

        :return: The card_verification of this InlineResponse20012ProcessorInformation.
        :rtype: InlineResponse20012ProcessorInformationCardVerification
        """
        return self._card_verification

    @card_verification.setter
    def card_verification(self, card_verification):
        """
        Sets the card_verification of this InlineResponse20012ProcessorInformation.

        :param card_verification: The card_verification of this InlineResponse20012ProcessorInformation.
        :type: InlineResponse20012ProcessorInformationCardVerification
        """

        self._card_verification = card_verification

    @property
    def ach_verification(self):
        """
        Gets the ach_verification of this InlineResponse20012ProcessorInformation.

        :return: The ach_verification of this InlineResponse20012ProcessorInformation.
        :rtype: InlineResponse20012ProcessorInformationAchVerification
        """
        return self._ach_verification

    @ach_verification.setter
    def ach_verification(self, ach_verification):
        """
        Sets the ach_verification of this InlineResponse20012ProcessorInformation.

        :param ach_verification: The ach_verification of this InlineResponse20012ProcessorInformation.
        :type: InlineResponse20012ProcessorInformationAchVerification
        """

        self._ach_verification = ach_verification

    @property
    def electronic_verification_results(self):
        """
        Gets the electronic_verification_results of this InlineResponse20012ProcessorInformation.

        :return: The electronic_verification_results of this InlineResponse20012ProcessorInformation.
        :rtype: InlineResponse20012ProcessorInformationElectronicVerificationResults
        """
        return self._electronic_verification_results

    @electronic_verification_results.setter
    def electronic_verification_results(self, electronic_verification_results):
        """
        Sets the electronic_verification_results of this InlineResponse20012ProcessorInformation.

        :param electronic_verification_results: The electronic_verification_results of this InlineResponse20012ProcessorInformation.
        :type: InlineResponse20012ProcessorInformationElectronicVerificationResults
        """

        self._electronic_verification_results = electronic_verification_results

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
        if not isinstance(other, InlineResponse20012ProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
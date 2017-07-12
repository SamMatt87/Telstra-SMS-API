# coding: utf-8

"""
    Telstra SMS Messaging API

    The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator. It also allows your application to track the delivery status of both sent and received SMS messages. 

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SendSMSRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, to=None, _from=None, validity=None, schedule_delivery=None, notify_url=None, reply_request=None, body=None):
        """
        SendSMSRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'to': 'str',
            '_from': 'str',
            'validity': 'int',
            'schedule_delivery': 'int',
            'notify_url': 'str',
            'reply_request': 'bool',
            'body': 'str'
        }

        self.attribute_map = {
            'to': 'to',
            '_from': 'from',
            'validity': 'validity',
            'schedule_delivery': 'scheduleDelivery',
            'notify_url': 'notifyURL',
            'reply_request': 'replyRequest',
            'body': 'body'
        }

        self._to = to
        self.__from = _from
        self._validity = validity
        self._schedule_delivery = schedule_delivery
        self._notify_url = notify_url
        self._reply_request = reply_request
        self._body = body

    @property
    def to(self):
        """
        Gets the to of this SendSMSRequest.
        Phone number (in E.164 format) to send the SMS to. This number can be in international format if preceeded by a ‘+’, or in national format.

        :return: The to of this SendSMSRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this SendSMSRequest.
        Phone number (in E.164 format) to send the SMS to. This number can be in international format if preceeded by a ‘+’, or in national format.

        :param to: The to of this SendSMSRequest.
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to

    @property
    def _from(self):
        """
        Gets the _from of this SendSMSRequest.
        Phone number (in E.164 format) the SMS was sent from. If not present, the serverice will use the mobile number associated with the application, or it be an Alphanumeric address of up to 11 characters.

        :return: The _from of this SendSMSRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this SendSMSRequest.
        Phone number (in E.164 format) the SMS was sent from. If not present, the serverice will use the mobile number associated with the application, or it be an Alphanumeric address of up to 11 characters.

        :param _from: The _from of this SendSMSRequest.
        :type: str
        """

        self.__from = _from

    @property
    def validity(self):
        """
        Gets the validity of this SendSMSRequest.
        How long the platform should attempt to deliver the message for. This period is specified in minutes from the message

        :return: The validity of this SendSMSRequest.
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this SendSMSRequest.
        How long the platform should attempt to deliver the message for. This period is specified in minutes from the message

        :param validity: The validity of this SendSMSRequest.
        :type: int
        """

        self._validity = validity

    @property
    def schedule_delivery(self):
        """
        Gets the schedule_delivery of this SendSMSRequest.
        How long the platform should wait before attempting to send the message - specified in minutes.

        :return: The schedule_delivery of this SendSMSRequest.
        :rtype: int
        """
        return self._schedule_delivery

    @schedule_delivery.setter
    def schedule_delivery(self, schedule_delivery):
        """
        Sets the schedule_delivery of this SendSMSRequest.
        How long the platform should wait before attempting to send the message - specified in minutes.

        :param schedule_delivery: The schedule_delivery of this SendSMSRequest.
        :type: int
        """

        self._schedule_delivery = schedule_delivery

    @property
    def notify_url(self):
        """
        Gets the notify_url of this SendSMSRequest.
        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc.

        :return: The notify_url of this SendSMSRequest.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """
        Sets the notify_url of this SendSMSRequest.
        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc.

        :param notify_url: The notify_url of this SendSMSRequest.
        :type: str
        """

        self._notify_url = notify_url

    @property
    def reply_request(self):
        """
        Gets the reply_request of this SendSMSRequest.
        If set to true, the reply message functionality will be implemented and the to address will be ignored if present. If false or not present, then normal message handling is implemented.

        :return: The reply_request of this SendSMSRequest.
        :rtype: bool
        """
        return self._reply_request

    @reply_request.setter
    def reply_request(self, reply_request):
        """
        Sets the reply_request of this SendSMSRequest.
        If set to true, the reply message functionality will be implemented and the to address will be ignored if present. If false or not present, then normal message handling is implemented.

        :param reply_request: The reply_request of this SendSMSRequest.
        :type: bool
        """

        self._reply_request = reply_request

    @property
    def body(self):
        """
        Gets the body of this SendSMSRequest.
        The text body of the message. Messages longer than 160 characters will be counted as multiple messages.

        :return: The body of this SendSMSRequest.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this SendSMSRequest.
        The text body of the message. Messages longer than 160 characters will be counted as multiple messages.

        :param body: The body of this SendSMSRequest.
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")

        self._body = body

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
        if not isinstance(other, SendSMSRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

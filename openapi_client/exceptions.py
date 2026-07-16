# coding: utf-8

# Copyright 2026 IBM Corporation
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    IBM Storage Virtualize REST API 

    The IBM Storage Virtualize Representational State Transfer (REST) model Application Programming Interface (API) consists of command targets that are used to retrieve system information and to create, modify, and delete system resources. These command targets allow command parameters to pass through unedited to the Virtualize command-line interface, which handles parsing parameter specifications for validity and error reporting. Use Hypertext Transfer Protocol Secure (HTTPS) to successfully communicate with the RESTful API server.  ***  ## Usage examples in CURL The following examples show how to use CURL for authentication and user management.  Each curl example takes the following form: >curl -L -X POST https://system_ip:7443/rest/v1/command -H header_1 -H header_2 data-raw 'JSON'  Where the following definitions apply:   * POST is the only HTTPS method that the Storage Virtualize RESTful API supports * system_ip is the IP address to which requests are sent. * v1 indicates this is version 1 of the API.  * command is the target command object (for example, auth, lseventlog or any other CLI command along with any included parameters) * Headers (header_1 ) are individually specified HTTP headers (for example, Content-Type and X-Auth-Token). * --data-raw is followed by JSON input (for example, ```'{\"name\": \"password\"}'```).  ## Authentication The HTTPS server requires authentication of a valid username and password for each API session. The /auth endpoint uses the POST method for the authentication request.  The /auth endpoint returns a JWT(JSON Web Token) authentication token that authenticates every command that a user runs. The JWT token has the token expiry encoded into it.  The following is an example of using the /auth endpoint for an authentication request. Initially, a username and password are provided through the X-Auth-Username and X-Auth-Password header fields. The initial authentication is the only instance where a username and password must be entered. Upon successfully entering the username and password, a JWT authentication token is returned. The returned token string can be decoded by using any JWT decode library freely available on the web. The X-Auth-Token header in  combination with the authentication token replaces the username and password for each  subsequent RESTful API request. Multiple tokens can be requested for a single user.  A token remains valid until its expiry time has been reached which is a user configurable option and can be set via the CLI i.e. `chsecurity`. ``` curl -k -X POST -H 'Content-Type: application/json' -H 'X-Auth-Username: superuser' -H 'X-Auth-Password: passw0rd' https://192.168.10.109:7443/rest/v1/auth ```  This yields an authentication token that can be used for all other commands. ```'{\"token\": \"<token>\"}'```  The auth endpoint has a limit of 3 requests per second for the RESTful API server. Likewise, if you have more than 4 different tokens being used per cluster, or more than  10 requests to command endpoints per second, the API will return the 429 HTTP error code.  ## Making a new user The following example shows how to create a new user, setting a password, and adding a user to a specific group. The example also demonstrates the use of the token in place of the authentication headers that are used in the authentication process: ``` curl -L -X POST '<system_ip>:7443/rest/v1/mkuser' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '{\"name\": \"testuser\", \"usergrp\": \"Service\", \"password\": \"testpassw0rd\"}' ```  ## Changing password by using the username The following example shows how to set a new user password for a user and demonstrates the use of the token in place of the authentication headers used in the authentication process: ``` curl -L -X POST '<system_ip>:7443/rest/chuser/testuser' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '{\"password\": \"newPassw0rd\"}' ```  ## Changing password using the ID The following example shows how to change a user password for a user by using the user ID. In this example, 2 is used as the user ID. ``` curl -L -X POST '<system_ip>:7443/rest/chuser/2' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '{\"password\": \"newPassw0rd\"}' ```  ## Listing all users The following example lists all user using version 1 of the API: ``` curl -L -X POST '<system_ip>:7443/rest/v1/lsuser' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '' ```  ## Listing details about a user The following example shows how to list a user in a version 1 of the API by using the user ID: ``` curl -L -X POST '<system_ip>:7443/rest/v1/lsuser/3' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '' ```  ## Removing a user The following example shows how to remove a user by using the user ID in a version 1 of the API: ``` curl -L -X POST '<system_ip>:7443/rest/v1/rmuser/2' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '' ```  ## Downloading a file The following example shows how to download a file using a directory and filename ``` curl -L -X POST '<system_ip>:7443/rest/v1/download' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json'  --data-raw '{\"prefix\": \"/targetdirectory\", \"filename\": \"filetodownload\"}' ```  *** 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Optional
from typing_extensions import Self

class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None) -> None:
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(
        self, 
        status=None, 
        reason=None, 
        http_resp=None,
        *,
        body: Optional[str] = None,
        data: Optional[Any] = None,
    ) -> None:
        self.status = status
        self.reason = reason
        self.body = body
        self.data = data
        self.headers = None

        if http_resp:
            if self.status is None:
                self.status = http_resp.status
            if self.reason is None:
                self.reason = http_resp.reason
            if self.body is None:
                try:
                    self.body = http_resp.data.decode('utf-8')
                except Exception:
                    pass
            self.headers = http_resp.getheaders()

    @classmethod
    def from_response(
        cls, 
        *, 
        http_resp, 
        body: Optional[str], 
        data: Optional[Any],
    ) -> Self:
        if http_resp.status == 400:
            raise BadRequestException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 401:
            raise UnauthorizedException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 403:
            raise ForbiddenException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 404:
            raise NotFoundException(http_resp=http_resp, body=body, data=data)

        # Added new conditions for 409 and 422
        if http_resp.status == 409:
            raise ConflictException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 422:
            raise UnprocessableEntityException(http_resp=http_resp, body=body, data=data)

        if 500 <= http_resp.status <= 599:
            raise ServiceException(http_resp=http_resp, body=body, data=data)
        raise ApiException(http_resp=http_resp, body=body, data=data)

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.data or self.body:
            error_message += "HTTP response body: {0}\n".format(self.data or self.body)

        return error_message


class BadRequestException(ApiException):
    pass


class NotFoundException(ApiException):
    pass


class UnauthorizedException(ApiException):
    pass


class ForbiddenException(ApiException):
    pass


class ServiceException(ApiException):
    pass


class ConflictException(ApiException):
    """Exception for HTTP 409 Conflict."""
    pass


class UnprocessableEntityException(ApiException):
    """Exception for HTTP 422 Unprocessable Entity."""
    pass


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result

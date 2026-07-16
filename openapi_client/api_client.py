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


import datetime
from dateutil.parser import parse
from enum import Enum
import decimal
import json
import mimetypes
import os
import re
import tempfile
import uuid
import time
import jwt
from pprint import pprint

from urllib.parse import quote
from typing import Tuple, Optional, List, Dict, Union
from pydantic import SecretStr

from openapi_client.configuration import Configuration
from openapi_client.api_response import ApiResponse, T as ApiResponseT
import openapi_client.models
from openapi_client import rest
from openapi_client.exceptions import (
    ApiValueError,
    ApiException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ServiceException
)

RequestSerialized = Tuple[str, str, Dict[str, str], Optional[str], List[str]]

ALGORITHM = 'HS512'

def update_header_params(header_name, header_value, header_params):
    '''(function) def update_header_params(
    header_name: Any,
    header_value: Any,
    header_params: Any
) -> None'''
    header_params[header_name] = header_value

def update_auth_token(configuration, new_token):
    '''(function) def update_auth_token(
    configuration: Any,
    new_token: Any
) -> None'''
    if configuration is not None:
        configuration.access_token = new_token

def get_auth_token(x_auth_username, x_auth_password, configuration=None):
    '''(function) def get_auth_token(
    x_auth_username: Any,
    x_auth_password: Any
) -> (Literal['eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3N…'] | None)'''
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.AuthenticationApi(api_client)
        try:
            api_response = api_instance.auth_post_with_http_info(x_auth_username=x_auth_username, x_auth_password=x_auth_password)
            if api_response.status_code == 200:
                new_token = json.loads(api_response.raw_data)['token']
                update_auth_token(configuration, new_token)
                return new_token
        except ApiException as e:
            print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
            return None
        
def _is_token_expired(auth_token: str) -> bool:
        """
        Verify whether the auth token is expired.
        Returns:
            bool
        Raises:
            Error: If there was an error decoding the access token.
        """
        try:
            jwt_claims = jwt.decode(auth_token.encode(),
                                    algorithms=ALGORITHM,
                                    options={
                                        'verify_signature': False,
                                        'verify_exp': False,
                                        'verify_nbf': False,
                                        'verify_iat': False,
                                        'verify_aud': False
                                    })
        except Exception as e:
            print(f"\n\n Error decoding auth token={auth_token}, error={e}\n\n")
            return False
        return jwt_claims['exp'] <= int(time.time())

def refresh_auth_token(x_auth_username, x_auth_password, configuration):
    '''(function) def refresh_auth_token(
    x_auth_username: Any,
    x_auth_password: Any
) -> (Literal['eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3N…'] | None)'''

    if configuration.access_token is not None:
        if _is_token_expired(configuration.access_token):
            print("\n Token is expired or not present, generating a new token........!!!!!\n")
        else:
            print("\n Token is still valid, reusing the existing token.\n")
            return configuration.access_token
    try:
        new_token = get_auth_token(x_auth_username, x_auth_password, configuration)
        return new_token
    except ApiException as e:
        print("Exception when calling get_auth_token: %s\n" % e)
        return None

class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int, # TODO remove as only py3 is supported?
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'decimal': decimal.Decimal,
        'object': object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None
    ) -> None:
        # use default configuration if none is provided
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value


    _default = None

    @classmethod
    def get_default(cls):
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    def param_serialize(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None, auth_settings=None,
        collection_formats=None,
        _host=None,
        _request_auth=None
    ) -> RequestSerialized:

        """Builds the HTTP request params needed by the request.
        :param method: Method to call.
        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :return: tuple of form (path, http_method, query_params, header_params,
            body, post_params, files)
        """

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params,collection_formats)
            )

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(
                path_params,
                collection_formats
            )
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(
                post_params,
                collection_formats
            )
            if files:
                post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(
            header_params,
            query_params,
            auth_settings,
            resource_path,
            method,
            body,
            request_auth=_request_auth
        )

        # body
        if body:
            body = self.sanitize_for_serialization(body)
            
        # request url
        if _host is None or self.configuration.ignore_operation_servers:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(
                query_params,
                collection_formats
            )
            url += "?" + url_query

        return method, url, header_params, body, post_params


    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ) -> rest.RESTResponse:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param url: Path to method endpoint.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param _request_timeout: timeout setting for this request.
        :return: RESTResponse
        """

        try:
            # 403 invalid token header handling for non-auth API calls if user has not given any token explicitly.
            # Check if the API call is not for auth and token is not present in header and also no existing token in configuration, then generate a new token and set in header before making the API call. This is to ensure that we always have a valid token for non-auth API calls. otherwise, if it's an auth API call or token is already present in header or existing token is present in configuration, then proceed with the API call and handle 401 response for expired token scenario.
            if 'auth' not in url and 'X-Auth-Token' not in header_params:
                # Not an auth API call, check and get auth token if token is absent. 
                # This is to ensure that we always have a valid token for non-auth API calls.
                if self.configuration.access_token is not None:
                    x_auth_token = self.configuration.access_token
                else:
                    x_auth_token = get_auth_token(self.configuration.username, self.configuration.password, self.configuration)
                
                update_header_params('X-Auth-Token', x_auth_token, header_params)

            # perform request and return response
            response_data = self.rest_client.request(
                method, url,
                headers=header_params,
                body=body, post_params=post_params,
                _request_timeout=_request_timeout
            )

            # Https status code 401 - Unauthorized
            if response_data.status == 401:
                # refresh_auth_token and retry
                print(f"\n Unauthorized access, refreshing auth token and retrying the request... \n")
                new_token = refresh_auth_token(self.configuration.username, self.configuration.password, self.configuration)
                if new_token is not None:
                    update_header_params('X-Auth-Token', new_token, header_params)
                    response_data = self.rest_client.request(
                        method, url,
                        headers=header_params,
                        body=body, post_params=post_params,
                        _request_timeout=_request_timeout
                    )

            # Https Code 429 - Too Many Requests
            if response_data.status == 429:
                print(f"\n Too many requests, refreshing auth token and retrying the request after some time... \n")
                # We can retry 5 times.. each with increasing delay..
                for retry_count in range(1,6):    
                    time.sleep(retry_count) # Sleep for retry_count seconds before retrying
                    response_data = self.rest_client.request(
                        method, url,
                        headers=header_params,
                        body=body, post_params=post_params,
                        _request_timeout=_request_timeout
                    )
                    if response_data.status != 429:
                        break
        
            # Https status code 308 - Permanent Redirect
            if response_data.status == 308:
            # redirect with new URL with same cred. ( Username/ password if auth req else for other APIs ?)
                redirect_location = response_data.getheader('Location')
                print(f"\n Redirect location from header: {redirect_location} \n")
                if response_data.status == 308 and redirect_location is not None:
                    print(f"\n Redirecting to new location: {redirect_location} \n")
                    self.configuration.host = redirect_location #should be like https://<IP>:7443/rest/v1
                    # Refresh the auth token
                    new_token = get_auth_token(self.configuration.username, self.configuration.password, self.configuration)
                    if new_token is not None:
                        update_header_params('X-Auth-Token', new_token, header_params)
                    response_data = self.rest_client.request(
                        method, redirect_location,
                        headers=header_params,
                        body=body, post_params=post_params,
                        _request_timeout=_request_timeout
                    )

        except ApiException as e:
            raise e

        return response_data

    def response_deserialize(
        self,
        response_data: rest.RESTResponse,
        response_types_map: Optional[Dict[str, ApiResponseT]]=None
    ) -> ApiResponse[ApiResponseT]:
        """Deserializes response into an object.
        :param response_data: RESTResponse object to be deserialized.
        :param response_types_map: dict of response types.
        :return: ApiResponse
        """

        msg = "RESTResponse.read() must be called before passing it to response_deserialize()"
        assert response_data.data is not None, msg

        response_type = response_types_map.get(str(response_data.status), None)
        if not response_type and isinstance(response_data.status, int) and 100 <= response_data.status <= 599:
            # if not found, look for '1XX', '2XX', etc.
            response_type = response_types_map.get(str(response_data.status)[0] + "XX", None)

        # deserialize response data
        response_text = None
        return_data = None
        try:
            if response_type == "bytearray":
                return_data = response_data.data
            elif response_type == "file":
                return_data = self.__deserialize_file(response_data)
            elif response_type is not None:
                match = None
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
                encoding = match.group(1) if match else "utf-8"
                response_text = response_data.data.decode(encoding)
                return_data = self.deserialize(response_text, response_type, content_type)
        finally:
            if not 200 <= response_data.status <= 299:
                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )

        return ApiResponse(
            status_code = response_data.status,
            data = return_data,
            headers = response_data.getheaders(),
            raw_data = response_data.data
        )

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is SecretStr, return obj.get_secret_value()
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is decimal.Decimal return string representation.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, SecretStr):
            return obj.get_secret_value()
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, list):
            return [
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            ]
        elif isinstance(obj, tuple):
            return tuple(
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            )
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return str(obj)

        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                obj_dict = obj.to_dict()
            else:
                obj_dict = obj.__dict__

        if isinstance(obj_dict, list):
            # here we handle instances that can either be a list or something else, and only became a real list by calling to_dict()
            return self.sanitize_for_serialization(obj_dict)

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in obj_dict.items()
        }

    def deserialize(self, response_text: str, response_type: str, content_type: Optional[str]):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :param content_type: content type of response.

        :return: deserialized object.
        """

        # fetch data from response object
        if content_type is None:
            try:
                data = json.loads(response_text)
            except ValueError:
                data = response_text
        elif re.match(r'^application/(json|[\w!#$&.+\-^_]+\+json)\s*(;|$)', content_type, re.IGNORECASE):
            if response_text == "":
                data = ""
            else:
                data = json.loads(response_text)
        elif re.match(r'^text\/[a-z.+-]+\s*(;|$)', content_type, re.IGNORECASE):
            data = response_text
        else:
            raise ApiException(
                status=0,
                reason="Unsupported content type: {0}".format(content_type)
            )

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith('List['):
                m = re.match(r'List\[(.*)]', klass)
                assert m is not None, "Malformed List type definition"
                sub_kls = m.group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('Dict['):
                m = re.match(r'Dict\[([^,]*), (.*)]', klass)
                assert m is not None, "Malformed Dict type definition"
                sub_kls = m.group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in data.items()}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(openapi_client.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass is object:
            return self.__deserialize_object(data)
        elif klass is datetime.date:
            return self.__deserialize_date(data)
        elif klass is datetime.datetime:
            return self.__deserialize_datetime(data)
        elif klass is decimal.Decimal:
            return decimal.Decimal(data)
        elif issubclass(klass, Enum):
            return self.__deserialize_enum(data, klass)
        else:
            return self.__deserialize_model(data, klass)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, quote(str(value))) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(map(str, item)) for item in new_params])

    def files_parameters(
        self,
        files: Dict[str, Union[str, bytes, List[str], List[bytes], Tuple[str, bytes]]],
    ):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []
        for k, v in files.items():
            if isinstance(v, str):
                with open(v, 'rb') as f:
                    filename = os.path.basename(f.name)
                    filedata = f.read()
            elif isinstance(v, bytes):
                filename = k
                filedata = v
            elif isinstance(v, tuple):
                filename, filedata = v
            elif isinstance(v, list):
                for file_param in v:
                    params.extend(self.files_parameters({k: file_param}))
                continue
            else:
                raise ValueError("Unsupported file value")
            mimetype = (
                mimetypes.guess_type(filename)[0]
                or 'application/octet-stream'
            )
            params.append(
                tuple([k, tuple([filename, filedata, mimetype])])
            )
        return params

    def select_header_accept(self, accepts: List[str]) -> Optional[str]:
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth=None
    ) -> None:
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param request_auth: if set, the provided settings will
                             override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(
                headers,
                queries,
                resource_path,
                method,
                body,
                request_auth
            )
        else:
            for auth in auth_settings:
                auth_setting = self.configuration.auth_settings().get(auth)
                if auth_setting:
                    self._apply_auth_params(
                        headers,
                        queries,
                        resource_path,
                        method,
                        body,
                        auth_setting
                    )

    def _apply_auth_params(
        self,
        headers,
        queries,
        resource_path,
        method,
        body,
        auth_setting
    ) -> None:
        """Updates the request parameters based on a single auth_setting

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param auth_setting: auth settings for the endpoint
        """
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        handle file downloading
        save response body into a tmp file and return the instance

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            m = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                content_disposition
            )
            assert m is not None, "Unexpected 'content-disposition' header value"
            filename = m.group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_enum(self, data, klass):
        """Deserializes primitive type to enum.

        :param data: primitive type.
        :param klass: class literal.
        :return: enum value.
        """
        try:
            return klass(data)
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as `{1}`"
                    .format(data, klass)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return klass.from_dict(data)

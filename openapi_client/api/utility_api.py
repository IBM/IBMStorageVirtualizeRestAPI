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

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictStr
from typing import Any, Optional
from openapi_client.models.svc_livedump_post_request import SvcLivedumpPostRequest
from openapi_client.models.svc_snap_post_request import SvcSnapPostRequest
from openapi_client.models.svcsearch_post_request import SvcsearchPostRequest
from openapi_client.models.svcupgradetest_post_request import SvcupgradetestPostRequest

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class UtilityApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def svc_livedump_post(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svc_livedump_post_request: Optional[SvcLivedumpPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """svc_livedump_post

        Runs svc_livedump 

        :param x_auth_token:
        :type x_auth_token: str
        :param svc_livedump_post_request:
        :type svc_livedump_post_request: SvcLivedumpPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svc_livedump_post_serialize(
            x_auth_token=x_auth_token,
            svc_livedump_post_request=svc_livedump_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def svc_livedump_post_with_http_info(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svc_livedump_post_request: Optional[SvcLivedumpPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """svc_livedump_post

        Runs svc_livedump 

        :param x_auth_token:
        :type x_auth_token: str
        :param svc_livedump_post_request:
        :type svc_livedump_post_request: SvcLivedumpPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svc_livedump_post_serialize(
            x_auth_token=x_auth_token,
            svc_livedump_post_request=svc_livedump_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def svc_livedump_post_without_preload_content(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svc_livedump_post_request: Optional[SvcLivedumpPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """svc_livedump_post

        Runs svc_livedump 

        :param x_auth_token:
        :type x_auth_token: str
        :param svc_livedump_post_request:
        :type svc_livedump_post_request: SvcLivedumpPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svc_livedump_post_serialize(
            x_auth_token=x_auth_token,
            svc_livedump_post_request=svc_livedump_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _svc_livedump_post_serialize(
        self,
        x_auth_token,
        svc_livedump_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_auth_token is not None:
            _header_params['X-Auth-Token'] = x_auth_token
        # process the form parameters
        # process the body parameter
        if svc_livedump_post_request is not None:
            _body_params = svc_livedump_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'text/html'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/svc_livedump',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def svc_snap_post(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svc_snap_post_request: Optional[SvcSnapPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """svc_snap_post

        Runs svc_snap.  Apart from `upload` and `pmr` only a single parameter can be specified. To combine multiple parameters, use the pre-defined `gui1`, `gui2` or `gui3` options, or specify a concatenation of multiple short parameters prefixed with x, for example: `{ \"xsa\": true }` for stats and dumpall.  ``` Option            Comment ------------------------------- gui1              stats gui2              stats dump gui3              stats dumpall fcm   Long              Short ------------------------- stats             s ups               u dump              d dumpall           a dumpenc           e noimm             n fcm               f anomalystats      t ``` 

        :param x_auth_token:
        :type x_auth_token: str
        :param svc_snap_post_request:
        :type svc_snap_post_request: SvcSnapPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svc_snap_post_serialize(
            x_auth_token=x_auth_token,
            svc_snap_post_request=svc_snap_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def svc_snap_post_with_http_info(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svc_snap_post_request: Optional[SvcSnapPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """svc_snap_post

        Runs svc_snap.  Apart from `upload` and `pmr` only a single parameter can be specified. To combine multiple parameters, use the pre-defined `gui1`, `gui2` or `gui3` options, or specify a concatenation of multiple short parameters prefixed with x, for example: `{ \"xsa\": true }` for stats and dumpall.  ``` Option            Comment ------------------------------- gui1              stats gui2              stats dump gui3              stats dumpall fcm   Long              Short ------------------------- stats             s ups               u dump              d dumpall           a dumpenc           e noimm             n fcm               f anomalystats      t ``` 

        :param x_auth_token:
        :type x_auth_token: str
        :param svc_snap_post_request:
        :type svc_snap_post_request: SvcSnapPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svc_snap_post_serialize(
            x_auth_token=x_auth_token,
            svc_snap_post_request=svc_snap_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def svc_snap_post_without_preload_content(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svc_snap_post_request: Optional[SvcSnapPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """svc_snap_post

        Runs svc_snap.  Apart from `upload` and `pmr` only a single parameter can be specified. To combine multiple parameters, use the pre-defined `gui1`, `gui2` or `gui3` options, or specify a concatenation of multiple short parameters prefixed with x, for example: `{ \"xsa\": true }` for stats and dumpall.  ``` Option            Comment ------------------------------- gui1              stats gui2              stats dump gui3              stats dumpall fcm   Long              Short ------------------------- stats             s ups               u dump              d dumpall           a dumpenc           e noimm             n fcm               f anomalystats      t ``` 

        :param x_auth_token:
        :type x_auth_token: str
        :param svc_snap_post_request:
        :type svc_snap_post_request: SvcSnapPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svc_snap_post_serialize(
            x_auth_token=x_auth_token,
            svc_snap_post_request=svc_snap_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _svc_snap_post_serialize(
        self,
        x_auth_token,
        svc_snap_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_auth_token is not None:
            _header_params['X-Auth-Token'] = x_auth_token
        # process the form parameters
        # process the body parameter
        if svc_snap_post_request is not None:
            _body_params = svc_snap_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'text/html'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/svc_snap',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def svcsearch_post(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svcsearch_post_request: Optional[SvcsearchPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """svcsearch_post

        Runs svcsearch to find objects matching a string.

        :param x_auth_token:
        :type x_auth_token: str
        :param svcsearch_post_request:
        :type svcsearch_post_request: SvcsearchPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svcsearch_post_serialize(
            x_auth_token=x_auth_token,
            svcsearch_post_request=svcsearch_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def svcsearch_post_with_http_info(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svcsearch_post_request: Optional[SvcsearchPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """svcsearch_post

        Runs svcsearch to find objects matching a string.

        :param x_auth_token:
        :type x_auth_token: str
        :param svcsearch_post_request:
        :type svcsearch_post_request: SvcsearchPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svcsearch_post_serialize(
            x_auth_token=x_auth_token,
            svcsearch_post_request=svcsearch_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def svcsearch_post_without_preload_content(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svcsearch_post_request: Optional[SvcsearchPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """svcsearch_post

        Runs svcsearch to find objects matching a string.

        :param x_auth_token:
        :type x_auth_token: str
        :param svcsearch_post_request:
        :type svcsearch_post_request: SvcsearchPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svcsearch_post_serialize(
            x_auth_token=x_auth_token,
            svcsearch_post_request=svcsearch_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _svcsearch_post_serialize(
        self,
        x_auth_token,
        svcsearch_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_auth_token is not None:
            _header_params['X-Auth-Token'] = x_auth_token
        # process the form parameters
        # process the body parameter
        if svcsearch_post_request is not None:
            _body_params = svcsearch_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'text/html'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/svcsearch',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def svcupgradetest_post(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svcupgradetest_post_request: Optional[SvcupgradetestPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """svcupgradetest_post

        Runs the Upgrade Test Utility 

        :param x_auth_token:
        :type x_auth_token: str
        :param svcupgradetest_post_request:
        :type svcupgradetest_post_request: SvcupgradetestPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svcupgradetest_post_serialize(
            x_auth_token=x_auth_token,
            svcupgradetest_post_request=svcupgradetest_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def svcupgradetest_post_with_http_info(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svcupgradetest_post_request: Optional[SvcupgradetestPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """svcupgradetest_post

        Runs the Upgrade Test Utility 

        :param x_auth_token:
        :type x_auth_token: str
        :param svcupgradetest_post_request:
        :type svcupgradetest_post_request: SvcupgradetestPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svcupgradetest_post_serialize(
            x_auth_token=x_auth_token,
            svcupgradetest_post_request=svcupgradetest_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def svcupgradetest_post_without_preload_content(
        self,
        x_auth_token: Optional[StrictStr] = None,
        svcupgradetest_post_request: Optional[SvcupgradetestPostRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """svcupgradetest_post

        Runs the Upgrade Test Utility 

        :param x_auth_token:
        :type x_auth_token: str
        :param svcupgradetest_post_request:
        :type svcupgradetest_post_request: SvcupgradetestPostRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svcupgradetest_post_serialize(
            x_auth_token=x_auth_token,
            svcupgradetest_post_request=svcupgradetest_post_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _svcupgradetest_post_serialize(
        self,
        x_auth_token,
        svcupgradetest_post_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_auth_token is not None:
            _header_params['X-Auth-Token'] = x_auth_token
        # process the form parameters
        # process the body parameter
        if svcupgradetest_post_request is not None:
            _body_params = svcupgradetest_post_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'text/html'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/svcupgradetest',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def svqueryclock_post(
        self,
        x_auth_token: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """svqueryclock_post

        Runs svqueryclock to get the current cluster time. 

        :param x_auth_token:
        :type x_auth_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svqueryclock_post_serialize(
            x_auth_token=x_auth_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def svqueryclock_post_with_http_info(
        self,
        x_auth_token: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """svqueryclock_post

        Runs svqueryclock to get the current cluster time. 

        :param x_auth_token:
        :type x_auth_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svqueryclock_post_serialize(
            x_auth_token=x_auth_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def svqueryclock_post_without_preload_content(
        self,
        x_auth_token: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """svqueryclock_post

        Runs svqueryclock to get the current cluster time. 

        :param x_auth_token:
        :type x_auth_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._svqueryclock_post_serialize(
            x_auth_token=x_auth_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _svqueryclock_post_serialize(
        self,
        x_auth_token,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_auth_token is not None:
            _header_params['X-Auth-Token'] = x_auth_token
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'text/html'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/svqueryclock',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



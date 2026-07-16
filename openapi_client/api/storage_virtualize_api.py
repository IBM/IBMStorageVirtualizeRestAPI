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

from openapi_client import Configuration, ApiException
from openapi_client.api.authentication_api import AuthenticationApi
from openapi_client.api.svc_info_api import SVCInfoApi
from openapi_client.api.svc_task_api import SVCTaskApi
from openapi_client.api.utility_api import UtilityApi
from openapi_client.api.download_api import DownloadApi
from openapi_client import ApiClient as api_client
import json
import urllib3
from typing import Optional

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class StorageVirtualizeAPI:
    """
    Provides a utility class to manage and interact with various APIs, such as authentication, 
    service information, tasks, utilities, and downloads. This class initializes and configures 
    the required API clients using the provided connection details.
    
    Notes:
    - The constructor obtains an access token via AuthenticationApi and sets Configuration.access_token.
    - The generated API classes (AuthenticationApi, SVCInfoApi, DownloadApi, etc.) implement context managers.
      If you create long-lived clients, prefer reusing HTTP client and disposing when your application shuts down.
    """
    
    def __init__(self, ip_address: str, username_or_token: str, password: Optional[str] = None):
        """
        Initialize the StorageVirtualizeAPI with either username/password or access token.
        
        Args:
            ip_address: The IP address of the server
            username_or_token: Username (if password provided) or access token (if password is None)
            password: Password for authentication (optional, if None then username_or_token is treated as token)
        """
        baseurl = f"https://{ip_address}:7443/rest/v1"
        config = Configuration()
        config.host = baseurl
        
        if password is not None:
            # Constructor with username and password
            config.username = username_or_token
            config.password = password
            
            # Initialize AuthenticationApi first
            self._authentication_api = AuthenticationApi(api_client(config))
            try:
                # Get access token
                config.access_token = self._get_auth_token(username_or_token, password)
            except ApiException as ex:
                raise ApiException(f"Failed to authenticate: {ex.reason} (status {ex.status})") from ex
        else:
            # Constructor with access token
            config.access_token = username_or_token
            
            # Initialize AuthenticationApi
            self._authentication_api = AuthenticationApi(api_client(config))
        
        if config.access_token is not None:
            # Initialize all API clients with the configured config
            self._svc_info_api = SVCInfoApi(api_client(config))
            self._svc_task_api = SVCTaskApi(api_client(config))
            self._utility_api = UtilityApi(api_client(config))
            self._download_api = DownloadApi(api_client(config))
        else:
            raise ApiException("Authentication failed: No access token obtained.")
    
    @property
    def authentication_api(self) -> AuthenticationApi:
        """Get the AuthenticationApi instance."""
        return self._authentication_api
    
    @property
    def svc_info_api(self) -> SVCInfoApi:
        """Get the SVCInfoApi instance."""
        return self._svc_info_api
    
    @property
    def svc_task_api(self) -> SVCTaskApi:
        """Get the SVCTaskApi instance."""
        return self._svc_task_api
    
    @property
    def utility_api(self) -> UtilityApi:
        """Get the UtilityApi instance."""
        return self._utility_api
    
    @property
    def download_api(self) -> DownloadApi:
        """Get the DownloadApi instance."""
        return self._download_api
    
    def _get_auth_token(self, username: str, password: str) -> str:
        """
        Private method to retrieve authentication token.
        
        Args:
            username: Username for authentication
            password: Password for authentication
            
        Returns:
            The authentication token string
        """
        try:
            response = self._authentication_api.auth_post_with_http_info(username, password)
            token_data = response.raw_data if hasattr(response, 'raw_data') else response.data
            
            # Parse the response to extract token
            if isinstance(token_data, str):
                doc = json.loads(token_data)
            elif isinstance(token_data, bytes):
                doc = json.loads(token_data.decode('utf-8'))
            else:
                doc = token_data

            try:
                token = doc.get("token") if isinstance(doc, dict) else doc["token"]
            except (KeyError, TypeError):
                token = None

            return token
        except ApiException as e:
            print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
            return None


"""
 Detailed usage examples (copy into your application code).  Adjust model types and fields
 to your generated SDK version. These examples are intentionally verbose to show common patterns.
 
 -- 1) Simple synchronous usage (small scripts / diagnostics)
 
 # Instantiate (constructor already fetches an access token and sets config.access_token)
 svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
 
 # Call an SVCInfo API (simple form). Many endpoints return an Ok response model in this SDK.
 try:
     # If endpoint accepts a request model, construct it; otherwise call parameterless overloads.
     lsarray_result = svc.svc_info_api.lsarray_post(x_auth_token=None, lsarray_post_request=None)
     # Inspect returned model (lsarray_result) for command output / status.
 except ApiException as ex:
     # ApiException contains status code, response headers and response content in many SDKs.
     print(f"API error: {ex.reason} (status {ex.status})", file=sys.stderr)
 
 -- 2) Using ApiResponse to inspect status, headers and raw content
 
 response = svc.svc_info_api.lsarray_post_with_http_info(x_auth_token=None, lsarray_post_request=None)
 status_code = response.status_code                 # HTTP status
 headers = response.headers                         # response headers
 data = response.data                               # deserialized Ok response model (if successful)
 raw = response.raw_data                            # raw response text (useful for debugging)
 
 -- 3) Async usage with asyncio
 
 import asyncio
 
 async def async_example():
     # Note: Check if your generated client supports async operations
     # If not, you can use asyncio.to_thread for blocking calls
     try:
         async_result = await asyncio.to_thread(
             svc.authentication_api.auth_post, "admin", "password"
         )
         # When using async methods that return models, inspect the returned object directly.
     except ApiException as api_ex:
         print(f"Async API error: {api_ex.reason}", file=sys.stderr)
 
 asyncio.run(async_example())
 
 -- 4) Download example (writing content to disk if the endpoint returns file bytes)
 
 # Build the request model expected by the Download API (DownloadPostRequest is generated).
 download_request = {
     # populate required properties, e.g. "path": "/var/logs/somefile"
 }
 
 try:
     download_response = svc.download_api.download_post_with_http_info(download_request, x_auth_token=None)
     # Many generated SDKs return an Ok response model; if the endpoint returns file data instead,
     # check download_response.raw_data or the HTTP response body via ApiResponse plumbing.
     raw_content = download_response.raw_data
     if raw_content:
         # Example: write raw response to a file
         with open("downloaded.raw", "wb") as f:
             if isinstance(raw_content, str):
                 f.write(raw_content.encode('utf-8'))
             elif isinstance(raw_content, bytes):
                 f.write(raw_content)
             else:
                 f.write(str(raw_content).encode('utf-8'))
 except ApiException as ex:
     print(f"Download failed: {ex.reason}", file=sys.stderr)
 
 -- 5) Getting a token explicitly (alternative to constructor behavior)
 
 # You can obtain a token manually and pass it to calls that accept x_auth_token:
 auth_resp = svc.authentication_api.auth_post_with_http_info("admin", "password")
 # auth_resp.raw_data contains JSON like { "token": "..." } — parse if needed.
 # Then call another endpoint with the explicit token:
 token_data = auth_resp.raw_data if hasattr(auth_resp, 'raw_data') else auth_resp.data
 if isinstance(token_data, str):
     token_dict = json.loads(token_data)
 else:
     token_dict = token_data
 token = token_dict.get("token")
 result_using_token = svc.svc_info_api.lsarray_post(x_auth_token=token, lsarray_post_request=None)
 
 -- 6) Best practices and notes
 
 - Reuse HTTP client and session instead of creating many instances in production. The generated constructors
   that accept configuration make that possible; this utility currently uses the default client per API.
 - Protect credentials: do not hard-code plaintext passwords in real apps; use secure storage or environment variables.
 - Validate server certificates in production: the sample code disables server certificate validation for convenience.
 - Use context managers (with statements) for API classes when finished to release resources if they support it.
 - Check ApiResponse.status_code / ApiException to implement retry logic or inspect error details.
 
 These examples are commentary only and intentionally placed here as reference. Move them into your application codebase
 (for example a small helper class or integration tests) and adapt to your models and runtime requirements.
"""

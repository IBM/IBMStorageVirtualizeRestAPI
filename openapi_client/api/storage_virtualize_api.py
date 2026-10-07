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
from openapi_client.models.lsvdisk_post_request import LsvdiskPostRequest
from openapi_client.models.lsvdisk_id_post_request import LsvdiskIdPostRequest
from openapi_client.models.mkvdisk_post_request import MkvdiskPostRequest
from openapi_client.models.rmvdisk_id_post_request import RmvdiskIdPostRequest
import json
import urllib3
from typing import Any, Dict, List, Optional, Union

# ---------------------------------------------------------------------------
# Capacity string → bytes converter
# ---------------------------------------------------------------------------
_CAPACITY_UNITS = {
    'b':   1,
    'kb':  1024,
    'mb':  1024 ** 2,
    'gb':  1024 ** 3,
    'tb':  1024 ** 4,
    'pb':  1024 ** 5,
}

def _capacity_to_bytes(value: str) -> str:
    """
    Convert a human-readable capacity string (e.g. ``"10.00GB"``) to an
    integer byte count expressed as a decimal string, which matches what the
    SSH CLI returns when ``-bytes`` is given.

    If the input is already a plain integer string it is returned as-is.
    """
    if not value:
        return value
    v = value.strip()
    # Already numeric (SSH -bytes output)?
    if v.isdigit():
        return v
    # Find where the digits end and the unit begins
    i = 0
    while i < len(v) and (v[i].isdigit() or v[i] == '.'):
        i += 1
    if i == 0:
        return v  # no leading digit; return unchanged
    num_part = v[:i]
    unit_part = v[i:].strip().lower()
    mult = _CAPACITY_UNITS.get(unit_part, 1)
    try:
        return str(int(float(num_part) * mult))
    except ValueError:
        return v


def _normalise_vdisk(item: dict) -> dict:
    """
    Convert the capacity fields in a single vdisk dict from human-readable
    strings (``"10.00GB"``) to integer byte strings so that the mediator's
    ``int(cli_volume.capacity)`` calls work correctly.
    """
    for key in ('capacity', 'used_capacity', 'real_capacity', 'free_capacity'):
        if key in item and item[key]:
            item[key] = _capacity_to_bytes(str(item[key]))
    return item


def _merge_lsvdisk_id_response(raw_list: list) -> dict:
    """
    The ``lsvdisk/{id}`` REST endpoint always returns a two-element list:
      [0]  vdisk-level detail (76 fields, e.g. capacity, vdisk_UID, FC_id …)
      [1]  copy-level detail  (31 fields, e.g. se_copy, compressed_copy …)

    Merge them into one flat dict so the mediator can access all fields on a
    single object without knowing about the two-part structure.
    Copy-level fields do **not** overwrite vdisk-level fields with the same name.
    """
    if not raw_list:
        return {}
    detail = dict(raw_list[0]) if raw_list[0] else {}
    if len(raw_list) > 1 and raw_list[1]:
        copy = raw_list[1]
        for k, v in copy.items():
            if k not in detail or detail[k] is None:
                detail[k] = v
    return _normalise_vdisk(detail)

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
    
    def __init__(self, ip_address: str, username_or_token: str, password: Optional[str] = None,
                 verify_ssl: bool = True):
        """
        Initialize the StorageVirtualizeAPI with either username/password or access token.

        Args:
            ip_address: The IP address of the server
            username_or_token: Username (if password provided) or access token (if password is None)
            password: Password for authentication (optional, if None then username_or_token is treated as token)
            verify_ssl: Whether to verify the server's SSL certificate (default True).
                        Set to False only when the array uses a self-signed certificate and
                        no CA bundle is available.
        """
        baseurl = f"https://{ip_address}:7443/rest/v1"
        config = Configuration()
        config.host = baseurl
        config.verify_ssl = verify_ssl

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
    
    def lsvdisk(self, filtervalue: Optional[str] = None,
                object_id: Optional[str] = None) -> Any:
        """
        List virtual disks via REST.

        Args:
            filtervalue: Optional filter string (e.g. ``"vdisk_UID=<uid>"``).
            object_id:   If provided, fetch the single vdisk with this exact
                         name / id / uid.  Uses the list endpoint with a
                         ``name=`` filter when the value looks like a name, and
                         the ``lsvdisk/{id}`` endpoint (which returns the merged
                         detail+copy view) for numeric IDs.

        Returns:
            * A single merged ``dict`` when *object_id* is given.
            * A ``list`` of normalised ``dict`` items when listing / filtering.
        """
        if object_id is not None:
            obj = str(object_id)
            # The lsvdisk/{id} endpoint accepts id, name, or uid and always
            # returns a two-element list [detail_view, copy_view] which we
            # merge into a single flat dict with all fields the mediator needs.
            req = LsvdiskIdPostRequest(bytes=True)
            raw = self._svc_info_api.lsvdisk_id_post(
                id=obj, lsvdisk_id_post_request=req)
            raw_list = json.loads(raw) if isinstance(raw, str) else raw
            if not isinstance(raw_list, list):
                raw_list = [raw_list] if raw_list else []
            if not raw_list or raw_list[0] is None:
                return None
            return _merge_lsvdisk_id_response(raw_list)

        # --- list all / filter ---
        fv_param = filtervalue or None
        req = LsvdiskPostRequest(bytes=True, filtervalue=fv_param) \
            if fv_param else LsvdiskPostRequest(bytes=True)
        raw = self._svc_info_api.lsvdisk_post(lsvdisk_post_request=req)
        items = json.loads(raw) if isinstance(raw, str) else raw
        if not isinstance(items, list):
            items = [items] if items else []
        return [_normalise_vdisk(dict(it)) for it in items]

    def mkvdisk(self, name: str, mdiskgrp: str, size: int, unit: str = 'b',
                iogrp: Optional[str] = None,
                rsize: Optional[str] = None,
                compressed: Optional[bool] = None,
                deduplicated: Optional[bool] = None) -> Any:
        """
        Create a virtual disk via REST.

        Args:
            name:        Name for the new vdisk.
            mdiskgrp:    Storage pool name or id.
            size:        Size of the vdisk.
            unit:        Size unit (``'b'``, ``'kb'``, ``'mb'``, ``'gb'``, ``'tb'``).
            iogrp:       Optional I/O group name or id.
            rsize:       Optional thin-provisioning reserve (e.g. ``"2%"``).
            compressed:  ``True`` to enable compression.
            deduplicated: ``True`` to enable deduplication.

        Returns:
            The API response object for the create operation.
        """
        request = MkvdiskPostRequest(
            name=name,
            mdiskgrp=mdiskgrp,
            size=size,
            unit=unit,
            iogrp=iogrp,
            rsize=rsize,
            compressed=compressed,
            deduplicated=deduplicated,
        )
        return self._svc_task_api.mkvdisk_post(mkvdisk_post_request=request)

    def rmvdisk(self, vdisk_id: str, force: bool = False) -> Any:
        """
        Delete a virtual disk via REST.

        Args:
            vdisk_id: The id, name, or uid of the vdisk to delete.
            force:    Pass ``True`` to force deletion even when dependencies exist.

        Returns:
            The API response object for the delete operation.
        """
        request = RmvdiskIdPostRequest(force=force) if force \
            else RmvdiskIdPostRequest()
        return self._svc_task_api.rmvdisk_id_post(
            id=str(vdisk_id),
            rmvdisk_id_post_request=request,
        )

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

# IBM Spectrum Virtualize REST API Python Client

## Overview
This repo contains a Python SDK for interacting with the IBM Storage Virtualize REST API.

## Install
1. Ensure Python 3.9+
2. Install dependencies (if any) using pip:
```bash
pip install -r requirements.txt
```
3. Install SDK using pip:
```bash
pip install ibm-svc-rest-client
```

or Manual Installation:
```bash
git clone https://github.com/IBM/IBMStorageVirtualizeRestAPI.git
cd IBMStorageVirtualizeRestAPI
pip install .
```

## Usage
## Detailed usage examples (copy into your application code).  Adjust model types and fields to your generated SDK version. These examples are intentionally verbose to show common patterns.
```python
from openapi_client.api.storage_virtualize_api import StorageVirtualizeAPI
from openapi_client.rest import ApiException
from pprint import pprint  
import sys

# Instantiate (constructor already fetches an access token and sets config.access_token)
try:
    svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
    print("Successfully authenticated and instantiated StorageVirtualizeAPI client.")
    try:
        lsarray_result = svc.svc_info_api.lsarray_post(x_auth_token=None, lsarray_post_request=None)
        # Inspect returned model (lsarray_result) for command output / status.
        pprint(lsarray_result)
    except ApiException as ex:
        # ApiException contains status code, response headers and response content in many SDKs.
        print(f"API error: {ex.reason} (status {ex.status})", file=sys.stderr)
except ApiException as ex:
    print(f"API error: {ex.reason} (status {ex.status})", file=sys.stderr)


```

## Documentation

For detailed documentation, refer https://github.com/IBM/IBMStorageVirtualizeRestAPI/blob/main/IBM_REST_SDK_USAGE_GUIDE.md

## Configuration
- `base_url`: API endpoint
- `api_key`: authentication token
- other settings are usually in `StorageVirtualizeAPI` constructor or config file

## Notes
- Check the wrapper methods in `storage_virtualize_api.py` for available API calls.
- Handle errors/exceptions as needed.

## Best practices

- Reuse HTTP client and session instead of creating many instances in production. The generated constructors
   that accept configuration make that possible; this utility currently uses the default client per API.
- Protect credentials: do not hard-code plaintext passwords in real apps; use secure storage or environment variables.
- Use context managers (with statements) for API classes when finished to release resources if they support it.
- Check ApiResponse.status_code / ApiException to inspect error details.

These examples are commentary only and intentionally placed here as reference. Move them into your application codebase
(for example a small helper class or integration tests) and adapt to your models and runtime requirements.

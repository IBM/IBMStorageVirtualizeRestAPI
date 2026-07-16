# IBM Storage Virtualize REST API - Python SDK Customer Guide

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [Core Concepts](#core-concepts)
- [Common Operations](#common-operations)
- [Advanced Usage](#advanced-usage)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Conclusion](#conclusion)

---

## Introduction

The IBM Storage Virtualize REST API Python SDK provides a comprehensive, easy-to-use interface for managing IBM Storage Virtualize systems programmatically. This SDK enables you to automate storage operations, monitor system health, and integrate storage management into your applications.

### Key Features

- **Simplified Authentication:** Automatic JWT token management with built-in refresh
- **Complete API Coverage:** Access to all Storage Virtualize REST API endpoints
- **Type Safety:** Full type hints and Pydantic models for validation
- **Error Handling:** Comprehensive exception handling with detailed error messages
- **Connection Management:** Built-in connection pooling and retry logic
- **SSL/TLS Support:** Secure communication with certificate validation

### What You Can Do

- Manage virtual disks (vdisks), volumes, and storage pools
- Configure hosts, host clusters, and mappings
- Monitor system health and performance
- Manage snapshots and replication
- Configure storage policies and QoS
- Download logs and diagnostic files
- Automate routine storage operations

---

## Getting Started

### Prerequisites

- **Python:** Version 3.9 or higher
- **Network Access:** HTTPS connectivity to your Storage Virtualize system (port 7443)
- **Credentials:** Valid username and password with appropriate permissions
- **System Requirements:** IBM Storage Virtualize 9.1.3.0 system with REST API enabled

### Installation

#### Quick Install (Recommended)

```bash
pip install ibm_svc_rest_client-1.0.0-py3-none-any.whl
```

#### Install from Source

```bash
git clone https://github.com/IBM/IBMStorageVirtualizeRestAPI.git
cd IBMStorageVirtualizeRestAPI
pip install .
```

#### Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv storage_env

# Activate virtual environment
source storage_env/bin/activate  # On Windows: storage_env\Scripts\activate

# Install SDK
pip install ibm_svc_rest_client-1.0.0-py3-none-any.whl
```

### Verify Installation

```python
import openapi_client

print(f"SDK Version: {openapi_client.__version__}")
```

### Your First API Call

```python
from openapi_client.api.storage_virtualize_api import StorageVirtualizeAPI
from openapi_client.rest import ApiException

# Connect to your storage system
try:
    svc = StorageVirtualizeAPI(
        ip_address="10.0.0.1",
        username_or_token="admin",
        password="your_password"
    )
    print("✓ Successfully connected!")

    # List all arrays
    arrays = svc.svc_info_api.lsarray_post()
    print(f"Found {len(arrays)} array(s)")
except ApiException as e:
    print(f"Error: {e.reason} (HTTP {e.status})")
```

---

## Authentication

### Understanding JWT Tokens

The SDK uses JWT (JSON Web Token) authentication. When you initialize the `StorageVirtualizeAPI` class, it automatically:

- Authenticates with your credentials
- Obtains a JWT token
- Uses the token for all subsequent API calls
- Handles token refresh when needed

### Authentication Methods

#### Method 1: Username and Password (Recommended)

```python
from openapi_client.api.storage_virtualize_api import StorageVirtualizeAPI

svc = StorageVirtualizeAPI(
    ip_address="10.0.0.1",
    username_or_token="admin",
    password="your_password"
)
```

#### Method 2: Pre-existing Token

If you already have a valid token:

```python
svc = StorageVirtualizeAPI(
    ip_address="10.0.0.1",
    username_or_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    password=None  # No password needed
)
```

#### Method 3: Manual Authentication

For more control over authentication:

```python
from openapi_client.api.authentication_api import AuthenticationApi
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient

# Configure
config = Configuration()
config.host = "https://10.0.0.1:7443/rest/v1"
config.verify_ssl = True

# Authenticate
auth_api = AuthenticationApi(ApiClient(config))
response = auth_api.auth_post(
    x_auth_username="admin",
    x_auth_password="your_password"
)

# Store token
config.access_token = response.token
print(f"Token obtained: {response.token[:20]}...")
```

### Token Management

#### Check Token Expiration

```python
import jwt
from datetime import datetime

def check_token_expiry(token):
    """Check if token is expired or about to expire"""
    try:
        decoded = jwt.decode(
            token,
            options={"verify_signature": False}
        )
        exp_timestamp = decoded.get('exp')
        if exp_timestamp:
            exp_time = datetime.fromtimestamp(exp_timestamp)
            time_left = exp_time - datetime.now()
            print(f"Token expires in: {time_left}")
            return time_left.total_seconds() > 0
    except Exception as e:
        print(f"Error checking token: {e}")
        return False

# Usage
check_token_expiry(svc._authentication_api.api_client.configuration.access_token)
```

#### Refresh Token

```python
def refresh_token(svc, username, password):
    """Refresh the authentication token"""
    try:
        response = svc.authentication_api.auth_post(
            x_auth_username=username,
            x_auth_password=password
        )

        # Update token in all API clients
        new_token = response.token
        svc._authentication_api.api_client.configuration.access_token = new_token
        svc._svc_info_api.api_client.configuration.access_token = new_token
        svc._svc_task_api.api_client.configuration.access_token = new_token

        print("Token refreshed successfully")
        return new_token
    except ApiException as e:
        print(f"Failed to refresh token: {e}")
        return None
```

### Security Best Practices

#### 1. Never Hardcode Credentials

```python
import os
from openapi_client.api.storage_virtualize_api import StorageVirtualizeAPI

# Use environment variables
svc = StorageVirtualizeAPI(
    ip_address=os.getenv("STORAGE_HOST"),
    username_or_token=os.getenv("STORAGE_USER"),
    password=os.getenv("STORAGE_PASSWORD")
)
```

#### 2. Use Configuration Files

```python
import json

# Load from secure config file
with open('/secure/path/config.json', 'r') as f:
    config = json.load(f)

svc = StorageVirtualizeAPI(
    ip_address=config['host'],
    username_or_token=config['username'],
    password=config['password']
)
```

#### 3. Enable SSL Verification in Production

```python
from openapi_client.configuration import Configuration

config = Configuration()
config.host = "https://10.0.0.1:7443/rest/v1"
config.verify_ssl = True  # Always True in production
config.ssl_ca_cert = "/path/to/ca-bundle.crt"  # Your CA certificate
```

---

## Core Concepts

### API Structure

The SDK is organized into several API classes:

```text
StorageVirtualizeAPI (Main wrapper)
├── authentication_api  → Authentication and token management
├── svc_info_api        → Read operations (ls* commands)
├── svc_task_api        → Write operations (mk*, ch*, rm* commands)
├── utility_api         → Utility functions
└── download_api        → File download operations
```

### API Naming Convention

Commands follow the Storage Virtualize CLI naming pattern:

- `ls*` - List/query operations (e.g., `lsvdisk`, `lshost`)
- `mk*` - Create operations (e.g., `mkvdisk`, `mkhost`)
- `ch*` - Modify operations (e.g., `chvdisk`, `chhost`)
- `rm*` - Delete operations (e.g., `rmvdisk`, `rmhost`)

### Request/Response Models

Most API calls use Pydantic models for type safety:

```python
from openapi_client.models.mkvdisk_post_request import MkvdiskPostRequest

# Create a request model
vdisk_request = MkvdiskPostRequest(
    name="my_vdisk",
    mdiskgrp="Pool0",
    size=100,  # Size in GB
    unit="gb"
)

# Make API call
response = svc.svc_task_api.mkvdisk_post(
    x_auth_token=None,  # Uses stored token
    mkvdisk_post_request=vdisk_request
)

print(f"Created vdisk with ID: {response['id']}")
```

### Error Handling

The SDK provides specific exception types:

```python
from openapi_client.rest import (
    ApiException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ServiceException
)

try:
    result = svc.svc_info_api.lsvdisk_id_post(vdisk_id="999")
except NotFoundException as e:
    print(f"VDisk not found: {e}")
except UnauthorizedException as e:
    print(f"Authentication failed: {e}")
except ApiException as e:
    print(f"API error: {e.status} - {e.reason}")
```

---

## Common Operations

### Managing Virtual Disks

#### List All Virtual Disks

```python
# List all vdisks
vdisks = svc.svc_info_api.lsvdisk_post()
for vdisk in vdisks:
    print(f"Name: {vdisk['name']}, Size: {vdisk['capacity']} GB, Status: {vdisk['status']}")
```

#### Get Specific Virtual Disk

```python
# By ID
vdisk = svc.svc_info_api.lsvdisk_id_post(vdisk_id="5")

# By name
from openapi_client.models.lsvdisk_post_request import LsvdiskPostRequest

request = LsvdiskPostRequest(filtervalue=f"name=my_vdisk")
vdisks = svc.svc_info_api.lsvdisk_post(lsvdisk_post_request=request)
```

#### Create Virtual Disk

```python
from openapi_client.models.mkvdisk_post_request import MkvdiskPostRequest

vdisk_request = MkvdiskPostRequest(
    name="production_vdisk_01",
    mdiskgrp="Pool0",
    size=500,
    unit="gb",
    rsize="2%",  # Thin provisioning
    autoexpand=True
)

try:
    response = svc.svc_task_api.mkvdisk_post(
        mkvdisk_post_request=vdisk_request
    )
    print(f"✓ Created vdisk ID: {response['id']}")
except ApiException as e:
    print(f"✗ Failed to create vdisk: {e.reason}")
```

#### Modify Virtual Disk

```python
from openapi_client.models.chvdisk_id_post_request import ChvdiskIdPostRequest

modify_request = ChvdiskIdPostRequest(
    name="new_vdisk_name",
    size=1000,  # Expand to 1TB
    unit="gb"
)

response = svc.svc_task_api.chvdisk_id_post(
    vdisk_id="5",
    chvdisk_id_post_request=modify_request
)

print("✓ VDisk modified successfully")
```

#### Delete Virtual Disk

```python
try:
    response = svc.svc_task_api.rmvdisk_id_post(vdisk_id="5")
    print("✓ VDisk deleted successfully")
except ApiException as e:
    if e.status == 400:
        print("✗ Cannot delete: VDisk may be mapped to hosts")
    else:
        print(f"✗ Error: {e.reason}")
```

### Managing Hosts

#### List Hosts

```python
hosts = svc.svc_info_api.lshost_post()
for host in hosts:
    print(
        f"Host: {host['name']}, Status: {host['status']}, "
        f"WWPNs: {host.get('WWPN', 'N/A')}"
    )
```

#### Create Host

```python
from openapi_client.models.mkhost_post_request import MkhostPostRequest

host_request = MkhostPostRequest(
    name="esx_host_01",
    protocol="scsi",
    type="generic",
    fcwwpn="50:01:23:45:67:89:AB:CD"  # Fibre Channel WWPN
)

response = svc.svc_task_api.mkhost_post(mkhost_post_request=host_request)
print(f"✓ Created host ID: {response['id']}")
```

#### Map VDisk to Host

```python
from openapi_client.models.mkvdiskhostmap_id_post_request import MkvdiskhostmapIdPostRequest

map_request = MkvdiskhostmapIdPostRequest(
    host="esx_host_01",
    scsi=0  # SCSI ID
)

response = svc.svc_task_api.mkvdiskhostmap_id_post(
    vdisk_id="5",
    mkvdiskhostmap_id_post_request=map_request
)

print(f"✓ VDisk mapped to host with SCSI ID: {response['scsi_id']}")
```

### Managing Snapshots

#### Create Snapshot

```python
from openapi_client.models.addsnapshot_post_request import AddsnapshotPostRequest

snapshot_request = AddsnapshotPostRequest(
    source="production_vdisk_01",
    name="prod_snapshot_20260513"
)

response = svc.svc_task_api.addsnapshot_post(
    addsnapshot_post_request=snapshot_request
)

print(f"✓ Snapshot created: {response['name']}")
```

#### List Snapshots

```python
snapshots = svc.svc_info_api.lsvolumesnapshot_post()
for snap in snapshots:
    print(
        f"Snapshot: {snap['name']}, Source: {snap['volume_name']}, "
        f"Created: {snap['time']}"
    )
```

#### Restore from Snapshot

```python
from openapi_client.models.refreshfromsnapshot_post_request import RefreshfromsnapshotPostRequest

restore_request = RefreshfromsnapshotPostRequest(
    source="prod_snapshot_20260513",
    target="production_vdisk_01"
)

response = svc.svc_task_api.refreshfromsnapshot_post(
    refreshfromsnapshot_post_request=restore_request
)

print("✓ Restore initiated")
```

### Monitoring System Health

#### Get System Information

```python
# Cluster information
cluster = svc.svc_info_api.lscluster_post()
print(f"Cluster: {cluster['name']}, Status: {cluster['statistics_status']}")

# Node information
nodes = svc.svc_info_api.lsnode_post()
for node in nodes:
    print(f"Node {node['id']}: {node['name']}, Status: {node['status']}")
```

#### Check Event Log

```python
from openapi_client.models.lseventlog_post_request import LseventlogPostRequest

# Get recent errors
event_request = LseventlogPostRequest(
    filtervalue="severity=error",
    limit=10
)

events = svc.svc_info_api.lseventlog_post(
    lseventlog_post_request=event_request
)

for event in events:
    print(f"[{event['time']}] {event['event_id']}: {event['message']}")
```

#### Monitor Performance

```python
# Get cluster statistics
stats = svc.svc_info_api.lsclusterstats_post()
print(
    f"IOPS: {stats['total_iops']}, "
    f"Throughput: {stats['total_throughput']} MB/s, "
    f"Latency: {stats['average_latency']} ms"
)

# Get vdisk statistics
vdisk_stats = svc.svc_info_api.lsvdiskstats_post()
for stat in vdisk_stats:
    print(
        f"VDisk {stat['name']}: {stat['iops']} IOPS, "
        f"{stat['throughput']} MB/s"
    )
```

### Downloading Files

```python
from openapi_client.models.download_post_request import DownloadPostRequest

# Download support package
download_request = DownloadPostRequest(
    prefix="/dumps",
    filename="support_package.tar.gz"
)

response = svc.download_api.download_post(
    download_post_request=download_request
)

# Save to file
with open("local_support_package.tar.gz", "wb") as f:
    f.write(response)

print("✓ File downloaded successfully")
```

---

## Advanced Usage

### Batch Operations

```python
def create_multiple_vdisks(svc, vdisk_configs):
    """Create multiple vdisks in batch"""
    results = []

    for config in vdisk_configs:
        try:
            request = MkvdiskPostRequest(**config)
            response = svc.svc_task_api.mkvdisk_post(
                mkvdisk_post_request=request
            )
            results.append({
                'name': config['name'],
                'status': 'success',
                'id': response['id']
            })
        except ApiException as e:
            results.append({
                'name': config['name'],
                'status': 'failed',
                'error': str(e)
            })

    return results

# Usage
vdisk_configs = [
    {'name': 'vdisk_01', 'mdiskgrp': 'Pool0', 'size': 100, 'unit': 'gb'},
    {'name': 'vdisk_02', 'mdiskgrp': 'Pool0', 'size': 200, 'unit': 'gb'},
    {'name': 'vdisk_03', 'mdiskgrp': 'Pool1', 'size': 300, 'unit': 'gb'},
]

results = create_multiple_vdisks(svc, vdisk_configs)
for result in results:
    print(f"{result['name']}: {result['status']}")
```

### Async Operations with Threading

```python
import concurrent.futures
from typing import List, Dict

def get_vdisk_details(svc, vdisk_id):
    """Get detailed information for a single vdisk"""
    try:
        return svc.svc_info_api.lsvdisk_id_post(vdisk_id=str(vdisk_id))
    except ApiException as e:
        return {'id': vdisk_id, 'error': str(e)}

def get_all_vdisk_details_parallel(svc, vdisk_ids: List[int]) -> List[Dict]:
    """Fetch vdisk details in parallel"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(get_vdisk_details, svc, vid)
            for vid in vdisk_ids
        ]
        results = [
            future.result()
            for future in concurrent.futures.as_completed(futures)
        ]
    return results

# Usage
vdisk_ids = range(1, 101)  # IDs 1-100
details = get_all_vdisk_details_parallel(svc, vdisk_ids)
print(f"Retrieved details for {len(details)} vdisks")
```

### Custom Retry Logic

```python
import time
from functools import wraps

def retry_on_failure(max_retries=3, delay=2, backoff=2):
    """Decorator to retry failed API calls"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay

            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except ApiException as e:
                    retries += 1
                    if retries >= max_retries:
                        raise

                    if e.status in [429, 503]:  # Rate limit or service unavailable
                        print(f"Retry {retries}/{max_retries} after {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        raise

            return None
        return wrapper
    return decorator

# Usage
@retry_on_failure(max_retries=5, delay=1, backoff=2)
def create_vdisk_with_retry(svc, vdisk_config):
    request = MkvdiskPostRequest(**vdisk_config)
    return svc.svc_task_api.mkvdisk_post(mkvdisk_post_request=request)
```

### Context Manager for Resource Cleanup

```python
from contextlib import contextmanager

@contextmanager
def storage_session(ip_address, username, password):
    """Context manager for storage API session"""
    svc = None
    try:
        svc = StorageVirtualizeAPI(ip_address, username, password)
        print("✓ Connected to storage system")
        yield svc
    except Exception as e:
        print(f"✗ Error: {e}")
        raise
    finally:
        if svc:
            print("✓ Session closed")

# Usage
with storage_session("10.0.0.1", "admin", "password") as svc:
    vdisks = svc.svc_info_api.lsvdisk_post()
    print(f"Found {len(vdisks)} vdisks")
```

### Filtering and Pagination

```python
from openapi_client.models.lsvdisk_post_request import LsvdiskPostRequest

def get_vdisks_by_pool(svc, pool_name, limit=100):
    """Get vdisks filtered by storage pool"""
    request = LsvdiskPostRequest(
        filtervalue=f"mdisk_grp_name={pool_name}",
        limit=limit
    )
    return svc.svc_info_api.lsvdisk_post(lsvdisk_post_request=request)

def get_large_vdisks(svc, min_size_gb=1000):
    """Get vdisks larger than specified size"""
    all_vdisks = svc.svc_info_api.lsvdisk_post()
    return [
        vdisk for vdisk in all_vdisks
        if int(vdisk.get('capacity', 0)) >= min_size_gb
    ]

# Usage
pool_vdisks = get_vdisks_by_pool(svc, "Pool0")
large_vdisks = get_large_vdisks(svc, min_size_gb=500)
```

---

## Best Practices

### 1. Connection Management

```python
# ✓ GOOD: Reuse connection
svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
for i in range(100):
    vdisks = svc.svc_info_api.lsvdisk_post()
    # Process vdisks...

# ✗ BAD: Creating new connection each time
for i in range(100):
    svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
    vdisks = svc.svc_info_api.lsvdisk_post()
```

### 2. Error Handling

```python
# ✓ GOOD: Specific exception handling
try:
    vdisk = svc.svc_info_api.lsvdisk_id_post(vdisk_id="5")
except NotFoundException:
    print("VDisk not found, creating new one...")
    # Create vdisk
except UnauthorizedException:
    print("Token expired, re-authenticating...")
    # Refresh token
except ApiException as e:
    print(f"Unexpected error: {e}")
    # Log and handle

# ✗ BAD: Catching all exceptions
try:
    vdisk = svc.svc_info_api.lsvdisk_id_post(vdisk_id="5")
except Exception as e:
    print("Something went wrong")
```

### 3. Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('storage_operations.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Use in operations
def create_vdisk_with_logging(svc, config):
    logger.info(f"Creating vdisk: {config['name']}")
    try:
        request = MkvdiskPostRequest(**config)
        response = svc.svc_task_api.mkvdisk_post(mkvdisk_post_request=request)
        logger.info(f"✓ VDisk created with ID: {response['id']}")
        return response
    except ApiException as e:
        logger.error(f"✗ Failed to create vdisk: {e.reason}")
        raise
```

### 4. Configuration Management

```python
import yaml

# config.yaml
"""
storage:
  host: 10.0.0.1
  username: admin
  password: ${STORAGE_PASSWORD}  # From environment
  ssl_verify: true
  timeout: 30

defaults:
  vdisk:
    mdiskgrp: Pool0
    rsize: 2%
    autoexpand: true
"""

def load_config(config_file='config.yaml'):
    """Load configuration from YAML file"""
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    # Replace environment variables
    import os
    password = os.getenv('STORAGE_PASSWORD')
    config['storage']['password'] = password
    return config

# Usage
config = load_config()
svc = StorageVirtualizeAPI(
    ip_address=config['storage']['host'],
    username_or_token=config['storage']['username'],
    password=config['storage']['password']
)
```

### 5. Input Validation

```python
def validate_vdisk_name(name):
    """Validate vdisk name according to rules"""
    if not name:
        raise ValueError("VDisk name cannot be empty")
    if len(name) > 63:
        raise ValueError("VDisk name too long (max 63 characters)")
    if not name[0].isalpha():
        raise ValueError("VDisk name must start with a letter")
    if not all(c.isalnum() or c in '-_' for c in name):
        raise ValueError("VDisk name contains invalid characters")
    return True

def create_vdisk_safe(svc, name, mdiskgrp, size):
    """Create vdisk with validation"""
    validate_vdisk_name(name)
    if size <= 0:
        raise ValueError("Size must be positive")

    request = MkvdiskPostRequest(
        name=name,
        mdiskgrp=mdiskgrp,
        size=size,
        unit="gb"
    )
    return svc.svc_task_api.mkvdisk_post(mkvdisk_post_request=request)
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: SSL Certificate Verification Failed

**Error:**

```text
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
```

**Solution:**

```python
# For development only - disable SSL verification
from openapi_client.configuration import Configuration

config = Configuration()
config.host = "https://10.0.0.1:7443/rest/v1"
config.verify_ssl = False  # Only for development!

# For production - provide CA certificate
config.verify_ssl = True
config.ssl_ca_cert = "/path/to/ca-bundle.crt"
```

#### Issue 2: Authentication Failed (401)

**Error:**

```text
UnauthorizedException: (401) Unauthorized
```

**Solutions:**

```python
# 1. Check credentials
print(f"Username: {username}")
print(f"Password length: {len(password)}")

# 2. Check if user account is locked
# Log into the system UI and verify account status

# 3. Verify REST API is enabled
# Check system configuration

# 4. Check token expiration
import jwt

token = svc._authentication_api.api_client.configuration.access_token
decoded = jwt.decode(token, options={"verify_signature": False})
print(f"Token expires at: {decoded.get('exp')}")
```

#### Issue 3: Rate Limiting (429)

**Error:**

```text
ApiException: (429) Too Many Requests
```

**Solution:**

```python
import time

def api_call_with_rate_limit(func, *args, **kwargs):
    """Call API with rate limiting"""
    max_retries = 5
    retry_delay = 1

    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            if e.status == 429 and attempt < max_retries - 1:
                wait_time = retry_delay * (2 ** attempt)
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
```

#### Issue 4: Connection Timeout

**Error:**

```text
urllib3.exceptions.ReadTimeoutError: Read timed out
```

**Solution:**

```python
from openapi_client.configuration import Configuration

config = Configuration()
config.host = "https://10.0.0.1:7443/rest/v1"
config.timeout = 60  # Increase timeout to 60 seconds

# Or set per-request timeout
import urllib3
http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=10.0, read=60.0))
```

#### Issue 5: Import Errors

**Error:**

```text
ModuleNotFoundError: No module named 'openapi_client'
```

**Solution:**

```bash
# Verify installation
pip list | grep ibm_svc_rest_client

# Reinstall if needed
pip uninstall ibm_svc_rest_client
pip install ibm_svc_rest_client-1.0.0-py3-none-any.whl

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

### Debug Mode

Enable debug logging to troubleshoot issues:

```python
import logging
from openapi_client.configuration import Configuration

# Enable debug mode
config = Configuration()
config.debug = True

# Configure detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('openapi_client')
logger.setLevel(logging.DEBUG)

# Now all API calls will show detailed debug information
svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
```

### Getting Support

- **Check Documentation:** Review this guide and the API reference
- **Enable Debug Logging:** Capture detailed logs for analysis
- **Check System Logs:** Review storage system event logs
- **Contact Support:** Provide debug logs and error messages

---

## API Reference

### StorageVirtualizeAPI Class

Main wrapper class providing access to all API endpoints.

#### Constructor

```python
StorageVirtualizeAPI(
    ip_address: str,
    username_or_token: str,
    password: Optional[str] = None
)
```

#### Properties

- `authentication_api`: `AuthenticationApi` instance
- `svc_info_api`: `SVCInfoApi` instance (read operations)
- `svc_task_api`: `SVCTaskApi` instance (write operations)
- `utility_api`: `UtilityApi` instance
- `download_api`: `DownloadApi` instance

### SVCInfoApi - Read Operations

#### Common methods

- `lsarray_post()` - List arrays
- `lsvdisk_post()` - List virtual disks
- `lsvdisk_id_post(vdisk_id)` - Get specific vdisk
- `lshost_post()` - List hosts
- `lshost_id_post(host_id)` - Get specific host
- `lsnode_post()` - List nodes
- `lscluster_post()` - Get cluster information
- `lseventlog_post()` - Get event log
- `lsmdiskgrp_post()` - List storage pools
- `lsvolumesnapshot_post()` - List snapshots

### SVCTaskApi - Write Operations

#### Common methods

- `mkvdisk_post(request)` - Create virtual disk
- `chvdisk_id_post(vdisk_id, request)` - Modify virtual disk
- `rmvdisk_id_post(vdisk_id)` - Delete virtual disk
- `mkhost_post(request)` - Create host
- `chhost_id_post(host_id, request)` - Modify host
- `rmhost_id_post(host_id)` - Delete host
- `mkvdiskhostmap_id_post(vdisk_id, request)` - Map vdisk to host
- `rmvdiskhostmap_id_post(vdisk_id, host)` - Unmap vdisk from host
- `addsnapshot_post(request)` - Create snapshot
- `refreshfromsnapshot_post(request)` - Restore from snapshot

### Exception Classes

- `ApiException` - Base exception for all API errors
- `BadRequestException` - HTTP 400 errors
- `UnauthorizedException` - HTTP 401 errors
- `ForbiddenException` - HTTP 403 errors
- `NotFoundException` - HTTP 404 errors
- `ServiceException` - HTTP 500 errors

---

## Examples

### Example 1: Complete VDisk Lifecycle

```python
from openapi_client.api.storage_virtualize_api import StorageVirtualizeAPI
from openapi_client.models.mkvdisk_post_request import MkvdiskPostRequest
from openapi_client.models.chvdisk_id_post_request import ChvdiskIdPostRequest
from openapi_client.rest import ApiException

def vdisk_lifecycle_demo():
    """Demonstrate complete vdisk lifecycle"""
    # Connect
    svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")

    # 1. Create vdisk
    print("1. Creating vdisk...")
    create_request = MkvdiskPostRequest(
        name="demo_vdisk",
        mdiskgrp="Pool0",
        size=100,
        unit="gb",
        rsize="2%"
    )
    response = svc.svc_task_api.mkvdisk_post(mkvdisk_post_request=create_request)
    vdisk_id = response['id']
    print(f"   ✓ Created vdisk ID: {vdisk_id}")

    # 2. Get vdisk details
    print("2. Getting vdisk details...")
    vdisk = svc.svc_info_api.lsvdisk_id_post(vdisk_id=vdisk_id)
    print(f"   Name: {vdisk['name']}, Capacity: {vdisk['capacity']} GB")

    # 3. Modify vdisk
    print("3. Expanding vdisk...")
    modify_request = ChvdiskIdPostRequest(size=200, unit="gb")
    svc.svc_task_api.chvdisk_id_post(
        vdisk_id=vdisk_id,
        chvdisk_id_post_request=modify_request
    )
    print("   ✓ Vdisk expanded to 200 GB")

    # 4. Create snapshot
    print("4. Creating snapshot...")
    from openapi_client.models.addsnapshot_post_request import AddsnapshotPostRequest
    snapshot_request = AddsnapshotPostRequest(
        source="demo_vdisk",
        name="demo_snapshot"
    )
    svc.svc_task_api.addsnapshot_post(addsnapshot_post_request=snapshot_request)
    print("   ✓ Snapshot created")

    # 5. Delete vdisk
    print("5. Deleting vdisk...")
    svc.svc_task_api.rmvdisk_id_post(vdisk_id=vdisk_id)
    print("   ✓ Vdisk deleted")

    print("\n✓ Lifecycle demo completed successfully!")

if __name__ == "__main__":
    vdisk_lifecycle_demo()
```

### Example 2: Automated Health Check

```python
import json
from datetime import datetime

def storage_health_check(svc):
    """Perform comprehensive storage health check"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'checks': {}
    }

    # Check 1: Cluster status
    print("Checking cluster status...")
    cluster = svc.svc_info_api.lscluster_post()
    report['checks']['cluster'] = {
        'name': cluster['name'],
        'status': cluster['statistics_status'],
        'healthy': cluster['statistics_status'] == 'online'
    }

    # Check 2: Node status
    print("Checking node status...")
    nodes = svc.svc_info_api.lsnode_post()
    unhealthy_nodes = [n for n in nodes if n['status'] != 'online']
    report['checks']['nodes'] = {
        'total': len(nodes),
        'online': len(nodes) - len(unhealthy_nodes),
        'unhealthy': unhealthy_nodes,
        'healthy': len(unhealthy_nodes) == 0
    }

    # Check 3: Storage pool capacity
    print("Checking storage pools...")
    pools = svc.svc_info_api.lsmdiskgrp_post()
    low_capacity_pools = []
    for pool in pools:
        used_pct = (int(pool['used_capacity']) / int(pool['capacity'])) * 100
        if used_pct > 80:
            low_capacity_pools.append({
                'name': pool['name'],
                'used_percent': used_pct
            })
    report['checks']['storage_pools'] = {
        'total': len(pools),
        'low_capacity': low_capacity_pools,
        'healthy': len(low_capacity_pools) == 0
    }

    # Check 4: Recent errors
    print("Checking event log...")
    from openapi_client.models.lseventlog_post_request import LseventlogPostRequest
    event_request = LseventlogPostRequest(
        filtervalue="severity=error",
        limit=10
    )
    errors = svc.svc_info_api.lseventlog_post(lseventlog_post_request=event_request)
    report['checks']['recent_errors'] = {
        'count': len(errors),
        'errors': [{'id': e['event_id'], 'message': e['message']} for e in errors[:5]],
        'healthy': len(errors) == 0
    }

    # Overall health
    all_healthy = all(check.get('healthy', True) for check in report['checks'].values())
    report['overall_health'] = 'HEALTHY' if all_healthy else 'ISSUES_DETECTED'

    # Print report
    print("\n" + "=" * 60)
    print("STORAGE HEALTH CHECK REPORT")
    print("=" * 60)
    print(json.dumps(report, indent=2))
    return report

# Usage
svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
health_report = storage_health_check(svc)
```

### Example 3: Bulk Host Provisioning

```python
def provision_hosts_from_csv(svc, csv_file):
    """Provision multiple hosts from CSV file"""
    import csv
    from openapi_client.models.mkhost_post_request import MkhostPostRequest

    results = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Create host
                host_request = MkhostPostRequest(
                    name=row['hostname'],
                    protocol=row['protocol'],
                    type=row['type'],
                    fcwwpn=row.get('wwpn')
                )
                response = svc.svc_task_api.mkhost_post(
                    mkhost_post_request=host_request
                )
                results.append({
                    'hostname': row['hostname'],
                    'status': 'success',
                    'id': response['id']
                })
                print(f"✓ Created host: {row['hostname']}")
            except ApiException as e:
                results.append({
                    'hostname': row['hostname'],
                    'status': 'failed',
                    'error': str(e)
                })
                print(f"✗ Failed to create host {row['hostname']}: {e}")

    # Summary
    success_count = sum(1 for r in results if r['status'] == 'success')
    print(f"\nProvisioned {success_count}/{len(results)} hosts successfully")
    return results

# CSV format:
# hostname,protocol,type,wwpn
# esx_host_01,scsi,generic,50:01:23:45:67:89:AB:CD
# esx_host_02,scsi,generic,50:01:23:45:67:89:AB:CE

# Usage
svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")
results = provision_hosts_from_csv(svc, "hosts.csv")
```

---

## Conclusion

This guide covers the essential aspects of using the IBM Storage Virtualize REST API Python SDK. For additional information:

- **API Documentation:** See the `docs/` directory for detailed API reference
- **Installation Guide:** Refer to `INSTALL.md`
- **Source Code:** Review the SDK source code for implementation details
- **IBM Documentation:** Consult official IBM Storage Virtualize documentation

### Quick Reference Card

```python
# Connect
from openapi_client.api.storage_virtualize_api import StorageVirtualizeAPI

svc = StorageVirtualizeAPI("10.0.0.1", "admin", "password")

# List resources
vdisks = svc.svc_info_api.lsvdisk_post()
hosts = svc.svc_info_api.lshost_post()
pools = svc.svc_info_api.lsmdiskgrp_post()

# Create vdisk
from openapi_client.models.mkvdisk_post_request import MkvdiskPostRequest

request = MkvdiskPostRequest(name="my_vdisk", mdiskgrp="Pool0", size=100, unit="gb")
response = svc.svc_task_api.mkvdisk_post(mkvdisk_post_request=request)

# Error handling
from openapi_client.rest import ApiException

try:
    result = svc.svc_info_api.lsvdisk_id_post(vdisk_id="5")
except ApiException as e:
    print(f"Error: {e.status} - {e.reason}")
```

Happy coding with IBM Storage Virtualize Python SDK! 🚀
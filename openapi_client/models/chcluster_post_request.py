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


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChclusterPostRequest(BaseModel):
    """
    ChclusterPostRequest
    """ # noqa: E501
    servicepwd: Optional[StrictStr] = None
    speed: Optional[StrictInt] = None
    alias: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    autoquorum: Optional[StrictInt] = None
    icatip: Optional[StrictStr] = None
    icatip_6: Optional[StrictStr] = None
    gmlinktolerance: Optional[StrictInt] = None
    gminterdelaysimulation: Optional[StrictInt] = None
    gmintradelaysimulation: Optional[StrictInt] = None
    invemailinterval: Optional[StrictInt] = None
    ntpip: Optional[StrictStr] = None
    ntpip_6: Optional[StrictStr] = None
    isnsip: Optional[StrictStr] = None
    isnsip_6: Optional[StrictStr] = None
    iscsiauthmethod: Optional[StrictStr] = None
    chapsecret: Optional[StrictStr] = None
    nochapsecret: Optional[StrictBool] = None
    relationshipbandwidthlimit: Optional[StrictInt] = None
    gmmaxhostdelay: Optional[StrictInt] = None
    layer: Optional[StrictInt] = None
    consoleip: Optional[StrictStr] = None
    rcbuffersize: Optional[StrictInt] = None
    svcconfig: Optional[StrictBool] = None
    easysetup: Optional[StrictInt] = None
    infocenterurl: Optional[StrictStr] = None
    cacheprefetch: Optional[StrictInt] = None
    regensslcert: Optional[StrictBool] = None
    compressiondestagemode: Optional[StrictInt] = None
    localfcportmask: Optional[StrictInt] = None
    partnerfcportmask: Optional[StrictInt] = None
    hightempmode: Optional[StrictInt] = None
    topology: Optional[StrictInt] = None
    rcauthmethod: Optional[StrictStr] = None
    guiadvancedpool: Optional[StrictInt] = None
    vdiskprotectiontime: Optional[StrictInt] = None
    vdiskprotectionenabled: Optional[StrictInt] = None
    easytieracceleration: Optional[StrictInt] = None
    legacyhyperswap: Optional[StrictInt] = None
    odx: Optional[StrictInt] = None
    maxreplicationdelay: Optional[StrictInt] = None
    partnershipexclusionthreshold: Optional[StrictInt] = None
    gen1compatibilitymode: Optional[StrictInt] = None
    ibmcustomer: Optional[StrictStr] = None
    ibmcomponent: Optional[StrictInt] = None
    ibmcountry: Optional[StrictStr] = None
    backendunmap: Optional[StrictInt] = None
    hostunmap: Optional[StrictInt] = None
    enhancedcallhome: Optional[StrictInt] = None
    censorcallhome: Optional[StrictInt] = None
    garbagecollectiondisabled: Optional[StrictInt] = None
    quorummode: Optional[StrictInt] = None
    quorumsite: Optional[StrictStr] = None
    quorumlease: Optional[StrictInt] = None
    cachepartitioncreditdisabled: Optional[StrictInt] = None
    deduplicationdisabled: Optional[StrictInt] = None
    foscopydisabled: Optional[StrictInt] = None
    rehomeoptimizationsdisabled: Optional[StrictInt] = None
    automaticvdiskanalysissettings: Optional[StrictInt] = None
    callhomeacceptedusage: Optional[StrictInt] = None
    safeguardedcopysuspended: Optional[StrictInt] = None
    snapshotpolicysuspended: Optional[StrictInt] = None
    flashcopyguienabled: Optional[StrictInt] = None
    hostipsecpsk: Optional[StrictStr] = None
    nohostipsecpsk: Optional[StrictBool] = None
    forcedhostipsecpsk: Optional[StrictBool] = None
    easytier: Optional[StrictInt] = None
    snapshotpreserveparent: Optional[StrictInt] = None
    anomalydetection: Optional[StrictInt] = None
    supportonly: Optional[StrictBool] = None
    anomalydetectionevent: Optional[StrictInt] = None
    flashcopydefaultgrainsize: Optional[StrictInt] = None
    storageinsightscontrolaccess: Optional[StrictInt] = None
    autodrivedownload: Optional[StrictInt] = None
    singlevolumetype: Optional[StrictInt] = None
    globalautoupdatepolicy: Optional[StrictInt] = None
    autozoneprefix: Optional[StrictStr] = None
    systemsetupstatus: Optional[StrictInt] = None
    ntpauthtype: Optional[StrictInt] = None
    ntpauthkey: Optional[StrictStr] = None
    ntpauthid: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["servicepwd", "speed", "alias", "name", "autoquorum", "icatip", "icatip_6", "gmlinktolerance", "gminterdelaysimulation", "gmintradelaysimulation", "invemailinterval", "ntpip", "ntpip_6", "isnsip", "isnsip_6", "iscsiauthmethod", "chapsecret", "nochapsecret", "relationshipbandwidthlimit", "gmmaxhostdelay", "layer", "consoleip", "rcbuffersize", "svcconfig", "easysetup", "infocenterurl", "cacheprefetch", "regensslcert", "compressiondestagemode", "localfcportmask", "partnerfcportmask", "hightempmode", "topology", "rcauthmethod", "guiadvancedpool", "vdiskprotectiontime", "vdiskprotectionenabled", "easytieracceleration", "legacyhyperswap", "odx", "maxreplicationdelay", "partnershipexclusionthreshold", "gen1compatibilitymode", "ibmcustomer", "ibmcomponent", "ibmcountry", "backendunmap", "hostunmap", "enhancedcallhome", "censorcallhome", "garbagecollectiondisabled", "quorummode", "quorumsite", "quorumlease", "cachepartitioncreditdisabled", "deduplicationdisabled", "foscopydisabled", "rehomeoptimizationsdisabled", "automaticvdiskanalysissettings", "callhomeacceptedusage", "safeguardedcopysuspended", "snapshotpolicysuspended", "flashcopyguienabled", "hostipsecpsk", "nohostipsecpsk", "forcedhostipsecpsk", "easytier", "snapshotpreserveparent", "anomalydetection", "supportonly", "anomalydetectionevent", "flashcopydefaultgrainsize", "storageinsightscontrolaccess", "autodrivedownload", "singlevolumetype", "globalautoupdatepolicy", "autozoneprefix", "systemsetupstatus", "ntpauthtype", "ntpauthkey", "ntpauthid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ChclusterPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChclusterPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "servicepwd": obj.get("servicepwd"),
            "speed": obj.get("speed"),
            "alias": obj.get("alias"),
            "name": obj.get("name"),
            "autoquorum": obj.get("autoquorum"),
            "icatip": obj.get("icatip"),
            "icatip_6": obj.get("icatip_6"),
            "gmlinktolerance": obj.get("gmlinktolerance"),
            "gminterdelaysimulation": obj.get("gminterdelaysimulation"),
            "gmintradelaysimulation": obj.get("gmintradelaysimulation"),
            "invemailinterval": obj.get("invemailinterval"),
            "ntpip": obj.get("ntpip"),
            "ntpip_6": obj.get("ntpip_6"),
            "isnsip": obj.get("isnsip"),
            "isnsip_6": obj.get("isnsip_6"),
            "iscsiauthmethod": obj.get("iscsiauthmethod"),
            "chapsecret": obj.get("chapsecret"),
            "nochapsecret": obj.get("nochapsecret"),
            "relationshipbandwidthlimit": obj.get("relationshipbandwidthlimit"),
            "gmmaxhostdelay": obj.get("gmmaxhostdelay"),
            "layer": obj.get("layer"),
            "consoleip": obj.get("consoleip"),
            "rcbuffersize": obj.get("rcbuffersize"),
            "svcconfig": obj.get("svcconfig"),
            "easysetup": obj.get("easysetup"),
            "infocenterurl": obj.get("infocenterurl"),
            "cacheprefetch": obj.get("cacheprefetch"),
            "regensslcert": obj.get("regensslcert"),
            "compressiondestagemode": obj.get("compressiondestagemode"),
            "localfcportmask": obj.get("localfcportmask"),
            "partnerfcportmask": obj.get("partnerfcportmask"),
            "hightempmode": obj.get("hightempmode"),
            "topology": obj.get("topology"),
            "rcauthmethod": obj.get("rcauthmethod"),
            "guiadvancedpool": obj.get("guiadvancedpool"),
            "vdiskprotectiontime": obj.get("vdiskprotectiontime"),
            "vdiskprotectionenabled": obj.get("vdiskprotectionenabled"),
            "easytieracceleration": obj.get("easytieracceleration"),
            "legacyhyperswap": obj.get("legacyhyperswap"),
            "odx": obj.get("odx"),
            "maxreplicationdelay": obj.get("maxreplicationdelay"),
            "partnershipexclusionthreshold": obj.get("partnershipexclusionthreshold"),
            "gen1compatibilitymode": obj.get("gen1compatibilitymode"),
            "ibmcustomer": obj.get("ibmcustomer"),
            "ibmcomponent": obj.get("ibmcomponent"),
            "ibmcountry": obj.get("ibmcountry"),
            "backendunmap": obj.get("backendunmap"),
            "hostunmap": obj.get("hostunmap"),
            "enhancedcallhome": obj.get("enhancedcallhome"),
            "censorcallhome": obj.get("censorcallhome"),
            "garbagecollectiondisabled": obj.get("garbagecollectiondisabled"),
            "quorummode": obj.get("quorummode"),
            "quorumsite": obj.get("quorumsite"),
            "quorumlease": obj.get("quorumlease"),
            "cachepartitioncreditdisabled": obj.get("cachepartitioncreditdisabled"),
            "deduplicationdisabled": obj.get("deduplicationdisabled"),
            "foscopydisabled": obj.get("foscopydisabled"),
            "rehomeoptimizationsdisabled": obj.get("rehomeoptimizationsdisabled"),
            "automaticvdiskanalysissettings": obj.get("automaticvdiskanalysissettings"),
            "callhomeacceptedusage": obj.get("callhomeacceptedusage"),
            "safeguardedcopysuspended": obj.get("safeguardedcopysuspended"),
            "snapshotpolicysuspended": obj.get("snapshotpolicysuspended"),
            "flashcopyguienabled": obj.get("flashcopyguienabled"),
            "hostipsecpsk": obj.get("hostipsecpsk"),
            "nohostipsecpsk": obj.get("nohostipsecpsk"),
            "forcedhostipsecpsk": obj.get("forcedhostipsecpsk"),
            "easytier": obj.get("easytier"),
            "snapshotpreserveparent": obj.get("snapshotpreserveparent"),
            "anomalydetection": obj.get("anomalydetection"),
            "supportonly": obj.get("supportonly"),
            "anomalydetectionevent": obj.get("anomalydetectionevent"),
            "flashcopydefaultgrainsize": obj.get("flashcopydefaultgrainsize"),
            "storageinsightscontrolaccess": obj.get("storageinsightscontrolaccess"),
            "autodrivedownload": obj.get("autodrivedownload"),
            "singlevolumetype": obj.get("singlevolumetype"),
            "globalautoupdatepolicy": obj.get("globalautoupdatepolicy"),
            "autozoneprefix": obj.get("autozoneprefix"),
            "systemsetupstatus": obj.get("systemsetupstatus"),
            "ntpauthtype": obj.get("ntpauthtype"),
            "ntpauthkey": obj.get("ntpauthkey"),
            "ntpauthid": obj.get("ntpauthid")
        })
        return _obj



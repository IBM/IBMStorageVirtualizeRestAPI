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

# flake8: noqa

"""
    IBM Storage Virtualize REST API 

    The IBM Storage Virtualize Representational State Transfer (REST) model Application Programming Interface (API) consists of command targets that are used to retrieve system information and to create, modify, and delete system resources. These command targets allow command parameters to pass through unedited to the Virtualize command-line interface, which handles parsing parameter specifications for validity and error reporting. Use Hypertext Transfer Protocol Secure (HTTPS) to successfully communicate with the RESTful API server.  ***  ## Usage examples in CURL The following examples show how to use CURL for authentication and user management.  Each curl example takes the following form: >curl -L -X POST https://system_ip:7443/rest/v1/command -H header_1 -H header_2 data-raw 'JSON'  Where the following definitions apply:   * POST is the only HTTPS method that the Storage Virtualize RESTful API supports * system_ip is the IP address to which requests are sent. * v1 indicates this is version 1 of the API.  * command is the target command object (for example, auth, lseventlog or any other CLI command along with any included parameters) * Headers (header_1 ) are individually specified HTTP headers (for example, Content-Type and X-Auth-Token). * --data-raw is followed by JSON input (for example, ```'{\"name\": \"password\"}'```).  ## Authentication The HTTPS server requires authentication of a valid username and password for each API session. The /auth endpoint uses the POST method for the authentication request.  The /auth endpoint returns a JWT(JSON Web Token) authentication token that authenticates every command that a user runs. The JWT token has the token expiry encoded into it.  The following is an example of using the /auth endpoint for an authentication request. Initially, a username and password are provided through the X-Auth-Username and X-Auth-Password header fields. The initial authentication is the only instance where a username and password must be entered. Upon successfully entering the username and password, a JWT authentication token is returned. The returned token string can be decoded by using any JWT decode library freely available on the web. The X-Auth-Token header in  combination with the authentication token replaces the username and password for each  subsequent RESTful API request. Multiple tokens can be requested for a single user.  A token remains valid until its expiry time has been reached which is a user configurable option and can be set via the CLI i.e. `chsecurity`. ``` curl -k -X POST -H 'Content-Type: application/json' -H 'X-Auth-Username: superuser' -H 'X-Auth-Password: passw0rd' https://192.168.10.109:7443/rest/v1/auth ```  This yields an authentication token that can be used for all other commands. ```'{\"token\": \"<token>\"}'```  The auth endpoint has a limit of 3 requests per second for the RESTful API server. Likewise, if you have more than 4 different tokens being used per cluster, or more than  10 requests to command endpoints per second, the API will return the 429 HTTP error code.  ## Making a new user The following example shows how to create a new user, setting a password, and adding a user to a specific group. The example also demonstrates the use of the token in place of the authentication headers that are used in the authentication process: ``` curl -L -X POST '<system_ip>:7443/rest/v1/mkuser' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '{\"name\": \"testuser\", \"usergrp\": \"Service\", \"password\": \"testpassw0rd\"}' ```  ## Changing password by using the username The following example shows how to set a new user password for a user and demonstrates the use of the token in place of the authentication headers used in the authentication process: ``` curl -L -X POST '<system_ip>:7443/rest/chuser/testuser' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '{\"password\": \"newPassw0rd\"}' ```  ## Changing password using the ID The following example shows how to change a user password for a user by using the user ID. In this example, 2 is used as the user ID. ``` curl -L -X POST '<system_ip>:7443/rest/chuser/2' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '{\"password\": \"newPassw0rd\"}' ```  ## Listing all users The following example lists all user using version 1 of the API: ``` curl -L -X POST '<system_ip>:7443/rest/v1/lsuser' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '' ```  ## Listing details about a user The following example shows how to list a user in a version 1 of the API by using the user ID: ``` curl -L -X POST '<system_ip>:7443/rest/v1/lsuser/3' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '' ```  ## Removing a user The following example shows how to remove a user by using the user ID in a version 1 of the API: ``` curl -L -X POST '<system_ip>:7443/rest/v1/rmuser/2' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json' --data-raw '' ```  ## Downloading a file The following example shows how to download a file using a directory and filename ``` curl -L -X POST '<system_ip>:7443/rest/v1/download' -H 'X-Auth-Token: <token>' -H 'Content-Type: application/json'  --data-raw '{\"prefix\": \"/targetdirectory\", \"filename\": \"filetodownload\"}' ```  *** 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "AuthenticationApi",
    "DownloadApi",
    "SVCInfoApi",
    "SVCTaskApi",
    "UtilityApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "ActivatefeaturePostRequest",
    "AddcontrolenclosurePostRequest",
    "AddfcportsetmemberPostRequest",
    "AddhostclustermemberIdPostRequest",
    "AddhostportIdPostRequest",
    "AddmdiskIdPostRequest",
    "AddnodePostRequest",
    "AddsnapshotPostRequest",
    "AddsnapshotpolicyscheduleIdPostRequest",
    "AddvdiskaccessIdPostRequest",
    "AddvdiskcopyIdPostRequest",
    "AddvolumecopyIdPostRequest",
    "AnalyzevdiskIdPostRequest",
    "AnalyzevdiskbysystemPostRequest",
    "ApplydrivesoftwarePostRequest",
    "ApplysoftwarePostRequest",
    "BackupvolumeIdPostRequest",
    "BackupvolumegroupIdPostRequest",
    "CatauditlogPostRequest",
    "CfgportipIdPostRequest",
    "ChaicontainerinfoPostRequest",
    "ChanomalydetectionPostRequest",
    "CharrayIdPostRequest",
    "CharraymemberIdPostRequest",
    "ChauthmultifactorduoPostRequest",
    "ChauthmultifactorverifyPostRequest",
    "ChauthservicePostRequest",
    "ChauthsinglesignonPostRequest",
    "ChbannerPostRequest",
    "Chcloudaccountawss3IdPostRequest",
    "ChcloudaccountazureIdPostRequest",
    "ChcloudaccountswiftIdPostRequest",
    "ChcloudcallhomePostRequest",
    "ChclusterPostRequest",
    "ChclusteripPostRequest",
    "ChcompatibilitymodePostRequest",
    "ChcontrollerIdPostRequest",
    "ChcurrentuserPostRequest",
    "ChdnsserverIdPostRequest",
    "ChdriveIdPostRequest",
    "ChemailPostRequest",
    "ChemailserverIdPostRequest",
    "ChemailuserIdPostRequest",
    "ChenclosureIdPostRequest",
    "ChenclosurecanisterIdPostRequest",
    "ChenclosuredisplaypanelIdPostRequest",
    "ChenclosurefanmoduleIdPostRequest",
    "ChenclosuresemIdPostRequest",
    "ChenclosureslotIdPostRequest",
    "ChencryptionPostRequest",
    "CheventlogPostRequest",
    "ChfcconsistgrpIdPostRequest",
    "ChfcmapIdPostRequest",
    "ChhostIdPostRequest",
    "ChhostclusterIdPostRequest",
    "ChiogrpIdPostRequest",
    "ChipIdPostRequest",
    "ChiscsistorageportIdPostRequest",
    "ChkeyserverIdPostRequest",
    "ChkeyserverisklmPostRequest",
    "ChkeyserverkeysecurePostRequest",
    "ChldapPostRequest",
    "ChldapserverIdPostRequest",
    "ChlicensePostRequest",
    "ChmdiskIdPostRequest",
    "ChmdiskgrpIdPostRequest",
    "ChnodeIdPostRequest",
    "ChnodebatteryIdPostRequest",
    "ChnodebootdriveIdPostRequest",
    "ChnodehwIdPostRequest",
    "ChownershipgroupIdPostRequest",
    "ChpartitionIdPostRequest",
    "ChpartitioncertstorePostRequest",
    "ChpartnershipIdPostRequest",
    "ChportethernetIdPostRequest",
    "ChportfcIdPostRequest",
    "ChportsetIdPostRequest",
    "ChprovisioningpolicyIdPostRequest",
    "ChproxyPostRequest",
    "ChquorumIdPostRequest",
    "ChrcconsistgrpIdPostRequest",
    "ChrcrelationshipIdPostRequest",
    "ChsafeguardedpolicyIdPostRequest",
    "ChsecurityPostRequest",
    "ChsiteIdPostRequest",
    "ChsnapshotPostRequest",
    "ChsnapshotpolicyIdPostRequest",
    "ChsnmpagentPostRequest",
    "ChsnmpserverIdPostRequest",
    "ChsraPostRequest",
    "ChsyslogserverIdPostRequest",
    "ChsystemcertPostRequest",
    "ChsystemcertstorePostRequest",
    "ChsystemethernetPostRequest",
    "ChsystemlimitsPostRequest",
    "ChthrottleIdPostRequest",
    "ChtruststoreIdPostRequest",
    "ChtwopersonintegrityrequestPostRequest",
    "ChuserIdPostRequest",
    "ChusergrpIdPostRequest",
    "ChvcenterIdPostRequest",
    "ChvdiskIdPostRequest",
    "ChvolumeIdPostRequest",
    "ChvolumegroupIdPostRequest",
    "ChvolumegroupreplicationIdPostRequest",
    "ChvolumegroupsnapshotbufferIdPostRequest",
    "ChvolumegroupsnapshotpolicyIdPostRequest",
    "CleardumpsIdPostRequest",
    "CleardumpsPostRequest",
    "ClearenclosuredumpsIdPostRequest",
    "ClearerrlogPostRequest",
    "ClearpluginPostRequest",
    "ConverttoclonePostRequest",
    "CpdumpsIdPostRequest",
    "CpenclosuredumpsIdPostRequest",
    "DetectiscsistorageportcandidatePostRequest",
    "DetectmdiskPostRequest",
    "DownloadPostRequest",
    "DumperrlogPostRequest",
    "Error",
    "ExpandarrayIdPostRequest",
    "ExpandvdisksizeIdPostRequest",
    "LsarrayIdPostRequest",
    "LsarrayPostRequest",
    "LsarrayexpansionprogressIdPostRequest",
    "LsarrayexpansionprogressPostRequest",
    "LsarrayinitprogressIdPostRequest",
    "LsarrayinitprogressPostRequest",
    "LsarraylbaPostRequest",
    "LsarraymemberIdPostRequest",
    "LsarraymemberPostRequest",
    "LsarraymembergoalsIdPostRequest",
    "LsarraymembergoalsPostRequest",
    "LsarraymemberprogressIdPostRequest",
    "LsarraymemberprogressPostRequest",
    "LsarrayrecommendationIdPostRequest",
    "LsarraysyncprogressIdPostRequest",
    "LsarraysyncprogressPostRequest",
    "LsclusterstatsPostRequest",
    "LscontrollerIdPostRequest",
    "LscontrollerPostRequest",
    "LsdependentvdisksPostRequest",
    "LsdiscoverystatusPostRequest",
    "LsdriveIdPostRequest",
    "LsdrivePostRequest",
    "LsdriveclassIdPostRequest",
    "LsdriveclassPostRequest",
    "LsdrivelbaPostRequest",
    "LsdriveprogressIdPostRequest",
    "LsdriveprogressPostRequest",
    "LsdriveupgradeprogressIdPostRequest",
    "LsdriveupgradeprogressPostRequest",
    "LsdumpsIdPostRequest",
    "LsdumpsPostRequest",
    "LsemailuserIdPostRequest",
    "LsemailuserPostRequest",
    "LsenclosureIdPostRequest",
    "LsenclosurePostRequest",
    "LsenclosurecanisterIdPostRequest",
    "LsenclosurecanisterPostRequest",
    "LsenclosuredisplaypanelIdPostRequest",
    "LsenclosuredisplaypanelPostRequest",
    "LsenclosurefanmoduleIdPostRequest",
    "LsenclosurefanmodulePostRequest",
    "LsenclosurepsuIdPostRequest",
    "LsenclosurepsuPostRequest",
    "LsenclosuresemIdPostRequest",
    "LsenclosuresemPostRequest",
    "LsenclosureslotIdPostRequest",
    "LsenclosureslotPostRequest",
    "LsenclosurestatsIdPostRequest",
    "LsenclosurestatsPostRequest",
    "LseventlogIdPostRequest",
    "LseventlogPostRequest",
    "LsfabricPostRequest",
    "LsfabricportIdPostRequest",
    "LsfabricportPostRequest",
    "LsfcconsistgrpIdPostRequest",
    "LsfcconsistgrpPostRequest",
    "LsfcmapIdPostRequest",
    "LsfcmapPostRequest",
    "LsfcportsetmemberIdPostRequest",
    "LsfcportsetmemberPostRequest",
    "LshostIdPostRequest",
    "LshostPostRequest",
    "LshostclusterIdPostRequest",
    "LshostclusterPostRequest",
    "LshostiploginIdPostRequest",
    "LshostiploginPostRequest",
    "LshostzonePostRequest",
    "LsiogrpIdPostRequest",
    "LsiogrpPostRequest",
    "LsipIdPostRequest",
    "LsipPostRequest",
    "LsiscsiauthPostRequest",
    "LsiscsistorageportIdPostRequest",
    "LsiscsistorageportPostRequest",
    "LslocaldiskIdPostRequest",
    "LslocaldiskPostRequest",
    "LsmdiskIdPostRequest",
    "LsmdiskPostRequest",
    "LsmdiskgrpIdPostRequest",
    "LsmdiskgrpPostRequest",
    "LsmdisklbaPostRequest",
    "LsmetadatavdiskPostRequest",
    "LsnodeIdPostRequest",
    "LsnodePostRequest",
    "LsnodebatteryIdPostRequest",
    "LsnodebatteryPostRequest",
    "LsnodebootdriveIdPostRequest",
    "LsnodebootdrivePostRequest",
    "LsnodepsuIdPostRequest",
    "LsnodepsuPostRequest",
    "LsnodestatsIdPostRequest",
    "LsnodestatsPostRequest",
    "LsnvmefabricPostRequest",
    "LsownershipgroupIdPostRequest",
    "LsownershipgroupPostRequest",
    "LspartitionIdPostRequest",
    "LspartitionPostRequest",
    "LspartnershipIdPostRequest",
    "LspartnershipPostRequest",
    "LsportethernetIdPostRequest",
    "LsportethernetPostRequest",
    "LsportfcIdPostRequest",
    "LsportfcPostRequest",
    "LsportibIdPostRequest",
    "LsportibPostRequest",
    "LsportipIdPostRequest",
    "LsportipPostRequest",
    "LsportsasPostRequest",
    "LsportsetIdPostRequest",
    "LsportsetPostRequest",
    "LsportstatsIdPostRequest",
    "LsportstatsPostRequest",
    "LsportusbIdPostRequest",
    "LsportusbPostRequest",
    "LspotentialarraysizeIdPostRequest",
    "LsprovisioningpolicyIdPostRequest",
    "LsprovisioningpolicyPostRequest",
    "LsquorumIdPostRequest",
    "LsquorumPostRequest",
    "LsrcconsistgrpIdPostRequest",
    "LsrcconsistgrpPostRequest",
    "LsrcrelationshipIdPostRequest",
    "LsrcrelationshipPostRequest",
    "LsrcrelationshipcandidatePostRequest",
    "LsrepairsevdiskcopyprogressIdPostRequest",
    "LsrepairsevdiskcopyprogressPostRequest",
    "LsrepairvdiskcopyprogressIdPostRequest",
    "LsrepairvdiskcopyprogressPostRequest",
    "LsreplicationpolicyIdPostRequest",
    "LsreplicationpolicyPostRequest",
    "LssafeguardedpolicyIdPostRequest",
    "LssafeguardedpolicyPostRequest",
    "LssafeguardedscheduleIdPostRequest",
    "LssafeguardedschedulePostRequest",
    "LssasfabricPostRequest",
    "LssevdiskcopyIdPostRequest",
    "LssevdiskcopyPostRequest",
    "LssnapshotpolicyIdPostRequest",
    "LssnapshotpolicyPostRequest",
    "LssnapshotscheduleIdPostRequest",
    "LssnapshotschedulePostRequest",
    "LstargetportfcIdPostRequest",
    "LstargetportfcPostRequest",
    "LsthrottleIdPostRequest",
    "LsthrottlePostRequest",
    "LstruststoreIdPostRequest",
    "LstruststorePostRequest",
    "LsuserIdPostRequest",
    "LsuserPostRequest",
    "LsusergrpIdPostRequest",
    "LsusergrpPostRequest",
    "LsvasaclientcertificateIdPostRequest",
    "LsvasaclientcertificatePostRequest",
    "LsvcenterIdPostRequest",
    "LsvcenterPostRequest",
    "LsvdiskIdPostRequest",
    "LsvdiskPostRequest",
    "LsvdiskaccessIdPostRequest",
    "LsvdiskaccessPostRequest",
    "LsvdiskanalysisIdPostRequest",
    "LsvdiskanalysisPostRequest",
    "LsvdiskcopyIdPostRequest",
    "LsvdiskcopyPostRequest",
    "LsvdiskextentIdPostRequest",
    "LsvdisklbaPostRequest",
    "LsvdiskmemberIdPostRequest",
    "LsvdisksyncprogressIdPostRequest",
    "LsvdisksyncprogressPostRequest",
    "LsvdisktiersIdPostRequest",
    "LsvdisktiersPostRequest",
    "LsvdiskunsharedchunksIdPostRequest",
    "LsvolumebackupPostRequest",
    "LsvolumebackupgenerationPostRequest",
    "LsvolumebackupprogressPostRequest",
    "LsvolumegroupIdPostRequest",
    "LsvolumegroupPostRequest",
    "LsvolumegrouppopulationIdPostRequest",
    "LsvolumegrouppopulationPostRequest",
    "LsvolumegroupreplicationIdPostRequest",
    "LsvolumegroupreplicationPostRequest",
    "LsvolumegroupsnapshotPostRequest",
    "LsvolumegroupsnapshotpolicyIdPostRequest",
    "LsvolumegroupsnapshotpolicyPostRequest",
    "LsvolumegroupsnapshotscheduleIdPostRequest",
    "LsvolumegroupsnapshotschedulePostRequest",
    "LsvolumepopulationIdPostRequest",
    "LsvolumepopulationPostRequest",
    "LsvolumerestoreprogressIdPostRequest",
    "LsvolumerestoreprogressPostRequest",
    "LsvolumesnapshotIdPostRequest",
    "LsvolumesnapshotPostRequest",
    "MergepartitionIdPostRequest",
    "MigrateextsPostRequest",
    "MigratetoimagePostRequest",
    "MigratevdiskPostRequest",
    "MkarrayIdPostRequest",
    "MkarrayPostRequest",
    "Mkcloudaccountawss3PostRequest",
    "MkcloudaccountazurePostRequest",
    "MkcloudaccountswiftPostRequest",
    "MkclusterPostRequest",
    "MkdistributedarrayIdPostRequest",
    "MkdnsserverPostRequest",
    "MkemailserverPostRequest",
    "MkemailuserPostRequest",
    "MkfcconsistgrpPostRequest",
    "MkfcmapPostRequest",
    "MkfcpartnershipIdPostRequest",
    "MkhostPostRequest",
    "MkhostclusterPostRequest",
    "MkimagevolumePostRequest",
    "MkipPostRequest",
    "MkippartnershipPostRequest",
    "MkkeyserverPostRequest",
    "MkldapserverPostRequest",
    "MkmdiskgrpPostRequest",
    "MkmetadatavdiskPostRequest",
    "MkownershipgroupPostRequest",
    "MkpartitionPostRequest",
    "MkpartitioncertstorePostRequest",
    "MkportsetPostRequest",
    "MkprovisioningpolicyPostRequest",
    "MkproxyPostRequest",
    "MkquorumappPostRequest",
    "MkrcconsistgrpPostRequest",
    "MkrcrelationshipPostRequest",
    "MkreplicationpolicyPostRequest",
    "MksafeguardedpolicyPostRequest",
    "MksnapshotpolicyPostRequest",
    "MksnmpserverPostRequest",
    "MksyslogserverPostRequest",
    "MksystemcertstorePostRequest",
    "MksystemsupportcenterPostRequest",
    "MkthrottlePostRequest",
    "MktruststorePostRequest",
    "MktwopersonintegrityrequestPostRequest",
    "MkuserPostRequest",
    "MkusergrpPostRequest",
    "MkvasaclientcertificatePostRequest",
    "MkvcenterPostRequest",
    "MkvdiskPostRequest",
    "MkvdiskhostmapIdPostRequest",
    "MkvolumePostRequest",
    "MkvolumegroupPostRequest",
    "MkvolumehostclustermapIdPostRequest",
    "MovevdiskIdPostRequest",
    "PrestartfcconsistgrpIdPostRequest",
    "PrestartfcmapIdPostRequest",
    "RecoverarrayIdPostRequest",
    "RecovervdiskIdPostRequest",
    "RefreshfromsnapshotPostRequest",
    "RegisterpluginPostRequest",
    "RegistervcenterIdPostRequest",
    "RepairsevdiskcopyIdPostRequest",
    "RepairvdiskcopyIdPostRequest",
    "RestorefromsnapshotPostRequest",
    "RestorevolumeIdPostRequest",
    "RmarrayIdPostRequest",
    "RmarrayPostRequest",
    "RmfcconsistgrpIdPostRequest",
    "RmfcmapIdPostRequest",
    "RmfcportsetmemberPostRequest",
    "RmhostIdPostRequest",
    "RmhostclusterIdPostRequest",
    "RmhostclustermemberIdPostRequest",
    "RmhostportIdPostRequest",
    "RmmdiskIdPostRequest",
    "RmmdiskgrpIdPostRequest",
    "RmmetadatavdiskPostRequest",
    "RmnodeIdPostRequest",
    "RmownershipgroupIdPostRequest",
    "RmpartitionIdPostRequest",
    "RmportipIdPostRequest",
    "RmrcconsistgrpIdPostRequest",
    "RmrcrelationshipIdPostRequest",
    "RmsafeguardedpolicyIdPostRequest",
    "RmsnapshotPostRequest",
    "RmsnapshotpolicyIdPostRequest",
    "RmusergrpIdPostRequest",
    "RmvasaclientcertificatePostRequest",
    "RmvcenterIdPostRequest",
    "RmvdiskIdPostRequest",
    "RmvdiskaccessIdPostRequest",
    "RmvdiskcopyIdPostRequest",
    "RmvdiskhostmapIdPostRequest",
    "RmvolumeIdPostRequest",
    "RmvolumebackupgenerationPostRequest",
    "RmvolumecopyIdPostRequest",
    "RmvolumegroupIdPostRequest",
    "RmvolumehostclustermapIdPostRequest",
    "SendcloudcallhomePostRequest",
    "SetlocalePostRequest",
    "SetpwdresetPostRequest",
    "SettimezonePostRequest",
    "ShrinkvdisksizeIdPostRequest",
    "SplitvdiskcopyIdPostRequest",
    "StartfcconsistgrpIdPostRequest",
    "StartfcmapIdPostRequest",
    "StartrcconsistgrpIdPostRequest",
    "StartrcrelationshipIdPostRequest",
    "StartstatsPostRequest",
    "StopfcconsistgrpIdPostRequest",
    "StopfcmapIdPostRequest",
    "StoprcconsistgrpIdPostRequest",
    "StoprcrelationshipIdPostRequest",
    "SvcLivedumpPostRequest",
    "SvcSnapPostRequest",
    "SvcsearchPostRequest",
    "SvcupgradetestPostRequest",
    "SwapnodeIdPostRequest",
    "SwitchrcconsistgrpIdPostRequest",
    "SwitchrcrelationshipIdPostRequest",
    "TestemailIdPostRequest",
    "TestemailPostRequest",
    "TestldapserverIdPostRequest",
    "TestldapserverPostRequest",
    "TestsnmpserverIdPostRequest",
    "TestsnmpserverPostRequest",
    "TracerouteIdPostRequest",
    "TraceroutePostRequest",
    "TriggerenclosuredumpPostRequest",
    "WritesernumIdPostRequest",
]

# import apis into sdk package
from openapi_client.api.authentication_api import AuthenticationApi as AuthenticationApi
from openapi_client.api.download_api import DownloadApi as DownloadApi
from openapi_client.api.svc_info_api import SVCInfoApi as SVCInfoApi
from openapi_client.api.svc_task_api import SVCTaskApi as SVCTaskApi
from openapi_client.api.utility_api import UtilityApi as UtilityApi

# import ApiClient
from openapi_client.api_response import ApiResponse as ApiResponse
from openapi_client.api_client import ApiClient as ApiClient
from openapi_client.configuration import Configuration as Configuration
from openapi_client.exceptions import OpenApiException as OpenApiException
from openapi_client.exceptions import ApiTypeError as ApiTypeError
from openapi_client.exceptions import ApiValueError as ApiValueError
from openapi_client.exceptions import ApiKeyError as ApiKeyError
from openapi_client.exceptions import ApiAttributeError as ApiAttributeError
from openapi_client.exceptions import ApiException as ApiException

# import models into sdk package
from openapi_client.models.activatefeature_post_request import ActivatefeaturePostRequest as ActivatefeaturePostRequest
from openapi_client.models.addcontrolenclosure_post_request import AddcontrolenclosurePostRequest as AddcontrolenclosurePostRequest
from openapi_client.models.addfcportsetmember_post_request import AddfcportsetmemberPostRequest as AddfcportsetmemberPostRequest
from openapi_client.models.addhostclustermember_id_post_request import AddhostclustermemberIdPostRequest as AddhostclustermemberIdPostRequest
from openapi_client.models.addhostport_id_post_request import AddhostportIdPostRequest as AddhostportIdPostRequest
from openapi_client.models.addmdisk_id_post_request import AddmdiskIdPostRequest as AddmdiskIdPostRequest
from openapi_client.models.addnode_post_request import AddnodePostRequest as AddnodePostRequest
from openapi_client.models.addsnapshot_post_request import AddsnapshotPostRequest as AddsnapshotPostRequest
from openapi_client.models.addsnapshotpolicyschedule_id_post_request import AddsnapshotpolicyscheduleIdPostRequest as AddsnapshotpolicyscheduleIdPostRequest
from openapi_client.models.addvdiskaccess_id_post_request import AddvdiskaccessIdPostRequest as AddvdiskaccessIdPostRequest
from openapi_client.models.addvdiskcopy_id_post_request import AddvdiskcopyIdPostRequest as AddvdiskcopyIdPostRequest
from openapi_client.models.addvolumecopy_id_post_request import AddvolumecopyIdPostRequest as AddvolumecopyIdPostRequest
from openapi_client.models.analyzevdisk_id_post_request import AnalyzevdiskIdPostRequest as AnalyzevdiskIdPostRequest
from openapi_client.models.analyzevdiskbysystem_post_request import AnalyzevdiskbysystemPostRequest as AnalyzevdiskbysystemPostRequest
from openapi_client.models.applydrivesoftware_post_request import ApplydrivesoftwarePostRequest as ApplydrivesoftwarePostRequest
from openapi_client.models.applysoftware_post_request import ApplysoftwarePostRequest as ApplysoftwarePostRequest
from openapi_client.models.backupvolume_id_post_request import BackupvolumeIdPostRequest as BackupvolumeIdPostRequest
from openapi_client.models.backupvolumegroup_id_post_request import BackupvolumegroupIdPostRequest as BackupvolumegroupIdPostRequest
from openapi_client.models.catauditlog_post_request import CatauditlogPostRequest as CatauditlogPostRequest
from openapi_client.models.cfgportip_id_post_request import CfgportipIdPostRequest as CfgportipIdPostRequest
from openapi_client.models.chaicontainerinfo_post_request import ChaicontainerinfoPostRequest as ChaicontainerinfoPostRequest
from openapi_client.models.chanomalydetection_post_request import ChanomalydetectionPostRequest as ChanomalydetectionPostRequest
from openapi_client.models.charray_id_post_request import CharrayIdPostRequest as CharrayIdPostRequest
from openapi_client.models.charraymember_id_post_request import CharraymemberIdPostRequest as CharraymemberIdPostRequest
from openapi_client.models.chauthmultifactorduo_post_request import ChauthmultifactorduoPostRequest as ChauthmultifactorduoPostRequest
from openapi_client.models.chauthmultifactorverify_post_request import ChauthmultifactorverifyPostRequest as ChauthmultifactorverifyPostRequest
from openapi_client.models.chauthservice_post_request import ChauthservicePostRequest as ChauthservicePostRequest
from openapi_client.models.chauthsinglesignon_post_request import ChauthsinglesignonPostRequest as ChauthsinglesignonPostRequest
from openapi_client.models.chbanner_post_request import ChbannerPostRequest as ChbannerPostRequest
from openapi_client.models.chcloudaccountawss3_id_post_request import Chcloudaccountawss3IdPostRequest as Chcloudaccountawss3IdPostRequest
from openapi_client.models.chcloudaccountazure_id_post_request import ChcloudaccountazureIdPostRequest as ChcloudaccountazureIdPostRequest
from openapi_client.models.chcloudaccountswift_id_post_request import ChcloudaccountswiftIdPostRequest as ChcloudaccountswiftIdPostRequest
from openapi_client.models.chcloudcallhome_post_request import ChcloudcallhomePostRequest as ChcloudcallhomePostRequest
from openapi_client.models.chcluster_post_request import ChclusterPostRequest as ChclusterPostRequest
from openapi_client.models.chclusterip_post_request import ChclusteripPostRequest as ChclusteripPostRequest
from openapi_client.models.chcompatibilitymode_post_request import ChcompatibilitymodePostRequest as ChcompatibilitymodePostRequest
from openapi_client.models.chcontroller_id_post_request import ChcontrollerIdPostRequest as ChcontrollerIdPostRequest
from openapi_client.models.chcurrentuser_post_request import ChcurrentuserPostRequest as ChcurrentuserPostRequest
from openapi_client.models.chdnsserver_id_post_request import ChdnsserverIdPostRequest as ChdnsserverIdPostRequest
from openapi_client.models.chdrive_id_post_request import ChdriveIdPostRequest as ChdriveIdPostRequest
from openapi_client.models.chemail_post_request import ChemailPostRequest as ChemailPostRequest
from openapi_client.models.chemailserver_id_post_request import ChemailserverIdPostRequest as ChemailserverIdPostRequest
from openapi_client.models.chemailuser_id_post_request import ChemailuserIdPostRequest as ChemailuserIdPostRequest
from openapi_client.models.chenclosure_id_post_request import ChenclosureIdPostRequest as ChenclosureIdPostRequest
from openapi_client.models.chenclosurecanister_id_post_request import ChenclosurecanisterIdPostRequest as ChenclosurecanisterIdPostRequest
from openapi_client.models.chenclosuredisplaypanel_id_post_request import ChenclosuredisplaypanelIdPostRequest as ChenclosuredisplaypanelIdPostRequest
from openapi_client.models.chenclosurefanmodule_id_post_request import ChenclosurefanmoduleIdPostRequest as ChenclosurefanmoduleIdPostRequest
from openapi_client.models.chenclosuresem_id_post_request import ChenclosuresemIdPostRequest as ChenclosuresemIdPostRequest
from openapi_client.models.chenclosureslot_id_post_request import ChenclosureslotIdPostRequest as ChenclosureslotIdPostRequest
from openapi_client.models.chencryption_post_request import ChencryptionPostRequest as ChencryptionPostRequest
from openapi_client.models.cheventlog_post_request import CheventlogPostRequest as CheventlogPostRequest
from openapi_client.models.chfcconsistgrp_id_post_request import ChfcconsistgrpIdPostRequest as ChfcconsistgrpIdPostRequest
from openapi_client.models.chfcmap_id_post_request import ChfcmapIdPostRequest as ChfcmapIdPostRequest
from openapi_client.models.chhost_id_post_request import ChhostIdPostRequest as ChhostIdPostRequest
from openapi_client.models.chhostcluster_id_post_request import ChhostclusterIdPostRequest as ChhostclusterIdPostRequest
from openapi_client.models.chiogrp_id_post_request import ChiogrpIdPostRequest as ChiogrpIdPostRequest
from openapi_client.models.chip_id_post_request import ChipIdPostRequest as ChipIdPostRequest
from openapi_client.models.chiscsistorageport_id_post_request import ChiscsistorageportIdPostRequest as ChiscsistorageportIdPostRequest
from openapi_client.models.chkeyserver_id_post_request import ChkeyserverIdPostRequest as ChkeyserverIdPostRequest
from openapi_client.models.chkeyserverisklm_post_request import ChkeyserverisklmPostRequest as ChkeyserverisklmPostRequest
from openapi_client.models.chkeyserverkeysecure_post_request import ChkeyserverkeysecurePostRequest as ChkeyserverkeysecurePostRequest
from openapi_client.models.chldap_post_request import ChldapPostRequest as ChldapPostRequest
from openapi_client.models.chldapserver_id_post_request import ChldapserverIdPostRequest as ChldapserverIdPostRequest
from openapi_client.models.chlicense_post_request import ChlicensePostRequest as ChlicensePostRequest
from openapi_client.models.chmdisk_id_post_request import ChmdiskIdPostRequest as ChmdiskIdPostRequest
from openapi_client.models.chmdiskgrp_id_post_request import ChmdiskgrpIdPostRequest as ChmdiskgrpIdPostRequest
from openapi_client.models.chnode_id_post_request import ChnodeIdPostRequest as ChnodeIdPostRequest
from openapi_client.models.chnodebattery_id_post_request import ChnodebatteryIdPostRequest as ChnodebatteryIdPostRequest
from openapi_client.models.chnodebootdrive_id_post_request import ChnodebootdriveIdPostRequest as ChnodebootdriveIdPostRequest
from openapi_client.models.chnodehw_id_post_request import ChnodehwIdPostRequest as ChnodehwIdPostRequest
from openapi_client.models.chownershipgroup_id_post_request import ChownershipgroupIdPostRequest as ChownershipgroupIdPostRequest
from openapi_client.models.chpartition_id_post_request import ChpartitionIdPostRequest as ChpartitionIdPostRequest
from openapi_client.models.chpartitioncertstore_post_request import ChpartitioncertstorePostRequest as ChpartitioncertstorePostRequest
from openapi_client.models.chpartnership_id_post_request import ChpartnershipIdPostRequest as ChpartnershipIdPostRequest
from openapi_client.models.chportethernet_id_post_request import ChportethernetIdPostRequest as ChportethernetIdPostRequest
from openapi_client.models.chportfc_id_post_request import ChportfcIdPostRequest as ChportfcIdPostRequest
from openapi_client.models.chportset_id_post_request import ChportsetIdPostRequest as ChportsetIdPostRequest
from openapi_client.models.chprovisioningpolicy_id_post_request import ChprovisioningpolicyIdPostRequest as ChprovisioningpolicyIdPostRequest
from openapi_client.models.chproxy_post_request import ChproxyPostRequest as ChproxyPostRequest
from openapi_client.models.chquorum_id_post_request import ChquorumIdPostRequest as ChquorumIdPostRequest
from openapi_client.models.chrcconsistgrp_id_post_request import ChrcconsistgrpIdPostRequest as ChrcconsistgrpIdPostRequest
from openapi_client.models.chrcrelationship_id_post_request import ChrcrelationshipIdPostRequest as ChrcrelationshipIdPostRequest
from openapi_client.models.chsafeguardedpolicy_id_post_request import ChsafeguardedpolicyIdPostRequest as ChsafeguardedpolicyIdPostRequest
from openapi_client.models.chsecurity_post_request import ChsecurityPostRequest as ChsecurityPostRequest
from openapi_client.models.chsite_id_post_request import ChsiteIdPostRequest as ChsiteIdPostRequest
from openapi_client.models.chsnapshot_post_request import ChsnapshotPostRequest as ChsnapshotPostRequest
from openapi_client.models.chsnapshotpolicy_id_post_request import ChsnapshotpolicyIdPostRequest as ChsnapshotpolicyIdPostRequest
from openapi_client.models.chsnmpagent_post_request import ChsnmpagentPostRequest as ChsnmpagentPostRequest
from openapi_client.models.chsnmpserver_id_post_request import ChsnmpserverIdPostRequest as ChsnmpserverIdPostRequest
from openapi_client.models.chsra_post_request import ChsraPostRequest as ChsraPostRequest
from openapi_client.models.chsyslogserver_id_post_request import ChsyslogserverIdPostRequest as ChsyslogserverIdPostRequest
from openapi_client.models.chsystemcert_post_request import ChsystemcertPostRequest as ChsystemcertPostRequest
from openapi_client.models.chsystemcertstore_post_request import ChsystemcertstorePostRequest as ChsystemcertstorePostRequest
from openapi_client.models.chsystemethernet_post_request import ChsystemethernetPostRequest as ChsystemethernetPostRequest
from openapi_client.models.chsystemlimits_post_request import ChsystemlimitsPostRequest as ChsystemlimitsPostRequest
from openapi_client.models.chthrottle_id_post_request import ChthrottleIdPostRequest as ChthrottleIdPostRequest
from openapi_client.models.chtruststore_id_post_request import ChtruststoreIdPostRequest as ChtruststoreIdPostRequest
from openapi_client.models.chtwopersonintegrityrequest_post_request import ChtwopersonintegrityrequestPostRequest as ChtwopersonintegrityrequestPostRequest
from openapi_client.models.chuser_id_post_request import ChuserIdPostRequest as ChuserIdPostRequest
from openapi_client.models.chusergrp_id_post_request import ChusergrpIdPostRequest as ChusergrpIdPostRequest
from openapi_client.models.chvcenter_id_post_request import ChvcenterIdPostRequest as ChvcenterIdPostRequest
from openapi_client.models.chvdisk_id_post_request import ChvdiskIdPostRequest as ChvdiskIdPostRequest
from openapi_client.models.chvolume_id_post_request import ChvolumeIdPostRequest as ChvolumeIdPostRequest
from openapi_client.models.chvolumegroup_id_post_request import ChvolumegroupIdPostRequest as ChvolumegroupIdPostRequest
from openapi_client.models.chvolumegroupreplication_id_post_request import ChvolumegroupreplicationIdPostRequest as ChvolumegroupreplicationIdPostRequest
from openapi_client.models.chvolumegroupsnapshotbuffer_id_post_request import ChvolumegroupsnapshotbufferIdPostRequest as ChvolumegroupsnapshotbufferIdPostRequest
from openapi_client.models.chvolumegroupsnapshotpolicy_id_post_request import ChvolumegroupsnapshotpolicyIdPostRequest as ChvolumegroupsnapshotpolicyIdPostRequest
from openapi_client.models.cleardumps_id_post_request import CleardumpsIdPostRequest as CleardumpsIdPostRequest
from openapi_client.models.cleardumps_post_request import CleardumpsPostRequest as CleardumpsPostRequest
from openapi_client.models.clearenclosuredumps_id_post_request import ClearenclosuredumpsIdPostRequest as ClearenclosuredumpsIdPostRequest
from openapi_client.models.clearerrlog_post_request import ClearerrlogPostRequest as ClearerrlogPostRequest
from openapi_client.models.clearplugin_post_request import ClearpluginPostRequest as ClearpluginPostRequest
from openapi_client.models.converttoclone_post_request import ConverttoclonePostRequest as ConverttoclonePostRequest
from openapi_client.models.cpdumps_id_post_request import CpdumpsIdPostRequest as CpdumpsIdPostRequest
from openapi_client.models.cpenclosuredumps_id_post_request import CpenclosuredumpsIdPostRequest as CpenclosuredumpsIdPostRequest
from openapi_client.models.detectiscsistorageportcandidate_post_request import DetectiscsistorageportcandidatePostRequest as DetectiscsistorageportcandidatePostRequest
from openapi_client.models.detectmdisk_post_request import DetectmdiskPostRequest as DetectmdiskPostRequest
from openapi_client.models.download_post_request import DownloadPostRequest as DownloadPostRequest
from openapi_client.models.dumperrlog_post_request import DumperrlogPostRequest as DumperrlogPostRequest
from openapi_client.models.error import Error as Error
from openapi_client.models.expandarray_id_post_request import ExpandarrayIdPostRequest as ExpandarrayIdPostRequest
from openapi_client.models.expandvdisksize_id_post_request import ExpandvdisksizeIdPostRequest as ExpandvdisksizeIdPostRequest
from openapi_client.models.lsarray_id_post_request import LsarrayIdPostRequest as LsarrayIdPostRequest
from openapi_client.models.lsarray_post_request import LsarrayPostRequest as LsarrayPostRequest
from openapi_client.models.lsarrayexpansionprogress_id_post_request import LsarrayexpansionprogressIdPostRequest as LsarrayexpansionprogressIdPostRequest
from openapi_client.models.lsarrayexpansionprogress_post_request import LsarrayexpansionprogressPostRequest as LsarrayexpansionprogressPostRequest
from openapi_client.models.lsarrayinitprogress_id_post_request import LsarrayinitprogressIdPostRequest as LsarrayinitprogressIdPostRequest
from openapi_client.models.lsarrayinitprogress_post_request import LsarrayinitprogressPostRequest as LsarrayinitprogressPostRequest
from openapi_client.models.lsarraylba_post_request import LsarraylbaPostRequest as LsarraylbaPostRequest
from openapi_client.models.lsarraymember_id_post_request import LsarraymemberIdPostRequest as LsarraymemberIdPostRequest
from openapi_client.models.lsarraymember_post_request import LsarraymemberPostRequest as LsarraymemberPostRequest
from openapi_client.models.lsarraymembergoals_id_post_request import LsarraymembergoalsIdPostRequest as LsarraymembergoalsIdPostRequest
from openapi_client.models.lsarraymembergoals_post_request import LsarraymembergoalsPostRequest as LsarraymembergoalsPostRequest
from openapi_client.models.lsarraymemberprogress_id_post_request import LsarraymemberprogressIdPostRequest as LsarraymemberprogressIdPostRequest
from openapi_client.models.lsarraymemberprogress_post_request import LsarraymemberprogressPostRequest as LsarraymemberprogressPostRequest
from openapi_client.models.lsarrayrecommendation_id_post_request import LsarrayrecommendationIdPostRequest as LsarrayrecommendationIdPostRequest
from openapi_client.models.lsarraysyncprogress_id_post_request import LsarraysyncprogressIdPostRequest as LsarraysyncprogressIdPostRequest
from openapi_client.models.lsarraysyncprogress_post_request import LsarraysyncprogressPostRequest as LsarraysyncprogressPostRequest
from openapi_client.models.lsclusterstats_post_request import LsclusterstatsPostRequest as LsclusterstatsPostRequest
from openapi_client.models.lscontroller_id_post_request import LscontrollerIdPostRequest as LscontrollerIdPostRequest
from openapi_client.models.lscontroller_post_request import LscontrollerPostRequest as LscontrollerPostRequest
from openapi_client.models.lsdependentvdisks_post_request import LsdependentvdisksPostRequest as LsdependentvdisksPostRequest
from openapi_client.models.lsdiscoverystatus_post_request import LsdiscoverystatusPostRequest as LsdiscoverystatusPostRequest
from openapi_client.models.lsdrive_id_post_request import LsdriveIdPostRequest as LsdriveIdPostRequest
from openapi_client.models.lsdrive_post_request import LsdrivePostRequest as LsdrivePostRequest
from openapi_client.models.lsdriveclass_id_post_request import LsdriveclassIdPostRequest as LsdriveclassIdPostRequest
from openapi_client.models.lsdriveclass_post_request import LsdriveclassPostRequest as LsdriveclassPostRequest
from openapi_client.models.lsdrivelba_post_request import LsdrivelbaPostRequest as LsdrivelbaPostRequest
from openapi_client.models.lsdriveprogress_id_post_request import LsdriveprogressIdPostRequest as LsdriveprogressIdPostRequest
from openapi_client.models.lsdriveprogress_post_request import LsdriveprogressPostRequest as LsdriveprogressPostRequest
from openapi_client.models.lsdriveupgradeprogress_id_post_request import LsdriveupgradeprogressIdPostRequest as LsdriveupgradeprogressIdPostRequest
from openapi_client.models.lsdriveupgradeprogress_post_request import LsdriveupgradeprogressPostRequest as LsdriveupgradeprogressPostRequest
from openapi_client.models.lsdumps_id_post_request import LsdumpsIdPostRequest as LsdumpsIdPostRequest
from openapi_client.models.lsdumps_post_request import LsdumpsPostRequest as LsdumpsPostRequest
from openapi_client.models.lsemailuser_id_post_request import LsemailuserIdPostRequest as LsemailuserIdPostRequest
from openapi_client.models.lsemailuser_post_request import LsemailuserPostRequest as LsemailuserPostRequest
from openapi_client.models.lsenclosure_id_post_request import LsenclosureIdPostRequest as LsenclosureIdPostRequest
from openapi_client.models.lsenclosure_post_request import LsenclosurePostRequest as LsenclosurePostRequest
from openapi_client.models.lsenclosurecanister_id_post_request import LsenclosurecanisterIdPostRequest as LsenclosurecanisterIdPostRequest
from openapi_client.models.lsenclosurecanister_post_request import LsenclosurecanisterPostRequest as LsenclosurecanisterPostRequest
from openapi_client.models.lsenclosuredisplaypanel_id_post_request import LsenclosuredisplaypanelIdPostRequest as LsenclosuredisplaypanelIdPostRequest
from openapi_client.models.lsenclosuredisplaypanel_post_request import LsenclosuredisplaypanelPostRequest as LsenclosuredisplaypanelPostRequest
from openapi_client.models.lsenclosurefanmodule_id_post_request import LsenclosurefanmoduleIdPostRequest as LsenclosurefanmoduleIdPostRequest
from openapi_client.models.lsenclosurefanmodule_post_request import LsenclosurefanmodulePostRequest as LsenclosurefanmodulePostRequest
from openapi_client.models.lsenclosurepsu_id_post_request import LsenclosurepsuIdPostRequest as LsenclosurepsuIdPostRequest
from openapi_client.models.lsenclosurepsu_post_request import LsenclosurepsuPostRequest as LsenclosurepsuPostRequest
from openapi_client.models.lsenclosuresem_id_post_request import LsenclosuresemIdPostRequest as LsenclosuresemIdPostRequest
from openapi_client.models.lsenclosuresem_post_request import LsenclosuresemPostRequest as LsenclosuresemPostRequest
from openapi_client.models.lsenclosureslot_id_post_request import LsenclosureslotIdPostRequest as LsenclosureslotIdPostRequest
from openapi_client.models.lsenclosureslot_post_request import LsenclosureslotPostRequest as LsenclosureslotPostRequest
from openapi_client.models.lsenclosurestats_id_post_request import LsenclosurestatsIdPostRequest as LsenclosurestatsIdPostRequest
from openapi_client.models.lsenclosurestats_post_request import LsenclosurestatsPostRequest as LsenclosurestatsPostRequest
from openapi_client.models.lseventlog_id_post_request import LseventlogIdPostRequest as LseventlogIdPostRequest
from openapi_client.models.lseventlog_post_request import LseventlogPostRequest as LseventlogPostRequest
from openapi_client.models.lsfabric_post_request import LsfabricPostRequest as LsfabricPostRequest
from openapi_client.models.lsfabricport_id_post_request import LsfabricportIdPostRequest as LsfabricportIdPostRequest
from openapi_client.models.lsfabricport_post_request import LsfabricportPostRequest as LsfabricportPostRequest
from openapi_client.models.lsfcconsistgrp_id_post_request import LsfcconsistgrpIdPostRequest as LsfcconsistgrpIdPostRequest
from openapi_client.models.lsfcconsistgrp_post_request import LsfcconsistgrpPostRequest as LsfcconsistgrpPostRequest
from openapi_client.models.lsfcmap_id_post_request import LsfcmapIdPostRequest as LsfcmapIdPostRequest
from openapi_client.models.lsfcmap_post_request import LsfcmapPostRequest as LsfcmapPostRequest
from openapi_client.models.lsfcportsetmember_id_post_request import LsfcportsetmemberIdPostRequest as LsfcportsetmemberIdPostRequest
from openapi_client.models.lsfcportsetmember_post_request import LsfcportsetmemberPostRequest as LsfcportsetmemberPostRequest
from openapi_client.models.lshost_id_post_request import LshostIdPostRequest as LshostIdPostRequest
from openapi_client.models.lshost_post_request import LshostPostRequest as LshostPostRequest
from openapi_client.models.lshostcluster_id_post_request import LshostclusterIdPostRequest as LshostclusterIdPostRequest
from openapi_client.models.lshostcluster_post_request import LshostclusterPostRequest as LshostclusterPostRequest
from openapi_client.models.lshostiplogin_id_post_request import LshostiploginIdPostRequest as LshostiploginIdPostRequest
from openapi_client.models.lshostiplogin_post_request import LshostiploginPostRequest as LshostiploginPostRequest
from openapi_client.models.lshostzone_post_request import LshostzonePostRequest as LshostzonePostRequest
from openapi_client.models.lsiogrp_id_post_request import LsiogrpIdPostRequest as LsiogrpIdPostRequest
from openapi_client.models.lsiogrp_post_request import LsiogrpPostRequest as LsiogrpPostRequest
from openapi_client.models.lsip_id_post_request import LsipIdPostRequest as LsipIdPostRequest
from openapi_client.models.lsip_post_request import LsipPostRequest as LsipPostRequest
from openapi_client.models.lsiscsiauth_post_request import LsiscsiauthPostRequest as LsiscsiauthPostRequest
from openapi_client.models.lsiscsistorageport_id_post_request import LsiscsistorageportIdPostRequest as LsiscsistorageportIdPostRequest
from openapi_client.models.lsiscsistorageport_post_request import LsiscsistorageportPostRequest as LsiscsistorageportPostRequest
from openapi_client.models.lslocaldisk_id_post_request import LslocaldiskIdPostRequest as LslocaldiskIdPostRequest
from openapi_client.models.lslocaldisk_post_request import LslocaldiskPostRequest as LslocaldiskPostRequest
from openapi_client.models.lsmdisk_id_post_request import LsmdiskIdPostRequest as LsmdiskIdPostRequest
from openapi_client.models.lsmdisk_post_request import LsmdiskPostRequest as LsmdiskPostRequest
from openapi_client.models.lsmdiskgrp_id_post_request import LsmdiskgrpIdPostRequest as LsmdiskgrpIdPostRequest
from openapi_client.models.lsmdiskgrp_post_request import LsmdiskgrpPostRequest as LsmdiskgrpPostRequest
from openapi_client.models.lsmdisklba_post_request import LsmdisklbaPostRequest as LsmdisklbaPostRequest
from openapi_client.models.lsmetadatavdisk_post_request import LsmetadatavdiskPostRequest as LsmetadatavdiskPostRequest
from openapi_client.models.lsnode_id_post_request import LsnodeIdPostRequest as LsnodeIdPostRequest
from openapi_client.models.lsnode_post_request import LsnodePostRequest as LsnodePostRequest
from openapi_client.models.lsnodebattery_id_post_request import LsnodebatteryIdPostRequest as LsnodebatteryIdPostRequest
from openapi_client.models.lsnodebattery_post_request import LsnodebatteryPostRequest as LsnodebatteryPostRequest
from openapi_client.models.lsnodebootdrive_id_post_request import LsnodebootdriveIdPostRequest as LsnodebootdriveIdPostRequest
from openapi_client.models.lsnodebootdrive_post_request import LsnodebootdrivePostRequest as LsnodebootdrivePostRequest
from openapi_client.models.lsnodepsu_id_post_request import LsnodepsuIdPostRequest as LsnodepsuIdPostRequest
from openapi_client.models.lsnodepsu_post_request import LsnodepsuPostRequest as LsnodepsuPostRequest
from openapi_client.models.lsnodestats_id_post_request import LsnodestatsIdPostRequest as LsnodestatsIdPostRequest
from openapi_client.models.lsnodestats_post_request import LsnodestatsPostRequest as LsnodestatsPostRequest
from openapi_client.models.lsnvmefabric_post_request import LsnvmefabricPostRequest as LsnvmefabricPostRequest
from openapi_client.models.lsownershipgroup_id_post_request import LsownershipgroupIdPostRequest as LsownershipgroupIdPostRequest
from openapi_client.models.lsownershipgroup_post_request import LsownershipgroupPostRequest as LsownershipgroupPostRequest
from openapi_client.models.lspartition_id_post_request import LspartitionIdPostRequest as LspartitionIdPostRequest
from openapi_client.models.lspartition_post_request import LspartitionPostRequest as LspartitionPostRequest
from openapi_client.models.lspartnership_id_post_request import LspartnershipIdPostRequest as LspartnershipIdPostRequest
from openapi_client.models.lspartnership_post_request import LspartnershipPostRequest as LspartnershipPostRequest
from openapi_client.models.lsportethernet_id_post_request import LsportethernetIdPostRequest as LsportethernetIdPostRequest
from openapi_client.models.lsportethernet_post_request import LsportethernetPostRequest as LsportethernetPostRequest
from openapi_client.models.lsportfc_id_post_request import LsportfcIdPostRequest as LsportfcIdPostRequest
from openapi_client.models.lsportfc_post_request import LsportfcPostRequest as LsportfcPostRequest
from openapi_client.models.lsportib_id_post_request import LsportibIdPostRequest as LsportibIdPostRequest
from openapi_client.models.lsportib_post_request import LsportibPostRequest as LsportibPostRequest
from openapi_client.models.lsportip_id_post_request import LsportipIdPostRequest as LsportipIdPostRequest
from openapi_client.models.lsportip_post_request import LsportipPostRequest as LsportipPostRequest
from openapi_client.models.lsportsas_post_request import LsportsasPostRequest as LsportsasPostRequest
from openapi_client.models.lsportset_id_post_request import LsportsetIdPostRequest as LsportsetIdPostRequest
from openapi_client.models.lsportset_post_request import LsportsetPostRequest as LsportsetPostRequest
from openapi_client.models.lsportstats_id_post_request import LsportstatsIdPostRequest as LsportstatsIdPostRequest
from openapi_client.models.lsportstats_post_request import LsportstatsPostRequest as LsportstatsPostRequest
from openapi_client.models.lsportusb_id_post_request import LsportusbIdPostRequest as LsportusbIdPostRequest
from openapi_client.models.lsportusb_post_request import LsportusbPostRequest as LsportusbPostRequest
from openapi_client.models.lspotentialarraysize_id_post_request import LspotentialarraysizeIdPostRequest as LspotentialarraysizeIdPostRequest
from openapi_client.models.lsprovisioningpolicy_id_post_request import LsprovisioningpolicyIdPostRequest as LsprovisioningpolicyIdPostRequest
from openapi_client.models.lsprovisioningpolicy_post_request import LsprovisioningpolicyPostRequest as LsprovisioningpolicyPostRequest
from openapi_client.models.lsquorum_id_post_request import LsquorumIdPostRequest as LsquorumIdPostRequest
from openapi_client.models.lsquorum_post_request import LsquorumPostRequest as LsquorumPostRequest
from openapi_client.models.lsrcconsistgrp_id_post_request import LsrcconsistgrpIdPostRequest as LsrcconsistgrpIdPostRequest
from openapi_client.models.lsrcconsistgrp_post_request import LsrcconsistgrpPostRequest as LsrcconsistgrpPostRequest
from openapi_client.models.lsrcrelationship_id_post_request import LsrcrelationshipIdPostRequest as LsrcrelationshipIdPostRequest
from openapi_client.models.lsrcrelationship_post_request import LsrcrelationshipPostRequest as LsrcrelationshipPostRequest
from openapi_client.models.lsrcrelationshipcandidate_post_request import LsrcrelationshipcandidatePostRequest as LsrcrelationshipcandidatePostRequest
from openapi_client.models.lsrepairsevdiskcopyprogress_id_post_request import LsrepairsevdiskcopyprogressIdPostRequest as LsrepairsevdiskcopyprogressIdPostRequest
from openapi_client.models.lsrepairsevdiskcopyprogress_post_request import LsrepairsevdiskcopyprogressPostRequest as LsrepairsevdiskcopyprogressPostRequest
from openapi_client.models.lsrepairvdiskcopyprogress_id_post_request import LsrepairvdiskcopyprogressIdPostRequest as LsrepairvdiskcopyprogressIdPostRequest
from openapi_client.models.lsrepairvdiskcopyprogress_post_request import LsrepairvdiskcopyprogressPostRequest as LsrepairvdiskcopyprogressPostRequest
from openapi_client.models.lsreplicationpolicy_id_post_request import LsreplicationpolicyIdPostRequest as LsreplicationpolicyIdPostRequest
from openapi_client.models.lsreplicationpolicy_post_request import LsreplicationpolicyPostRequest as LsreplicationpolicyPostRequest
from openapi_client.models.lssafeguardedpolicy_id_post_request import LssafeguardedpolicyIdPostRequest as LssafeguardedpolicyIdPostRequest
from openapi_client.models.lssafeguardedpolicy_post_request import LssafeguardedpolicyPostRequest as LssafeguardedpolicyPostRequest
from openapi_client.models.lssafeguardedschedule_id_post_request import LssafeguardedscheduleIdPostRequest as LssafeguardedscheduleIdPostRequest
from openapi_client.models.lssafeguardedschedule_post_request import LssafeguardedschedulePostRequest as LssafeguardedschedulePostRequest
from openapi_client.models.lssasfabric_post_request import LssasfabricPostRequest as LssasfabricPostRequest
from openapi_client.models.lssevdiskcopy_id_post_request import LssevdiskcopyIdPostRequest as LssevdiskcopyIdPostRequest
from openapi_client.models.lssevdiskcopy_post_request import LssevdiskcopyPostRequest as LssevdiskcopyPostRequest
from openapi_client.models.lssnapshotpolicy_id_post_request import LssnapshotpolicyIdPostRequest as LssnapshotpolicyIdPostRequest
from openapi_client.models.lssnapshotpolicy_post_request import LssnapshotpolicyPostRequest as LssnapshotpolicyPostRequest
from openapi_client.models.lssnapshotschedule_id_post_request import LssnapshotscheduleIdPostRequest as LssnapshotscheduleIdPostRequest
from openapi_client.models.lssnapshotschedule_post_request import LssnapshotschedulePostRequest as LssnapshotschedulePostRequest
from openapi_client.models.lstargetportfc_id_post_request import LstargetportfcIdPostRequest as LstargetportfcIdPostRequest
from openapi_client.models.lstargetportfc_post_request import LstargetportfcPostRequest as LstargetportfcPostRequest
from openapi_client.models.lsthrottle_id_post_request import LsthrottleIdPostRequest as LsthrottleIdPostRequest
from openapi_client.models.lsthrottle_post_request import LsthrottlePostRequest as LsthrottlePostRequest
from openapi_client.models.lstruststore_id_post_request import LstruststoreIdPostRequest as LstruststoreIdPostRequest
from openapi_client.models.lstruststore_post_request import LstruststorePostRequest as LstruststorePostRequest
from openapi_client.models.lsuser_id_post_request import LsuserIdPostRequest as LsuserIdPostRequest
from openapi_client.models.lsuser_post_request import LsuserPostRequest as LsuserPostRequest
from openapi_client.models.lsusergrp_id_post_request import LsusergrpIdPostRequest as LsusergrpIdPostRequest
from openapi_client.models.lsusergrp_post_request import LsusergrpPostRequest as LsusergrpPostRequest
from openapi_client.models.lsvasaclientcertificate_id_post_request import LsvasaclientcertificateIdPostRequest as LsvasaclientcertificateIdPostRequest
from openapi_client.models.lsvasaclientcertificate_post_request import LsvasaclientcertificatePostRequest as LsvasaclientcertificatePostRequest
from openapi_client.models.lsvcenter_id_post_request import LsvcenterIdPostRequest as LsvcenterIdPostRequest
from openapi_client.models.lsvcenter_post_request import LsvcenterPostRequest as LsvcenterPostRequest
from openapi_client.models.lsvdisk_id_post_request import LsvdiskIdPostRequest as LsvdiskIdPostRequest
from openapi_client.models.lsvdisk_post_request import LsvdiskPostRequest as LsvdiskPostRequest
from openapi_client.models.lsvdiskaccess_id_post_request import LsvdiskaccessIdPostRequest as LsvdiskaccessIdPostRequest
from openapi_client.models.lsvdiskaccess_post_request import LsvdiskaccessPostRequest as LsvdiskaccessPostRequest
from openapi_client.models.lsvdiskanalysis_id_post_request import LsvdiskanalysisIdPostRequest as LsvdiskanalysisIdPostRequest
from openapi_client.models.lsvdiskanalysis_post_request import LsvdiskanalysisPostRequest as LsvdiskanalysisPostRequest
from openapi_client.models.lsvdiskcopy_id_post_request import LsvdiskcopyIdPostRequest as LsvdiskcopyIdPostRequest
from openapi_client.models.lsvdiskcopy_post_request import LsvdiskcopyPostRequest as LsvdiskcopyPostRequest
from openapi_client.models.lsvdiskextent_id_post_request import LsvdiskextentIdPostRequest as LsvdiskextentIdPostRequest
from openapi_client.models.lsvdisklba_post_request import LsvdisklbaPostRequest as LsvdisklbaPostRequest
from openapi_client.models.lsvdiskmember_id_post_request import LsvdiskmemberIdPostRequest as LsvdiskmemberIdPostRequest
from openapi_client.models.lsvdisksyncprogress_id_post_request import LsvdisksyncprogressIdPostRequest as LsvdisksyncprogressIdPostRequest
from openapi_client.models.lsvdisksyncprogress_post_request import LsvdisksyncprogressPostRequest as LsvdisksyncprogressPostRequest
from openapi_client.models.lsvdisktiers_id_post_request import LsvdisktiersIdPostRequest as LsvdisktiersIdPostRequest
from openapi_client.models.lsvdisktiers_post_request import LsvdisktiersPostRequest as LsvdisktiersPostRequest
from openapi_client.models.lsvdiskunsharedchunks_id_post_request import LsvdiskunsharedchunksIdPostRequest as LsvdiskunsharedchunksIdPostRequest
from openapi_client.models.lsvolumebackup_post_request import LsvolumebackupPostRequest as LsvolumebackupPostRequest
from openapi_client.models.lsvolumebackupgeneration_post_request import LsvolumebackupgenerationPostRequest as LsvolumebackupgenerationPostRequest
from openapi_client.models.lsvolumebackupprogress_post_request import LsvolumebackupprogressPostRequest as LsvolumebackupprogressPostRequest
from openapi_client.models.lsvolumegroup_id_post_request import LsvolumegroupIdPostRequest as LsvolumegroupIdPostRequest
from openapi_client.models.lsvolumegroup_post_request import LsvolumegroupPostRequest as LsvolumegroupPostRequest
from openapi_client.models.lsvolumegrouppopulation_id_post_request import LsvolumegrouppopulationIdPostRequest as LsvolumegrouppopulationIdPostRequest
from openapi_client.models.lsvolumegrouppopulation_post_request import LsvolumegrouppopulationPostRequest as LsvolumegrouppopulationPostRequest
from openapi_client.models.lsvolumegroupreplication_id_post_request import LsvolumegroupreplicationIdPostRequest as LsvolumegroupreplicationIdPostRequest
from openapi_client.models.lsvolumegroupreplication_post_request import LsvolumegroupreplicationPostRequest as LsvolumegroupreplicationPostRequest
from openapi_client.models.lsvolumegroupsnapshot_post_request import LsvolumegroupsnapshotPostRequest as LsvolumegroupsnapshotPostRequest
from openapi_client.models.lsvolumegroupsnapshotpolicy_id_post_request import LsvolumegroupsnapshotpolicyIdPostRequest as LsvolumegroupsnapshotpolicyIdPostRequest
from openapi_client.models.lsvolumegroupsnapshotpolicy_post_request import LsvolumegroupsnapshotpolicyPostRequest as LsvolumegroupsnapshotpolicyPostRequest
from openapi_client.models.lsvolumegroupsnapshotschedule_id_post_request import LsvolumegroupsnapshotscheduleIdPostRequest as LsvolumegroupsnapshotscheduleIdPostRequest
from openapi_client.models.lsvolumegroupsnapshotschedule_post_request import LsvolumegroupsnapshotschedulePostRequest as LsvolumegroupsnapshotschedulePostRequest
from openapi_client.models.lsvolumepopulation_id_post_request import LsvolumepopulationIdPostRequest as LsvolumepopulationIdPostRequest
from openapi_client.models.lsvolumepopulation_post_request import LsvolumepopulationPostRequest as LsvolumepopulationPostRequest
from openapi_client.models.lsvolumerestoreprogress_id_post_request import LsvolumerestoreprogressIdPostRequest as LsvolumerestoreprogressIdPostRequest
from openapi_client.models.lsvolumerestoreprogress_post_request import LsvolumerestoreprogressPostRequest as LsvolumerestoreprogressPostRequest
from openapi_client.models.lsvolumesnapshot_id_post_request import LsvolumesnapshotIdPostRequest as LsvolumesnapshotIdPostRequest
from openapi_client.models.lsvolumesnapshot_post_request import LsvolumesnapshotPostRequest as LsvolumesnapshotPostRequest
from openapi_client.models.mergepartition_id_post_request import MergepartitionIdPostRequest as MergepartitionIdPostRequest
from openapi_client.models.migrateexts_post_request import MigrateextsPostRequest as MigrateextsPostRequest
from openapi_client.models.migratetoimage_post_request import MigratetoimagePostRequest as MigratetoimagePostRequest
from openapi_client.models.migratevdisk_post_request import MigratevdiskPostRequest as MigratevdiskPostRequest
from openapi_client.models.mkarray_id_post_request import MkarrayIdPostRequest as MkarrayIdPostRequest
from openapi_client.models.mkarray_post_request import MkarrayPostRequest as MkarrayPostRequest
from openapi_client.models.mkcloudaccountawss3_post_request import Mkcloudaccountawss3PostRequest as Mkcloudaccountawss3PostRequest
from openapi_client.models.mkcloudaccountazure_post_request import MkcloudaccountazurePostRequest as MkcloudaccountazurePostRequest
from openapi_client.models.mkcloudaccountswift_post_request import MkcloudaccountswiftPostRequest as MkcloudaccountswiftPostRequest
from openapi_client.models.mkcluster_post_request import MkclusterPostRequest as MkclusterPostRequest
from openapi_client.models.mkdistributedarray_id_post_request import MkdistributedarrayIdPostRequest as MkdistributedarrayIdPostRequest
from openapi_client.models.mkdnsserver_post_request import MkdnsserverPostRequest as MkdnsserverPostRequest
from openapi_client.models.mkemailserver_post_request import MkemailserverPostRequest as MkemailserverPostRequest
from openapi_client.models.mkemailuser_post_request import MkemailuserPostRequest as MkemailuserPostRequest
from openapi_client.models.mkfcconsistgrp_post_request import MkfcconsistgrpPostRequest as MkfcconsistgrpPostRequest
from openapi_client.models.mkfcmap_post_request import MkfcmapPostRequest as MkfcmapPostRequest
from openapi_client.models.mkfcpartnership_id_post_request import MkfcpartnershipIdPostRequest as MkfcpartnershipIdPostRequest
from openapi_client.models.mkhost_post_request import MkhostPostRequest as MkhostPostRequest
from openapi_client.models.mkhostcluster_post_request import MkhostclusterPostRequest as MkhostclusterPostRequest
from openapi_client.models.mkimagevolume_post_request import MkimagevolumePostRequest as MkimagevolumePostRequest
from openapi_client.models.mkip_post_request import MkipPostRequest as MkipPostRequest
from openapi_client.models.mkippartnership_post_request import MkippartnershipPostRequest as MkippartnershipPostRequest
from openapi_client.models.mkkeyserver_post_request import MkkeyserverPostRequest as MkkeyserverPostRequest
from openapi_client.models.mkldapserver_post_request import MkldapserverPostRequest as MkldapserverPostRequest
from openapi_client.models.mkmdiskgrp_post_request import MkmdiskgrpPostRequest as MkmdiskgrpPostRequest
from openapi_client.models.mkmetadatavdisk_post_request import MkmetadatavdiskPostRequest as MkmetadatavdiskPostRequest
from openapi_client.models.mkownershipgroup_post_request import MkownershipgroupPostRequest as MkownershipgroupPostRequest
from openapi_client.models.mkpartition_post_request import MkpartitionPostRequest as MkpartitionPostRequest
from openapi_client.models.mkpartitioncertstore_post_request import MkpartitioncertstorePostRequest as MkpartitioncertstorePostRequest
from openapi_client.models.mkportset_post_request import MkportsetPostRequest as MkportsetPostRequest
from openapi_client.models.mkprovisioningpolicy_post_request import MkprovisioningpolicyPostRequest as MkprovisioningpolicyPostRequest
from openapi_client.models.mkproxy_post_request import MkproxyPostRequest as MkproxyPostRequest
from openapi_client.models.mkquorumapp_post_request import MkquorumappPostRequest as MkquorumappPostRequest
from openapi_client.models.mkrcconsistgrp_post_request import MkrcconsistgrpPostRequest as MkrcconsistgrpPostRequest
from openapi_client.models.mkrcrelationship_post_request import MkrcrelationshipPostRequest as MkrcrelationshipPostRequest
from openapi_client.models.mkreplicationpolicy_post_request import MkreplicationpolicyPostRequest as MkreplicationpolicyPostRequest
from openapi_client.models.mksafeguardedpolicy_post_request import MksafeguardedpolicyPostRequest as MksafeguardedpolicyPostRequest
from openapi_client.models.mksnapshotpolicy_post_request import MksnapshotpolicyPostRequest as MksnapshotpolicyPostRequest
from openapi_client.models.mksnmpserver_post_request import MksnmpserverPostRequest as MksnmpserverPostRequest
from openapi_client.models.mksyslogserver_post_request import MksyslogserverPostRequest as MksyslogserverPostRequest
from openapi_client.models.mksystemcertstore_post_request import MksystemcertstorePostRequest as MksystemcertstorePostRequest
from openapi_client.models.mksystemsupportcenter_post_request import MksystemsupportcenterPostRequest as MksystemsupportcenterPostRequest
from openapi_client.models.mkthrottle_post_request import MkthrottlePostRequest as MkthrottlePostRequest
from openapi_client.models.mktruststore_post_request import MktruststorePostRequest as MktruststorePostRequest
from openapi_client.models.mktwopersonintegrityrequest_post_request import MktwopersonintegrityrequestPostRequest as MktwopersonintegrityrequestPostRequest
from openapi_client.models.mkuser_post_request import MkuserPostRequest as MkuserPostRequest
from openapi_client.models.mkusergrp_post_request import MkusergrpPostRequest as MkusergrpPostRequest
from openapi_client.models.mkvasaclientcertificate_post_request import MkvasaclientcertificatePostRequest as MkvasaclientcertificatePostRequest
from openapi_client.models.mkvcenter_post_request import MkvcenterPostRequest as MkvcenterPostRequest
from openapi_client.models.mkvdisk_post_request import MkvdiskPostRequest as MkvdiskPostRequest
from openapi_client.models.mkvdiskhostmap_id_post_request import MkvdiskhostmapIdPostRequest as MkvdiskhostmapIdPostRequest
from openapi_client.models.mkvolume_post_request import MkvolumePostRequest as MkvolumePostRequest
from openapi_client.models.mkvolumegroup_post_request import MkvolumegroupPostRequest as MkvolumegroupPostRequest
from openapi_client.models.mkvolumehostclustermap_id_post_request import MkvolumehostclustermapIdPostRequest as MkvolumehostclustermapIdPostRequest
from openapi_client.models.movevdisk_id_post_request import MovevdiskIdPostRequest as MovevdiskIdPostRequest
from openapi_client.models.prestartfcconsistgrp_id_post_request import PrestartfcconsistgrpIdPostRequest as PrestartfcconsistgrpIdPostRequest
from openapi_client.models.prestartfcmap_id_post_request import PrestartfcmapIdPostRequest as PrestartfcmapIdPostRequest
from openapi_client.models.recoverarray_id_post_request import RecoverarrayIdPostRequest as RecoverarrayIdPostRequest
from openapi_client.models.recovervdisk_id_post_request import RecovervdiskIdPostRequest as RecovervdiskIdPostRequest
from openapi_client.models.refreshfromsnapshot_post_request import RefreshfromsnapshotPostRequest as RefreshfromsnapshotPostRequest
from openapi_client.models.registerplugin_post_request import RegisterpluginPostRequest as RegisterpluginPostRequest
from openapi_client.models.registervcenter_id_post_request import RegistervcenterIdPostRequest as RegistervcenterIdPostRequest
from openapi_client.models.repairsevdiskcopy_id_post_request import RepairsevdiskcopyIdPostRequest as RepairsevdiskcopyIdPostRequest
from openapi_client.models.repairvdiskcopy_id_post_request import RepairvdiskcopyIdPostRequest as RepairvdiskcopyIdPostRequest
from openapi_client.models.restorefromsnapshot_post_request import RestorefromsnapshotPostRequest as RestorefromsnapshotPostRequest
from openapi_client.models.restorevolume_id_post_request import RestorevolumeIdPostRequest as RestorevolumeIdPostRequest
from openapi_client.models.rmarray_id_post_request import RmarrayIdPostRequest as RmarrayIdPostRequest
from openapi_client.models.rmarray_post_request import RmarrayPostRequest as RmarrayPostRequest
from openapi_client.models.rmfcconsistgrp_id_post_request import RmfcconsistgrpIdPostRequest as RmfcconsistgrpIdPostRequest
from openapi_client.models.rmfcmap_id_post_request import RmfcmapIdPostRequest as RmfcmapIdPostRequest
from openapi_client.models.rmfcportsetmember_post_request import RmfcportsetmemberPostRequest as RmfcportsetmemberPostRequest
from openapi_client.models.rmhost_id_post_request import RmhostIdPostRequest as RmhostIdPostRequest
from openapi_client.models.rmhostcluster_id_post_request import RmhostclusterIdPostRequest as RmhostclusterIdPostRequest
from openapi_client.models.rmhostclustermember_id_post_request import RmhostclustermemberIdPostRequest as RmhostclustermemberIdPostRequest
from openapi_client.models.rmhostport_id_post_request import RmhostportIdPostRequest as RmhostportIdPostRequest
from openapi_client.models.rmmdisk_id_post_request import RmmdiskIdPostRequest as RmmdiskIdPostRequest
from openapi_client.models.rmmdiskgrp_id_post_request import RmmdiskgrpIdPostRequest as RmmdiskgrpIdPostRequest
from openapi_client.models.rmmetadatavdisk_post_request import RmmetadatavdiskPostRequest as RmmetadatavdiskPostRequest
from openapi_client.models.rmnode_id_post_request import RmnodeIdPostRequest as RmnodeIdPostRequest
from openapi_client.models.rmownershipgroup_id_post_request import RmownershipgroupIdPostRequest as RmownershipgroupIdPostRequest
from openapi_client.models.rmpartition_id_post_request import RmpartitionIdPostRequest as RmpartitionIdPostRequest
from openapi_client.models.rmportip_id_post_request import RmportipIdPostRequest as RmportipIdPostRequest
from openapi_client.models.rmrcconsistgrp_id_post_request import RmrcconsistgrpIdPostRequest as RmrcconsistgrpIdPostRequest
from openapi_client.models.rmrcrelationship_id_post_request import RmrcrelationshipIdPostRequest as RmrcrelationshipIdPostRequest
from openapi_client.models.rmsafeguardedpolicy_id_post_request import RmsafeguardedpolicyIdPostRequest as RmsafeguardedpolicyIdPostRequest
from openapi_client.models.rmsnapshot_post_request import RmsnapshotPostRequest as RmsnapshotPostRequest
from openapi_client.models.rmsnapshotpolicy_id_post_request import RmsnapshotpolicyIdPostRequest as RmsnapshotpolicyIdPostRequest
from openapi_client.models.rmusergrp_id_post_request import RmusergrpIdPostRequest as RmusergrpIdPostRequest
from openapi_client.models.rmvasaclientcertificate_post_request import RmvasaclientcertificatePostRequest as RmvasaclientcertificatePostRequest
from openapi_client.models.rmvcenter_id_post_request import RmvcenterIdPostRequest as RmvcenterIdPostRequest
from openapi_client.models.rmvdisk_id_post_request import RmvdiskIdPostRequest as RmvdiskIdPostRequest
from openapi_client.models.rmvdiskaccess_id_post_request import RmvdiskaccessIdPostRequest as RmvdiskaccessIdPostRequest
from openapi_client.models.rmvdiskcopy_id_post_request import RmvdiskcopyIdPostRequest as RmvdiskcopyIdPostRequest
from openapi_client.models.rmvdiskhostmap_id_post_request import RmvdiskhostmapIdPostRequest as RmvdiskhostmapIdPostRequest
from openapi_client.models.rmvolume_id_post_request import RmvolumeIdPostRequest as RmvolumeIdPostRequest
from openapi_client.models.rmvolumebackupgeneration_post_request import RmvolumebackupgenerationPostRequest as RmvolumebackupgenerationPostRequest
from openapi_client.models.rmvolumecopy_id_post_request import RmvolumecopyIdPostRequest as RmvolumecopyIdPostRequest
from openapi_client.models.rmvolumegroup_id_post_request import RmvolumegroupIdPostRequest as RmvolumegroupIdPostRequest
from openapi_client.models.rmvolumehostclustermap_id_post_request import RmvolumehostclustermapIdPostRequest as RmvolumehostclustermapIdPostRequest
from openapi_client.models.sendcloudcallhome_post_request import SendcloudcallhomePostRequest as SendcloudcallhomePostRequest
from openapi_client.models.setlocale_post_request import SetlocalePostRequest as SetlocalePostRequest
from openapi_client.models.setpwdreset_post_request import SetpwdresetPostRequest as SetpwdresetPostRequest
from openapi_client.models.settimezone_post_request import SettimezonePostRequest as SettimezonePostRequest
from openapi_client.models.shrinkvdisksize_id_post_request import ShrinkvdisksizeIdPostRequest as ShrinkvdisksizeIdPostRequest
from openapi_client.models.splitvdiskcopy_id_post_request import SplitvdiskcopyIdPostRequest as SplitvdiskcopyIdPostRequest
from openapi_client.models.startfcconsistgrp_id_post_request import StartfcconsistgrpIdPostRequest as StartfcconsistgrpIdPostRequest
from openapi_client.models.startfcmap_id_post_request import StartfcmapIdPostRequest as StartfcmapIdPostRequest
from openapi_client.models.startrcconsistgrp_id_post_request import StartrcconsistgrpIdPostRequest as StartrcconsistgrpIdPostRequest
from openapi_client.models.startrcrelationship_id_post_request import StartrcrelationshipIdPostRequest as StartrcrelationshipIdPostRequest
from openapi_client.models.startstats_post_request import StartstatsPostRequest as StartstatsPostRequest
from openapi_client.models.stopfcconsistgrp_id_post_request import StopfcconsistgrpIdPostRequest as StopfcconsistgrpIdPostRequest
from openapi_client.models.stopfcmap_id_post_request import StopfcmapIdPostRequest as StopfcmapIdPostRequest
from openapi_client.models.stoprcconsistgrp_id_post_request import StoprcconsistgrpIdPostRequest as StoprcconsistgrpIdPostRequest
from openapi_client.models.stoprcrelationship_id_post_request import StoprcrelationshipIdPostRequest as StoprcrelationshipIdPostRequest
from openapi_client.models.svc_livedump_post_request import SvcLivedumpPostRequest as SvcLivedumpPostRequest
from openapi_client.models.svc_snap_post_request import SvcSnapPostRequest as SvcSnapPostRequest
from openapi_client.models.svcsearch_post_request import SvcsearchPostRequest as SvcsearchPostRequest
from openapi_client.models.svcupgradetest_post_request import SvcupgradetestPostRequest as SvcupgradetestPostRequest
from openapi_client.models.swapnode_id_post_request import SwapnodeIdPostRequest as SwapnodeIdPostRequest
from openapi_client.models.switchrcconsistgrp_id_post_request import SwitchrcconsistgrpIdPostRequest as SwitchrcconsistgrpIdPostRequest
from openapi_client.models.switchrcrelationship_id_post_request import SwitchrcrelationshipIdPostRequest as SwitchrcrelationshipIdPostRequest
from openapi_client.models.testemail_id_post_request import TestemailIdPostRequest as TestemailIdPostRequest
from openapi_client.models.testemail_post_request import TestemailPostRequest as TestemailPostRequest
from openapi_client.models.testldapserver_id_post_request import TestldapserverIdPostRequest as TestldapserverIdPostRequest
from openapi_client.models.testldapserver_post_request import TestldapserverPostRequest as TestldapserverPostRequest
from openapi_client.models.testsnmpserver_id_post_request import TestsnmpserverIdPostRequest as TestsnmpserverIdPostRequest
from openapi_client.models.testsnmpserver_post_request import TestsnmpserverPostRequest as TestsnmpserverPostRequest
from openapi_client.models.traceroute_id_post_request import TracerouteIdPostRequest as TracerouteIdPostRequest
from openapi_client.models.traceroute_post_request import TraceroutePostRequest as TraceroutePostRequest
from openapi_client.models.triggerenclosuredump_post_request import TriggerenclosuredumpPostRequest as TriggerenclosuredumpPostRequest
from openapi_client.models.writesernum_id_post_request import WritesernumIdPostRequest as WritesernumIdPostRequest


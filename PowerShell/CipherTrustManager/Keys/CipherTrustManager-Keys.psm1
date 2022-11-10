#######################################################################################################################
# File:             CipherTrustManager-Keys.psm1                                                                    #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
# Notes:            This module is loaded by the master module, CIpherTrustManager                                    #
#                   Do not load this directly                                                                         #
#######################################################################################################################

####
# Local Variables
####
$target_uri = "/vault/keys2"
$target_search_uri = "/vault/query-keys/"
####



<#
    .SYNOPSIS
        Create a key in CipherTrust Manager
    .DESCRIPTION
        This allows you to create a new key on CIpherTrust Manager and control a series of its parameters. Those parameters include: keyname, usageMask, algo, size, Undeleteable, Unexportable, NoVersionedKey
    .EXAMPLE
        PS> Get-CM_CreateKey -keyname <keyname> -usageMask <usageMask> -algorithm <algorithm> -size <size>

        This shows the minimum parameters necessary to create a key. By default, this key will be created as a versioned key that can be exported and can be deleted
    .EXAMPLE
        PS> Get-CM_CreateKey -keyname $keyname -usageMask $usageMask -algorithm $algorithm -size $size -Undeleteable

        This shows the minimum parameters necessary to create a key that CANNOT BE DELETED. By default, this key will be created as a versioned key that can be exported
    .EXAMPLE
        PS> Get-CM_CreateKey -keyname $keyname -usageMask $usageMask -algorithm $algorithm -size $size -Unexportable

        This shows the minimum parameters necessary to create a key that CANNOT BE EXPORTED. By default, this key will be created as a versioned key that can be deleted
    .EXAMPLE
        PS> Get-CM_CreateKey -keyname $keyname -usageMask $usageMask -algorithm $algorithm -size $size -NoVersionedKey

        This shows the minimum parameters necessary to create a key with NO VERSION CONTROL. By default, this key will be created can be exported and can be deleted
    .LINK
        https://github.com/thalescpl-io/whatever_this_repo_is
#>
function Get-CM_CreateKey {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $keyname, 
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [int] $usageMask, 
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [Alias("algo")]
        [string] $algorithm, 
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [int] $size,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [switch] $Unexportable = $false,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [switch] $Undeletable = $false,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [switch] $NoVersionedKey = $false
    )

    Write-Debug "Creating a Key in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"
    $keyID = $null

    $body = @{
        'name'         = "$keyname"
        'usageMask'    = $usageMask
        'algorithm'    = "$algorithm"
        'size'         = 256
        'unexportable' = If ($Unexportable) { $true } else { $false }
        'undeletable'  = If ($Undeletable) { $true } else { $false }
        'meta'         = @{
            'ownerId'      = 'local|312c1485-aa03-454c-8591-6bd41509d846'
            'versionedKey' = If ($NoVersionedKey) { $false } else { $true }
        }
    }
    $jsonBody = $body | ConvertTo-Json -Depth 5
    Write-Debug "JSON Body: $($jsonBody)"

    Try {
        Test-CM_JWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer " + $CM_Session.AuthToken
        }
        Write-Debug "Headers: $($headers)"    
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'Post' -Uri $endpoint -Body $jsonBody -Headers $headers -ContentType 'application/json'
        Write-Debug "Response: $($response)"  
        $keyID = $response.id
    }
    Catch {
        $StatusCode = $_.Exception.Response.StatusCode
        if ($StatusCode -EQ [System.Net.HttpStatusCode]::Conflict) {
            Write-Error "Conflict: Key already exists by that name"
            return
        }
        else {
            Write-Error "Expected 200, got $([int]$StatusCode)" -ErrorAction Stop
            return
        }
    }

    Write-Debug $keyID
    return $keyID
}    

#             "uri": [
#                 string
#             ]
#         },
#         "issuerDNFields": {
#             "c": [
#                 string
#             ],
#             "cn": string,
#             "dc": [
#                 string
#             ],
#             "dnq": [
#                 string
#             ],
#             "email": [
#                 string
#             ],
#             "l": [
#                 string
#             ],
#             "o": [
#                 string
#             ],
#             "ou": [
#                 string
#             ],
#             "sn": string,
#             "st": [
#                 string
#             ],
#             "street": [
#                 string
#             ],
#             "t": [
#                 string
#             ],
#             "uid": [
#                 string
#             ]
#         },
#         "serialNumber": string,
#         "subjectANFields": {
#             "dns": [
#                 string
#             ],
#             "emailAddress": [
#                 string
#             ],
#             "ipAddress": [
#                 string
#             ],
#             "uri": [
#                 string
#             ]
#         },
#         "subjectDNFields": {
#             "c": [
#                 string
#             ],
#             "cn": string,
#             "dc": [
#                 string
#             ],
#             "dnq": [
#                 string
#             ],
#             "email": [
#                 string
#             ],
#             "l": [
#                 string
#             ],
#             "o": [
#                 string
#             ],
#             "ou": [
#                 string
#             ],
#             "sn": string,
#             "st": [
#                 string
#             ],
#             "street": [
#                 string
#             ],
#             "t": [
#                 string
#             ],
#             "uid": [
#                 string
#             ]
#         },
#         "x509SerialNumber": string
#     },
#     "compareIDWithUUID": string,
#     "compromiseAfter": string,
#     "compromiseAt": string,
#     "compromiseBefore": string,
#     "compromiseOccurranceAfter": string,
#     "compromiseOccurranceAt": string,
#     "compromiseOccurranceBefore": string,
#     "createdAfter": string,
#     "createdAt": string,
#     "createdBefore": string,
#     "curveIDs": [
#         string
#     ],
#     "deactivationAfter": string,
#     "deactivationAt": string,
#     "deactivationBefore": string,
#     "destroyAfter": string,
#     "destroyAt": string,
#     "destroyBefore": string,
#     "id": string,
#     "labels": {    },
#     "limit": integer,
#     "linkTypes": [
#         string
#     ],
#     "metaContains": string,
#     "neverExportable": boolean,
#     "neverExported": boolean,
#     "objectTypes": [
#         string
#     ],
#     "processStartAfter": string,
#     "processStartAt": string,
#     "processStartBefore": string,
#     "protectStopAfter": string,
#     "protectStopAt": string,
#     "protectStopBefore": string,
#     "returnOnlyIDs": boolean,
#     "revocationReason": string,
#     "revocationReasons": [
#         string
#     ],
#     "rotationDateReached": boolean,
#     "sha1Fingerprint": string,
#     "sha1Fingerprints": [
#         string
#     ],
#     "sha256Fingerprint": string,
#     "sha256Fingerprints": [
#         string
#     ],
#     "size": integer,
#     "sizes": [
#         integer
#     ],
#     "skip": integer,
#     "states": [
#         string
#     ],
#     "unexportable": boolean,
#     "updatedAfter": string,
#     "updatedAt": string,
#     "updatedBefore": string,
#     "uri": string,
#     "usageMasks": [
#         integer
#     ],
#     "version": integer,
#     "versions": [
#         integer
#     ]
# }

<#
    .SYNOPSIS
        Get-CM_ListKeys
    .DESCRIPTION
        Returns a list of keys. 
#    .PARAMETER server
##    Specifies the IP Address or FQDN of CipherTrust Manager.
#
#    .PARAMETER credential
#    Specifies the "credential (username/password) authorized to connect with CipherTrust manager.
#
#    .INPUTS
#    None. You cannot pipe objects to Connect-CipherTrustManager.
#
#    .OUTPUTS
#    None. Connect-CipherTrustManager returns a proxy to this connection.
#
#    .EXAMPLE
#    PS> Connect-CipherTrustManager -server 10.23.104.40 -user "user1" -pass "P@ssw0rd!"
#
#    .LINK
#    Online version: <github docs>
#>


function Get-CM_ListKeys {
    param
    (
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [string] $keyname, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [int] $usageMask, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [Alias("algo")]
        [string] $algorithm, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [int] $size,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [switch] $Unexportable,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [switch] $Undeletable
    )

    Write-Debug "Getting a List of Keys configured in CM"
    $endpoint = $CM_Session.REST_URL + $target_search_uri
    Write-Debug "Endpoint: $($endpoint)"

    # Mandatory Parameters
    $body = @{}

    # Optional Parameters
    if ($keyname) { $body.add('name', $keyname) }
    if ($usageMask) { $body.add('usageMask', $usageMask) }
    if ($algorithm) { $body.add('algorithm', $algorithm) }
    if ($size) { $body.add('size', $size) }

    if ($Unexportable) { $body.add('unexportable', $true) }
    if ($Undeletable) { $body.add('undeletable', $true) }
    
    $jsonBody = $body | ConvertTo-Json -Depth 5
    Write-Debug "JSON Body: $($jsonBody)"

    Try {
        Test-CM_JWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: $($headers)"    
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'POST' -Uri $endpoint -Body $jsonBody -Headers $headers -ContentType 'application/json'
        Write-Debug "Headers: $($response)"    
    }
    Catch {
        $StatusCode = $_.Exception.Response.StatusCode
        if ($StatusCode -EQ [System.Net.HttpStatusCode]::Conflict) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): User set already exists"
            return
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::Unauthorized) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to connect to CipherTrust Manager with current credentials"
            return
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::NotFound) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to find a Key by those parameters to delete"
            return
        }
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "List of Keys created"
    return $response
}    


function Get-CM_DeleteKey {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $key_id
    )

    Write-Debug "Deleting a Key by ID in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"

    #Set ID
    $endpoint += "/$key_id"

    Write-Debug "Endpoint with ID: $($endpoint)"

    Try {
        Test-CM_JWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: $($headers)"    
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'DELETE' -Uri $endpoint -Headers $headers -ContentType 'application/json'
        Write-Debug "Response: $($response)"  
    }
    Catch {
        $StatusCode = $_.Exception.Response.StatusCode
        if ($StatusCode -EQ [System.Net.HttpStatusCode]::Conflict) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): User set already exists"
            return
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::Unauthorized) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to connect to CipherTrust Manager with current credentials"
            return
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::NotFound) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to find a Key by that ID to delete"
            return
        }
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "Key deleted"
    return
}    


Export-ModuleMember -Function Get-CM_ListKeys
Export-ModuleMember -Function Get-CM_CreateKey
Export-ModuleMember -Function Get-CM_DeleteKey

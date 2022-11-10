#######################################################################################################################
# File:             CipherTrustManager-Interfaces.psm1                                                                #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
# Notes:            This module is loaded by the master module, CIpherTrustManager                                    #
#                   Do not load this directly                                                                         #
#######################################################################################################################

####
# ENUMS
####
#Interface Types
Add-Type -TypeDefinition @"
   public enum CM_InterfaceTypes {
    nae,
    kmip,
    snmp
}
"@
#
#TLS
Add-Type -TypeDefinition @"
   public enum CM_TLSVersion {
    tls_1_0,
    tls_1_1,
    tls_1_2,
    tls_1_3
}
"@
#
#
Add-Type -TypeDefinition @"
   public enum CM_CertUserFieldOptions {
    CN,
    SN,
    E,
    E_ND, 
    UID,
    OU
}
"@
####

####
# Local Variables
####
$target_uri = "/configs/interfaces"
####

<#
    .SYNOPSIS
        Add a new interface
    .DESCRIPTION
        This allows you to create a key on CIpherTrust Manager and control a series of its parameters. Those parameters include: keyname, usageMask, algo, size, Undeleteable, Unexportable, NoVersionedKey
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
function Get-CM_AddInterface {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [int] $port, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $auto_gen_ca_id,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [switch] $auto_registration,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [CM_CertUserFieldOptions] $cert_user_field,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [int] $custom_uid_size,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [switch] $custom_uid_v2,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $default_connection,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [CM_InterfaceTypes] $interfaceType, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [int] $kmip_enable_hard_delete,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [CM_TLSVersion] $maximum_tls_version,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [switch] $nae_mask_system_groups,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [CM_TLSVersion] $minimum_tls_version,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $mode,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $name,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $network_interface,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $registration_token,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $trusted_cas_local,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $trusted_cas_external
    )

    Write-Debug "Adding an Interface in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"
    $interfaceID = $null
    
    # Mandatory Parameters
    $body = @{
        'port' = $port
    }

    # Optional Parameters
    if ($auto_gen_ca_id) { $body.add('auto_gen_ca_id', $auto_gen_ca_id) }
    if ($auto_registration) { $body.add('auto_registration', $true) } 
    if ($null -ne $cert_user_field) { $body.add('cert_user_field', $cert_user_field.ToString()) }
    if ($auto_registration) { $body.add('custom_uid_size', $custom_uid_size) } 
    if ($custom_uid_v2) { $body.add('custom_uid_v2', $true) }
    if ($default_connection) { $body.add('default_connection', $default_connection) } 
    if ($interfaceType) { $body.add('interfaceType', $interfaceType.ToString()) }
    if ($kmip_enable_hard_delete) { $body.add('kmip_enable_hard_delete', $kmip_enable_hard_delete) }     
    if ($maximum_tls_version) { $body.add('maximum_tls_version', $maximum_tls_version) }
    if ($nae_mask_system_groups) { $body.add('nae_mask_system_groups', $nae_mask_system_groups) } 
    if ($minimum_tls_version) { $body.add('minimum_tls_version', $minimum_tls_version) }
    if ($mode) { $body.add('mode', $mode) } 
    if ($name) { $body.add('name', $name) }
    if ($network_interface) { $body.add('network_interface', $network_interface) } 
    if ($registration_token) { $body.add('registration_token', $registration_token) }

    if ($trusted_cas_local -OR $trusted_cas_external) { 
        $trusted_cas = @{}
        #local cas
        if (($trusted_cas_local -is [String])) { 
            if ($trusted_cas_local) {
                #CA came in as a single string...convert to array
                $trusted_cas.add('local', @($trusted_cas_local)) 
            }
            else {
                #CA is empty...convert to blank array
                $trusted_cas.add('local', @()) 
            }
        }
        else {
            #CA came in as an array
            $trusted_cas.add('local', $trusted_cas_local) 
        } 
        
        #external cas
        if (($trusted_cas_external -is [String])) { 
            if ($trusted_cas_external) {
                #CA came in as a single string...convert to array
                $trusted_cas.add('external', @($trusted_cas_external)) 
            }
            else {
                #CA is empty...convert to blank array
                $trusted_cas.add('external', @()) 
            }
        }
        else {
            #CA came in as an array
            $trusted_cas.add('external', $trusted_cas_external) 
        } 
        $body.add('trusted_cas', $trusted_cas)
    }
    $jsonBody = $body | ConvertTo-Json -Depth 5
    Write-Debug "JSON Body: $($jsonBody)"

    Try {
        Test-CM_JWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: $($headers)"    
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'POST' -Uri $endpoint -Body $jsonBody -Headers $headers -ContentType 'application/json'
        Write-Debug "Response: $($response)"    
        $interfaceID = $response.id

    }
    Catch {
        $StatusCode = $_.Exception.Response.StatusCode
        if ($StatusCode -EQ [System.Net.HttpStatusCode]::Conflict) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Interface already exists on that port"
            return $null
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::Unauthorized) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to connect to CipherTrust Manager with current credentials"
            return $null
        }
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "Interface added"
    return $interfaceID
}    

function Get-CM_ListInterfaces {
    param
    (
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [string] $name, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [int] $skip,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [int] $limit
    )

    Write-Debug "Getting a List of Interfaces configured in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"

    #Set query
    #    $firstset = $false #can skip if there is only one mandatory element
    if ($name) {
        $endpoint += "?name="
        #        $firstset = $true
        $endpoint += $name.ToString()            
    }

    if ($skip) {
        $endpoint += "&skip="
        $endpoint += $skip
    }

    if ($limit) {
        $endpoint += "&limit="
        $endpoint += $limit
    }

    Write-Debug "Endpoint w Query: $($endpoint)"

    Try {
        Test-CM_JWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: $($headers)"    
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'GET' -Uri $endpoint -Body $jsonBody -Headers $headers -ContentType 'application/json'
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
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "List of Interfaces created"
    return $response
}    


function Get-CM_DeleteInterface {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $interface_name
    )

    Write-Debug "Deleting a Interface by ID in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"

    #Set ID
    $endpoint += "/$interface_name"

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
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::BadRequest) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to find an Interface by that name to delete"
            return
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::NotFound) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to find an Interface by that name to delete"
            return
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::Unauthorized) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to connect to CipherTrust Manager with current credentials"
            return
        }
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "Interface deleted"
    return
}    

Export-ModuleMember -Function Get-CM_ListInterfaces
Export-ModuleMember -Function Get-CM_AddInterface
Export-ModuleMember -Function Get-CM_DeleteInterface

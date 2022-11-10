#######################################################################################################################
# File:             CipherTrustManager-Users.psm1                                                                  #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
# Notes:            This module is loaded by the master module, CIpherTrustManager                                    #
#                   Do not load this directly                                                                         #
#######################################################################################################################

<#
    .SYNOPSIS
        Create a new user
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
function Get-CM_CreateUser {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $name, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $username,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $email, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $password, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [hashtable] $app_metadata, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [hashtable] $user_metadata
    )

    Write-Debug "Creating a User in CM"
    $endpoint = $CM_Session.REST_URL + "/usermgmt/users"
    Write-Debug "Endpoint: $($endpoint)"

    # Mandatory Parameters
    $body = @{
        'name'     = $name
        'username' = $username
        'email'    = $email
        'password' = $password
    }

    # Optional Parameters
    if ('app_metadata') {
        $body.add('app_metadata', $app_metadata)
    }
    else {
        $body.add('app_metadata', @{})
    }
    if ('user_metadata') {
        $body.add('user_metadata', $user_metadata)
    }
    else {
        $body.add('user_metadata', @{})
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
    Write-Debug "User created"
    return
}    


function Get-CM_ListUsers {
    param
    (
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true)]
        [string] $name, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $username,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [mailaddress] $email, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $groups, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [string] $auth_domain_name, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [int] $skip,
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [int] $limit
    )

    Write-Debug "Getting a List of Users in CM"
    $endpoint = $CM_Session.REST_URL + "/usermgmt/users"
    Write-Debug "Endpoint: $($endpoint)"

    #Set query
    $firstset = $false
    if ($name) {
        $endpoint += "?name="
        $firstset = $true
        $endpoint += $name            
    }
    if ($username) {
        if ($firstset) {
            $endpoint += "&username="
        }
        else {
            $endpoint += "?username="
            $firstset = $true
        }
        $endpoint += $username
    }
    if ($email) {
        if ($firstset) {
            $endpoint += "&email="
        }
        else {
            $endpoint += "?email="
            $firstset = $true
        }
        $endpoint += $email
    }
    if ($groups) {
        if ($firstset) {
            $endpoint += "&groups="
        }
        else {
            $endpoint += "?groups="
            $firstset = $true
        }
        $endpoint += $groups
    }
    if ($auth_domain_name) {
        if ($firstset) {
            $endpoint += "&auth_domain_name="
        }
        else {
            $endpoint += "?auth_domain_name="
            $firstset = $true
        }
        $endpoint += $auth_domain_name
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
    Write-Debug "List of users created"
    return $response
}    


function Get-CM_DeleteUser {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $user_id
    )

    Write-Debug "Deleting a User by ID in CM"
    $endpoint = $CM_Session.REST_URL + "/usermgmt/users"
    Write-Debug "Endpoint: $($endpoint)"

    #Set ID
    $endpoint += "/$user_id"

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
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "User deleted"
    return
}    

Export-ModuleMember -Function Get-CM_ListUsers
Export-ModuleMember -Function Get-CM_CreateUser
Export-ModuleMember -Function Get-CM_DeleteUser

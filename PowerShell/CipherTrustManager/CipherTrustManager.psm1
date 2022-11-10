#######################################################################################################################
# File:             CipherTrustManager.psm1                                                                           #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Author:           Marc Seguin, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
# Usage:            To load this module in your PowerShell:                                                           #
#                   1. Open PowerShell (or PowerShell ISE).                                                           #
#                   2. Run the following commands                                                                     #
#                      Import-Module -Name CipherTrustManager                                                         #
#                      Initialize-CipherTrustManager                                                                  #
#######################################################################################################################

####
# Module Variables
#
$CM_Session = [ordered]@{
    KMS_IP    = $null
    User      = $null
    Pass      = $null
    REST_URL  = $null
    AuthToken = $null
}
#New-Variable -Name CM_Session -Value $CM_Session -Scope Script -Force
New-Variable -Name CM_Session -Value $CM_Session -Scope Global -Force
#
###

####
# Constants
#
$KMS_NAME = "CipherTrust Manager"
####

<#
    .SYNOPSIS
    Create a connection to CipherTrust Manager and store AuthToken for use in future calls

    .DESCRIPTION
    Create a connection to CipherTrust Manager and store AuthToken (JWT) for use in future calls. It uses Get-JWT to manage the lifecycle of your JWT token so it is `set and forget`

    .PARAMETER server
    Specifies the IP Address or FQDN of CipherTrust Manager.

    .PARAMETER user
    Specifies the username for the account authorized to connect with CipherTrust manager.

    .PARAMETER pass
    Specifies the password (in plaintext for now) for the user.

    .INPUTS
    None. You cannot pipe objects to Connect-CipherTrustManager.

    .OUTPUTS
    None. Connect-CipherTrustManager returns a proxy to this connection.

    .EXAMPLE
    PS> Connect-CipherTrustManager -server 10.23.104.40 -user "user1" -pass "P@ssw0rd!"

    .LINK
    Online version: https://github.com/thalescpl-io/CDSP_Orchestration/tree/main/PowerShell/CipherTrustManager
#>

function Connect-CipherTrustManager {
    param
    (
        [Parameter(Mandatory = $true,
        ValueFromPipelineByPropertyName = $true)]
        [string] $server, 
        [Parameter(Mandatory = $true,
        ValueFromPipelineByPropertyName = $true)]
        [string] $user,
        [Parameter(Mandatory = $true,
        ValueFromPipelineByPropertyName = $true)] 
        [string] $pass
    )

    Write-Debug "Start: $($MyInvocation.MyCommand.Name)"

    $CM_Session.KMS_IP = $server
    $CM_Session.User = $user
    $CM_Session.Pass = $pass

    Write-Debug "Session Parameters: $($CM_Session)"

    #Invoke API for token generation
    Write-Debug "Getting authentication token from $($KMS_NAME)..."
    
    $CM_Session.REST_URL = "https://" + ($CM_Session.KMS_IP) + "/api/v1"

    #Authenticate with CM, get JWT and set BEARER token in Headers
    Get-CM_JWT  

    Write-Debug "End: $($MyInvocation.MyCommand.Name)"
    return
}

###
# Exports
###
#This module
Export-ModuleMember -Function Connect-CipherTrustManager
#Utils
Export-ModuleMember -Function Get-CM_JWT
Export-ModuleMember -Function Test-CM_JWT
Export-ModuleMember -Function Write-HashtableArray
#Keys
Export-ModuleMember -Function Get-CM_ListKeys
Export-ModuleMember -Function Get-CM_CreateKey
Export-ModuleMember -Function Get-CM_DeleteKey
#Users
Export-ModuleMember -Function Get-CM_ListUsers
Export-ModuleMember -Function Get-CM_CreateUser
Export-ModuleMember -Function Get-CM_DeleteUser
#Tokens
Export-ModuleMember -Function Get-CM_AuthTokens
#CAs
Export-ModuleMember -Function Get-CM_ListLocalCAs
#Char Sets
Export-ModuleMember -Function Get-CM_ListCharacterSets
Export-ModuleMember -Function Get-CM_CreateCharacterSet
Export-ModuleMember -Function Get-CM_DeleteCharacterSet
#User Sets
Export-ModuleMember -Function Get-CM_ListUserSets
Export-ModuleMember -Function Get-CM_CreateUserSet
Export-ModuleMember -Function Get-CM_DeleteUserSet
#Masking Formats
Export-ModuleMember -Function Get-CM_ListMaskingFormats
Export-ModuleMember -Function Get-CM_CreateMaskingFormat
Export-ModuleMember -Function Get-CM_DeleteMaskingFormat
#Protection Policies
Export-ModuleMember -Function Get-CM_ListProtectionPolicies
Export-ModuleMember -Function Get-CM_CreateProtectionPolicy
Export-ModuleMember -Function Get-CM_DeleteProtectionPolicy
#Access Policies
Export-ModuleMember -Function Get-CM_ListAccessPolicies
Export-ModuleMember -Function Get-CM_CreateAccessPolicy
Export-ModuleMember -Function Get-CM_DeleteAccessPolicy
Export-ModuleMember -Function Get-CM_CreateUserSetPolicy
#Interfaces
Export-ModuleMember -Function Get-CM_ListInterfaces
Export-ModuleMember -Function Get-CM_AddInterface
Export-ModuleMember -Function Get-CM_DeleteInterface
#DPG Policies
Export-ModuleMember -Function Get-CM_DPG_ListPolicies
Export-ModuleMember -Function Get-CM_DPG_CreatePolicy
Export-ModuleMember -Function Get-CM_DPG_DeletePolicy
Export-ModuleMember -Function Get-CM_DPG_ProxyConfig
Export-ModuleMember -Function Get-CM_DPG_JSONRequestResponse
#ClientProfiles
Export-ModuleMember -Function Get-CM_ListClientProfiles
Export-ModuleMember -Function Get-CM_CreateClientProfile
Export-ModuleMember -Function Get-CM_DeleteClientProfile

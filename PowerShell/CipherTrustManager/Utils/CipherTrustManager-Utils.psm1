#######################################################################################################################
# File:             CipherTrustManager-Tokens.psm1                                                                    #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
# Notes:            This module is loaded by the master module, CIpherTrustManager                                    #
#                   Do not load this directly                                                                         #
#######################################################################################################################

<#
    .SYNOPSIS
        Authenitcate with CipherTrust Manager, get a JWT and store it in the header as a BEARER token for use in future calls

    .DESCRIPTION
        This function gets all of its necessary information from $CM_Session variables within this module
    .EXAMPLE
        PS> Get-CM_JWT
    .NOTES
        NOT EXPORTED. INTERNAL ONLY
#>
function Get-CM_JWT {
    Write-Debug "Start: $($MyInvocation.MyCommand.Name)"

    $CM_Session.AuthToken = $null
    $REST_URL = $CM_Session.REST_URL + "/auth/tokens"

    $Body = @{
        #        grant_type = "password"
        username = $CM_Session.User
        password = $CM_Session.Pass
    }
    
    Try {
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'POST' -Uri $REST_URL -Body $Body
        Write-Debug "Response: $($response)"
    }
    Catch {
        $StatusCode = $_.Exception.Response.StatusCode
        if ($StatusCode -EQ $null) {
            Write-Error "Connection Timeout Error. Unable to reach CipherTrust Manager." -ErrorAction Stop
        }
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }    
    }

    $CM_Session.AuthToken = $response.jwt 
    Write-Debug "End: $($MyInvocation.MyCommand.Name)"
    return
}

<#
    .SYNOPSIS
        Authenitcate with CipherTrust Manager, get a JWT and store it in the header as a BEARER token for use in future calls

    .DESCRIPTION
        This function gets all of its necessary information from $CM_Session variables within this module
    .EXAMPLE
        PS> Get-CM_JWT
    .NOTES
        NOT EXPORTED. INTERNAL ONLY
#>
function Test-CM_JWT {
    Write-Debug "Start: $($MyInvocation.MyCommand.Name)"

    Write-Debug "Time to expire (sec): $((get-jwtdetails $CM_Session.AuthToken).timeToExpiry.TotalSeconds)"
    if ((get-jwtdetails $CM_Session.AuthToken).timeToExpiry.TotalSeconds -lt 60) {
        Write-Debug "JWT is close to or past expiry. Refreshing token."
        Get-CM_JWT
    }
    else {
        Write-Debug "JWT not close to or past expiry"
    }

    Write-Debug "End: $($MyInvocation.MyCommand.Name)"
    return
}
####

function Write-HashtableArray {
    param(
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true,
            Position = 0)]
        [AllowEmptyCollection()]
        [hashtable[]]$Hashtables
    )

    Write-Debug "@("
    foreach ($hashtable in $Hashtables) {
        Write-Debug "  @{"
        foreach ($entry in $hashtable.GetEnumerator()) {
            Write-Debug "     $($entry.Key) = $($entry.Value)"
        }
        Write-Debug "  }"
    }
    Write-Debug ")"    
}

Export-ModuleMember -Function Get-CM_JWT
Export-ModuleMember -Function Test-CM_JWT
Export-ModuleMember -Function Write-HashtableArray

#######################################################################################################################
# File:             CipherTrustManager-Users.psm1                                                                  #
# Author:           Anurag Jain, Developer Advocate                                                                   #
# Author:           Marc Seguin, Developer Advocate                                                                   #
# Publisher:        Thales Group                                                                                      #
# Copyright:        (c) 2022 Thales Group. All rights reserved.                                                       #
# Notes:            This module is loaded by the master module, CipherTrustManager                                    #
#                   Do not load this directly                                                                         #
#######################################################################################################################

####
# Local Variables
####
$target_uri = "/usermgmt/users"
####


<#
    .SYNOPSIS
        Create a new User
    .DESCRIPTION
        This allows you to create a new User on CipherTrust Manager and control a series of its parameters.
    .PARAMETER name
        Full name/Display name of User 
    .PARAMETER ps_creds
        PSCredential of User (use PSCredental or username/SecureString or username/plaintext but not all three)
    .PARAMETER username
        Account name of User...must come with -secure_password or -password
    .PARAMETER secure_password 
        SecureString password for User (use PSCredental or username/SecureString or username/plaintext but not all three)    
    .PARAMETER password 
        Plaintext password for User (use PSCredental or username/SecureString or username/plaintext but not all three)
    .PARAMETER email 
        Email address for User. Must be UNIQUE for all of CipherTrust Manager
    .PARAMETER app_metadata 
        A schema-less object, which can be used by applications to store information about the resource. `app_metadata` is typically used by applications to store information which the end-users are not themselves allowed to change, like group membership or security roles.
    .PARAMETER user_metadata        
        A schema-less object, which can be used by applications to store information about the resource. `user_metadata` is typically used by applications to store information about the resource which the end-users are allowed to modify, such as user preferences.
    .EXAMPLE
        PS> New-CMUser -email <email> -name <full name> -ps_creds <PSCredential>

        This creates a User with basic settings using a PSCredential.
    .EXAMPLE
        PS> New-CMUser -email <email> -name <full name> -username <account name> -secure_password <SecureString>

        This creates a User with basic settings. Password is provided in SecureString
    .EXAMPLE
        PS> New-CMUser -email <email> -name <full name> -username <account name> -password <plaintext>

        This creates a User with basic settings. Password is provided in plaintext (least secure)
    .LINK
        https://github.com/thalescpl-io/CDSP_Orchestration/tree/main/PowerShell/CipherTrustManager
#>
function New-CMUser {
    [CmdletBinding(DefaultParameterSetName = 'by PSCredential')]
    [Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingPlainTextForPassword', 
        '', 
        Justification = 'Allowing for choice. Customer can pass SecureString if they have it')]
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $name, 
        [Parameter(Mandatory = $true,
            ParameterSetName = 'by PSCredential',
            ValueFromPipelineByPropertyName = $true )]
        [System.Management.Automation.PSCredential] $ps_creds,
        [Parameter(Mandatory = $true,
            ParameterSetName = 'by SecureString',
            ValueFromPipelineByPropertyName = $true )]
        [Parameter(Mandatory = $true,
            ParameterSetName = 'by Plaintext',
            ValueFromPipelineByPropertyName = $true )]
        [string] $username,
        [Parameter(Mandatory = $true,
            ParameterSetName = 'by SecureString',
            ValueFromPipelineByPropertyName = $true )]
        [SecureString] $secure_password, 
        [Parameter(Mandatory = $true,
            ParameterSetName = 'by Plaintext',
            ValueFromPipelineByPropertyName = $true )]
        [string] $password, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        #Email address for User
        [string] $email, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        #Plaintext password for User
        [hashtable] $app_metadata, 
        [Parameter(Mandatory = $false,
            ValueFromPipelineByPropertyName = $true )]
        [hashtable] $user_metadata
    )
    Write-Debug "Start: $($MyInvocation.MyCommand.Name)"

    Write-Debug "Creating a User in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"

    # Mandatory Parameters
    $body = @{
        'name'  = $name
        'email' = $email
    }

    #if we are using PSCredential parameter set
    Write-Debug "ParameterSetName $($PSCmdlet.ParameterSetName)"
    if ($PSCmdlet.ParameterSetName -eq 'by PSCredential') {
        $body.add('username', $ps_creds.UserName)
        $body.add('password', (ConvertFrom-SecureString $ps_creds.Password -AsPlainText))
    }
    elseif ($PSCmdlet.ParameterSetName -eq 'by SecureString') {
        $body.add('username', $username)
        $body.add('password', (ConvertFrom-SecureString $secure_password -AsPlainText)) 
    }
    elseif ($PSCmdlet.ParameterSetName -eq 'by Plaintext') {
        $body.add('username', $username)
        $body.add('password', $password) 
    }
    else {
        Write-Error "Did not get the proper ParameterSetName. Got $($PSCmdlet.ParameterSetName)"
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
        Test-CMJWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: "
        Write-HashtableArray $($headers)    
        $response = Invoke-RestMethod -SkipCertificateCheck -Method 'POST' -Uri $endpoint -Body $jsonBody -Headers $headers -ContentType 'application/json'
        Write-Debug "Response: $($response)"  
    }
    Catch {
        $StatusCode = $_.Exception.Response.StatusCode
        if ($StatusCode -EQ [System.Net.HttpStatusCode]::Conflict) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): User already exists" -ErrorAction Continue
        }
        elseif ($StatusCode -EQ [System.Net.HttpStatusCode]::Unauthorized) {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): Unable to connect to CipherTrust Manager with current credentials" -ErrorAction Stop
        }
        else {
            Write-Error "Error $([int]$StatusCode) $($StatusCode): $($_.Exception.Response.ReasonPhrase)" -ErrorAction Stop
        }
    }
    Write-Debug "User created"
    Write-Debug "End: $($MyInvocation.MyCommand.Name)"

    return
}    


<#
    .SYNOPSIS
        List Users
    .DESCRIPTION
        Returns a list of all user resources. The results can be filtered, using the query parameters. Wildcards are supported.

        Results are returned in pages. Each page of results includes the total results found, and information for requesting the next page of results, using the skip and limit query parameters.    
    .PARAMETER name
        Filter by the User's Full name/Display name
    .PARAMETER username
        Filter by the Username/Account name of User
    .PARAMETER email 
        Filter by the User's Email address
    .PARAMETER groups 
        Filter by the Users in the given group name. Using `nil` as the group name will return users that are not part of any group.
    .PARAMETER auth_domain_name
        Filter by the User's Auth Domain
    .PARAMETER skip
        The index of the first resource to return. Equivalent to `offset` in SQL.
    .PARAMETER limit
        The max number of resources to return. Equivalent to `limit` in SQL.
    .EXAMPLE
        PS> Find-CMUsers -name "Bob*"

        Returns a list of all users whose name starts with "Bob"
    .LINK
        https://github.com/thalescpl-io/CDSP_Orchestration/tree/main/PowerShell/CipherTrustManager
#>
#function Get-CM_ListUsers {
function Find-CMUsers {
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
    Write-Debug "Start: $($MyInvocation.MyCommand.Name)"

    Write-Debug "Getting a List of Users in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"

    #Set query
    $isQuery=$false
    $firstset = $false
    if ($name) {
        $endpoint += "?name="
        $firstset = $true
        $endpoint += $name
        $isQuery = $true            
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
        $isQuery = $true            
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
        $isQuery = $true            
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
        $isQuery = $true            
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
        $isQuery = $true            
    }

    if(-NOT $isQuery){
        throw "No search parameters provided"
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
        Test-CMJWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: "
        Write-HashtableArray $($headers)      
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
    Write-Debug "End: $($MyInvocation.MyCommand.Name)"
    return $response
}    

<#
    .SYNOPSIS
        Delete User
    .DESCRIPTION
        Deletes a user given the user's user-id. 
        If the current user is logged into a sub-domain, the user is deleted from that sub-domain. 
        If the current user is logged into the root domain, the user is deleted from all domains it belongs to.    
    .PARAMETER id
        The ID of the user to be deleted. Can be obtained through Find-CMUsers
    .EXAMPLE
        PS> $toDelete = Find-CMUsers -name "Bob Smith" #assuming there is only ONE `Bob Smith` in CipherTrust Manager
        PS> Remove-CMUser -id $toDelete.resources[0].id

        Deletes the user `Bob Smith` by the user's id
    .LINK
        https://github.com/thalescpl-io/CDSP_Orchestration/tree/main/PowerShell/CipherTrustManager
#>
function Remove-CMUser {
    param
    (
        [Parameter(Mandatory = $true,
            ValueFromPipelineByPropertyName = $true)]
        [string] $id
    )
    Write-Debug "Start: $($MyInvocation.MyCommand.Name)"

    Write-Debug "Deleting a User by ID in CM"
    $endpoint = $CM_Session.REST_URL + $target_uri
    Write-Debug "Endpoint: $($endpoint)"

    #Set ID
    $endpoint += "/$id"

    Write-Debug "Endpoint with ID: $($endpoint)"

    Try {
        Test-CMJWT #Make sure we have an up-to-date jwt
        $headers = @{
            Authorization = "Bearer $($CM_Session.AuthToken)"
        }
        Write-Debug "Headers: "
        Write-HashtableArray $($headers)      
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
    Write-Debug "End: $($MyInvocation.MyCommand.Name)"
    return
}    

Export-ModuleMember -Function Find-CMUsers
Export-ModuleMember -Function New-CMUser
Export-ModuleMember -Function Remove-CMUser

# PowerShell Module for CipherTrust Manager (CDSP_Orchestration)
This PowerShell Module offers simple integration between a PowerShell script and CipherTrust Manager

## Prerequisite

Download this module (available as [CipherTrustManager.zip](CipherTrustManager.zip) for simplicity) and put it in the Modules directory on your Windows computer. These Modules are usually put in C:\Users\<current user>\Documents\WindowsPowerShell\Modules but you can install it anywhere the $Env:PSModulePath can find it


## Usage

1. In your PowerShell script, add `Import-Module CipherTrustManager -Force -ErrorAction Stop`. The `-Force` will ensure that the module is overwritten if already loaded. The `-ErrorAction Stop` will abort your script if the module cannot be found.
2. #Initialize and authenticate a connection with CipherTrust Manager

```powershell
Connect-CipherTrustManager `
    -server <ip_address_of_CipherTrust_Manager> `
    -user <account_with_access> `
    -pass <password_for_that_account>
```

3. At this point, you are connected and authenticated so you can make any calls that the REST API and PowerShell Module supports

## Notes
As best we could, we have added documentation and help to the module. To see what a command can do AND get examples:

* For basic help
  
```powershell
Get-Help Connect-CipherTrustManager
```

* To see examples

```powershell
Get-Help Connect-CipherTrustManager -examples
```

* For full help

```powershell
Get-Help Connect-CipherTrustManager -full
```

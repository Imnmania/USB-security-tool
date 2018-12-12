import os
import subprocess

def registryClear():
    print("Registry Clean")
    asd = "Get-ChildItem -path HKLM:\ -Recurse | where { $_.Name -match 'office12'} | Remove-Item -Force"
    returned_value = os.system(asd)
    print("Registry Cleaning Complete= ",returned_value)
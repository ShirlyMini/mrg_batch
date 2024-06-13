*** Settings ***
Library    SSHLibrary

*** Test Cases ***
Open Connection to local server
    Open Connection   192.168.1.9
    Execute Command    date
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://admin-demo.nopcommerce.com/
#${usr}   admin@yourstore.com
#${pswd}    admin
# @{lst}   1    2    3    4
#@{cred}   admin@yourstore.com    admin
# &{dict}    key1=value1   key2=value2   key3=value3
&{cred_dict}    user=admin@yourstore.com   pass=admin


*** Test Cases ***
TestCase1: Verify Login page title
    Open Browser   url=${url}    browser=chrome   #executable_path=E:\selenium\drivers\
    Maximize Browser Window
#    ${title}    Get Title
#    Log   ${title}    console=True
    ${title}    Log Title
    Log   ${title}    console=True
    Close Browser

TestCase2: Verify Dashbord page
    Open Browser   url=${url}    browser=chrome
    Maximize Browser Window
    # scalar
#    Input Text   id:Email    ${usr}    clear=True
#    Input Text   id:Password    ${pswd}    clear=True
    # list
#    Input Text   id:Email    ${cred[0]}    clear=True
#    Input Text   id:Password    ${cred[1]}    clear=True
    # dict
    Input Text   id:Email    ${cred_dict['user']}    clear=True
    Input Text   id:Password    ${cred_dict['pass']}    clear=True
    Click Element   xpath://button[@type="submit"]
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser

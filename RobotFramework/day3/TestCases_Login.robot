*** Settings ***
Library    SeleniumLibrary
Resource    ./resource.robot    #current folder
#Resource    ../../day2/
#Resource    ./keyword/resource1.robot


*** Variables ***
${url}   https://admin-demo.nopcommerce.com/
&{cred_dict}    user=admin@yourstore.com   pass=admin


*** Test Cases ***
TestCase1: Verify Dashbord page
    [tags]   tc1   sanity
    #Set Log Level   Trace
    Open Browser   url=${url}    browser=chrome    #executable_path=E:/selenium/drivers/chromedriver.exe
    Maximize Browser Window
    Login with Username and Password-basic
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser

TestCase2: Verify Dashbord page with parameter
    [tags]   tc2
    Open Browser   url=${url}    browser=chrome
    Maximize Browser Window
    Login with Username and Password-with parameter   ${cred_dict['user']}   ${cred_dict['pass']}
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser

TestCase3: Verify Dashbord page with return
    [tags]   tc3   sanity
    Open Browser   url=${url}    browser=chrome
    Maximize Browser Window
    ${verify_title}   Login with Username and Password-with return   ${cred_dict['user']}   ${cred_dict['pass']}
    Run Keyword If    '${verify_title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser
*** Settings ***
Library    SeleniumLibrary
Resource    ./resource.robot
Test Setup    NopCommerce Test Setup
Test Teardown    NopCommerce Test teardown
Suite Setup    Set Log Level   Trace
Suite Teardown   Close All Browsers


*** Variables ***
${url}   https://admin-demo.nopcommerce.com/
&{cred_dict}    user=admin@yourstore.com   pass=admin

*** Test Cases ***
TestCase1: Verify Dashbord page
    [tags]   tc1   sanity
    #
    Login with Username and Password-basic
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail


TestCase2: Verify Dashbord page with parameter
    [tags]   tc2
    Login with Username and Password-with parameter   ${cred_dict['user']}   ${cred_dict['pass']}
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail


TestCase3: Verify Dashbord page with return
    [tags]   tc3   sanity
    ${verify_title}   Login with Username and Password-with return   ${cred_dict['user']}   ${cred_dict['pass']}
    Run Keyword If    '${verify_title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
